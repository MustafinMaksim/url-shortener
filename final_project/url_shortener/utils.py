# This file stores important functions for requests handling


import re
import os
import hashlib
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest


def is_valid_url(url: str) -> bool:

    '''
    A function to validate input full url

            Parameters:
                    url (str): Input full url

            Returns:
                    True - input full URL is URL indeed
                    False - input full URL is not URL  
    '''

    # check if url is not None
    if url is not None:

        # compile regex for validating
        regex = re.compile(
            r'^https?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)

        # validating 
        if regex.search(url):
                return True
        else:
                return False

    else: 
        return False


def hash_url(url: str):

    '''
    A function to compute SHA256 hash of url with pbkdf2 algorithm with salt.

            Parameters:
                    url (str): Input full url

            Returns:
                    hex_hash  
    '''

    if isinstance(url, str):

        # creating salt
        salt = os.urandom(32)

        # encoding input url to utf-8
        plain_text = url.encode('utf-8')

        # computing hash of url
        digest = hashlib.pbkdf2_hmac('md5', plain_text, salt, 10000)
        hex_hash = digest.hex()

        return hex_hash[0:8]

    return None


def form_short_url(request, hash_url: str):

    '''
    A function to create short url for user on template

            Parameters:
                    request: 
                    hash_url: str

            Returns:
                    short url 
    '''

    return HttpRequest.get_host(request) + "/u/" + hash_url

