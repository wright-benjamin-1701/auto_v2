import requests
import dotenv

default_settings = {
    'starting_url': 'https://en.wikipedia.org/wiki/List_of_science_fiction_novels', #'https://en.wikipedia.org/wiki/List_of_jazz_albums',# If you modify this,
    # make sure to respect the robots.txt file on the sites you visit
    'internal_links_only' : True, #whether to filter out links not from the same domain. If you turn this off,
    # make sure to modify the code to respect the robots.txt file on the sites you visit
    'request_throttle_limit':10000, #requests per period
    'batch_size':25, 
    'number_of_batches':3
}

starting_content = requests.get(default_settings['starting_url']).text

default_database_url = 'sqlite:///crawler.db'
env_connection = dotenv.dotenv_values().get('SQL_CONNECTION')
database_url = default_database_url

if(env_connection != None):
    database_url = env_connection

class SearchSettings():
    def __init__(self, **kwargs):
        self.starting_url = kwargs['starting_url']
        self.internal_links_only = kwargs['internal_links_only']
        self.request_throttle_limit = kwargs['request_throttle_limit']
        self.batch_size = kwargs['batch_size']
        self.starting_content = starting_content
        self.number_of_batches = kwargs['number_of_batches']

default_search_settings = SearchSettings(**default_settings)
