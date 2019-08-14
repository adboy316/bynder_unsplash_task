# Authentication Module

import os
import requests

import urllib.parse as urlparse

# Unsplash urls
auth_base_url = 'https://unsplash.com/oauth/authorize'
token_url = 'https://unsplash.com/oauth/token'


def get_token(access_key, secret_key, redirect_uri, scope):
    """ Returns JSONaccess token """

    auth_params = {'client_id': access_key, 'redirect_uri': redirect_uri,
                   'response_type': 'code', 'scope': scope}

    # Direct the user to authorize link with required auth_params
    auth = requests.post(
        'https://unsplash.com/oauth/authorize', params=auth_params)

    print(f'Please go to {auth.url} and authorize access.')
    authorization_response = input('Enter the full callback URL: ')

    parsed_code_url = urlparse.urlparse(authorization_response)
    code = urlparse.parse_qs(parsed_code_url.query)['code']

    # Get Token
    token_params = {'client_id': access_key, 'client_secret': secret_key,
                    'redirect_uri': redirect_uri, 'code': code, 'grant_type': 'authorization_code'}

    token = requests.post(
        'https://unsplash.com/oauth/token', params=token_params)
    return token.json()
