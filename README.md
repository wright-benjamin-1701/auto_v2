# auto_v2
version two of the web crawler

TL;DR Quickstart:
1. Update settings.py with the URL you want to start a web crawl on.
2. Run crawler.py to start the crawler. 

This is an upgraded version of previous development I've done. It is a custom web crawler. Technically, it will run breadth-first searches in batches for links on a web pages, and follow them out to the next layer the web. It was designed specifically for Wikipedia, but you can modify settings to suit your own needs.

The default settings are found in settings.py. You can modify the start point of the crawl here, or create your own settings object based on the class here and pass it into the crawler function in crawler.py.

The crawler stores data in an SQLite database specified in models.py. The database is created automatically if it doesn't exist. You can modify the database name and location in models.py.

