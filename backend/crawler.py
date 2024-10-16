import asyncio
import aiohttp
from throttler import Throttler
import time
import crud
from services.web_services import fetch_page
import settings
import services.database_services
import models
import core.soup_processing
from urllib.parse import urlparse
from datetime import datetime


# processes a batch of pages of the same depth in a breadth-first web crawling algorithm
async def process_batch(
    throttler: Throttler, settings=settings.default_search_settings
):
    t = time.time()

    netloc = urlparse(settings.starting_url).netloc
    internal_only = settings.internal_links_only

    # fetches the html data from the urls in the batch in an async session
    async with aiohttp.ClientSession() as session:

        destination_links = []
        fetch_urls = []

        db_session = models.Session()
        pages = services.database_services.get_unprocessed_page_batch(
            db_session, settings.batch_size
        )
        for page in pages:

            destination_links = core.soup_processing.get_links_from_page(page)
            crud.update_page(session=db_session, db_page=page)
            fetch_urls += destination_links

        for url in fetch_urls:
            link = models.LinkCreate(source=page.url,destination=url)
            crud.create_link(session=db_session,link_create=link)

        db_session.close()

        fetch_urls = list(set(fetch_urls))

        tasks = []
        print(f"fetching {len(fetch_urls)} pages")
        # loop through URLs and append tasks
        for url in fetch_urls:
            if urlparse(url).netloc != netloc and internal_only:
                pass
            else:
                tasks.append(fetch_page(session, throttler, url))

        # group and Execute tasks concurrently
        html_url_pairs = await asyncio.gather(*tasks)

        db_session = models.Session()
        # todo: batch insert, skip names gracefully
        for html, url in html_url_pairs:

            core.soup_processing.process_new_page(html, url, db_session)

        db_session.close()

        print(f"Split time: {time.time()-t}")


# the main program
async def main():

    throttler = Throttler(
        settings.default_search_settings.request_throttle_limit[0]
    )  # throttle network requests - wikipedia allows web crawling at small, slow scales
    async with aiohttp.ClientSession() as session:

        for i in range(3):
            await process_batch(
                throttler=throttler, settings=settings.default_search_settings
            )
    print()

if __name__ == "__main__":
    asyncio.run(main())
