import requests

default_settings = {
    'starting_url': 'https://en.wikipedia.org/wiki/List_of_science_fiction_novels', #'https://en.wikipedia.org/wiki/List_of_jazz_albums',# If you modify this,
    # make sure to respect the robots.txt file on the sites you visit
    'internal_links_only' : True, #whether to filter out links not from the same domain. If you turn this off,
    # make sure to modify the code to respect the robots.txt file on the sites you visit
    'depth' : 2, # max depth of your search. A depth of 2 gets all the pages which are links and links of links from the starting_url
    'request_throttle_limit':(10000,1), #requests per period
    'batch_size':100, 
    'absolute_page_limit':500000, # this is only checked after a batch completes, so it is possible to exceed it by the (size of a batch)*(average number of links per batch)
}

starting_content = requests.get(default_settings['starting_url']).text

class SearchSettings():
    def __init__(self, **kwargs):
        self.starting_url = kwargs['starting_url']
        self.internal_links_only = kwargs['internal_links_only']
        self.depth = kwargs['depth']
        self.request_throttle_limit = kwargs['request_throttle_limit']
        self.batch_size = kwargs['batch_size']
        self.absolute_page_limit = kwargs['absolute_page_limit']
        self.starting_content = starting_content

default_search_settings = SearchSettings(**default_settings)
