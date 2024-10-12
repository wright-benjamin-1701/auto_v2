import aiohttp
import requests  # Import the requests module to handle HTTP requests.
from throttler import Throttler


async def fetch_page(
    session: aiohttp.ClientSession, throttler: Throttler, url: str
) -> str:
    try:
        # make GET request using session
        async with throttler, session.get(url) as response:
            # return HTML content
            html = await response.text()
        return html, url

    except Exception as e:
        pass


def fetch_page_synchronous(url):
    response = requests.get(url)
    return response.text
