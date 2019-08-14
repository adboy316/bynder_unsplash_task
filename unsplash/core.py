# -*- coding: utf-8 -*-
import auth
import requests


# Constants
API_URL = 'https://api.unsplash.com/'
access_key = 'd26fde1909ce78f465b6e16cf0bdd99e902cb1f83127aa599fe4329bf7208afb'
secret_key = '271c0b15e47fa6314bcb13e1cd1d55850a6c58a7ef5b2a42922176ad3121ab53'
redirect_uri = 'urn:ietf:wg:oauth:2.0:oob'
scope = 'public+read_user+write_collections'

token_info = auth.get_token(access_key, secret_key, redirect_uri, scope)

auth_token = token_info['access_token']

head = {'Authorization': 'Bearer ' + auth_token}


def get_user_profile():
    """ Retrieve private details of user. """
    return get_endpoint('me')


def get_photos(page=1, per_page=10, order_by='latest'):
    """ Get a single page from the list of all photos. """
    params = {'page': page, 'per_page': per_page, 'order_by': order_by}
    return get_endpoint('photos', params=params)


def get_collections(page=1, per_page=10):
    """ Get a single page from the list of all collections. """
    params = {'page': page, 'per_page': per_page}
    return get_endpoint('collections', params=params)


def create_collections(title, description="", private=False):
    """ Create a new collection. This requires the write_collections scope.  """
    payload = {'title': title, 'description': description, 'private': private}
    return post_endpoint('collections', payload=payload)


# Helper functions
def get_endpoint(endpoint, params=None):
    return requests.get(API_URL+endpoint, headers=head, params=params)


def post_endpoint(endpoint, payload=None):
    return requests.post(API_URL+endpoint, headers=head, data=payload)


# Simple Tests
user_profile = get_user_profile()
print(user_profile.text)

photos = get_photos()
print(photos.text)

collections = get_collections()
print(collections.json())

new_collection = create_collections("Hello", "Hello Collection", False)
print(new_collection.text)
