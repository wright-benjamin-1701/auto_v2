from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup

from models import PageCreate, PageUpdate
from crud import try_create_page
from datetime import datetime


# get all the links from a Beautiful Soup as urls
def get_links_from_page(page) -> list[str]:

    links = []

    if page.content == None or len(page.content) < 256:
        return []

    base_url = page.url
    soup = BeautifulSoup(page.content, "html.parser")

    default_scheme = "https://"

    for link in soup.find_all("a"):

        found_link = link.get("href")
        parsed_result = urlparse(found_link)

        if parsed_result.netloc == None or parsed_result.netloc == "":
            # use only the scheme, netloc and path for internal links (ignore fragments)
            links.append(urljoin(base_url, parsed_result.path))

        else:
            # if the link is a full ink, we still only want the scheme, netloc and path
            links.append(
                urljoin(default_scheme, parsed_result.netloc, parsed_result.path)
            )

    return list(set(links))


def page_df_row_to_page_update(page_df_row):

    page_update = PageUpdate(
        id=page_df_row["id"],
        title=page_df_row["title"],
        url=page_df_row["url"],
        content=page_df_row["content"],
        added=page_df_row["added"],
        updated=page_df_row["updated"],
    )
    return page_update


def process_new_page(content, url, session):

    page_create = PageCreate(
        url=url,
        content=content,
        added=datetime.now(),
        updated=None,
    )
    try_create_page(session=session, page_create=page_create)
