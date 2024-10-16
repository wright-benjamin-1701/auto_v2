import requests

default_settings = {
    'starting_url': 'https://en.wikipedia.org/wiki/List_of_science_fiction_novels', #'https://en.wikipedia.org/wiki/List_of_jazz_albums',# If you modify this,
    # make sure to respect the robots.txt file on the sites you visit
    'internal_links_only' : True, #whether to filter out links not from the same domain. If you turn this off,
    # make sure to modify the code to respect the robots.txt file on the sites you visit
    'request_throttle_limit':(10000,1), #requests per period
    'batch_size':25, 
}

starting_content = requests.get(default_settings['starting_url']).text
database_url = 'postgresql://postgres:changethis@localhost/benwright'


class SearchSettings():
    def __init__(self, **kwargs):
        self.starting_url = kwargs['starting_url']
        self.internal_links_only = kwargs['internal_links_only']
        self.request_throttle_limit = kwargs['request_throttle_limit']
        self.batch_size = kwargs['batch_size']
        self.starting_content = starting_content

default_search_settings = SearchSettings(**default_settings)
