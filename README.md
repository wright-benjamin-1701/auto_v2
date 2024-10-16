# auto_v2
version two of the web crawler

TL;DR Quickstart:
1. Update settings.py with the URL you want to start a web crawl on.
2. Run crawler.py to start the crawler. 

More Customization:
1. You can add a .env file with an SQL_CONNECTION variable to connect to a different SQL database. By default, SQLite is used and an SQLite database is created if none exists.
2. The internal links only setting is used to restrict the crawler to parsing links on the page that match the domain of the starting URL.
3. Adjust the throttle limit to allow more simultaneous requests for web data. Note, however, you are still bottlenecked by processing the pages for links and writing to the database. 
4. You can adjust how many batches of URLs are processed in the settings as well. My experience has been every batch of 5 URLs yields about 1200 links to process in under 30 seconds, and 100 URLs takes about 10 minutes.
5. Feel free to import functions of crawler into other scripts to suit more custom algorithms.

=========================================================================================

This is an upgraded version of previous development I've done. It is a custom web crawler. Technically, it will run breadth-first searches in batches for links on a web pages, and follow them out to the next layer the web. It was designed specifically for Wikipedia, but you can modify settings to suit your own needs.

The default settings are found in settings.py. You can modify the start point of the crawl here, or create your own settings object based on the class here and pass it into the crawler function in crawler.py.

The crawler stores data in an SQLite database specified in models.py. The database is created automatically if it doesn't exist. You can modify the database name and location in models.py.

