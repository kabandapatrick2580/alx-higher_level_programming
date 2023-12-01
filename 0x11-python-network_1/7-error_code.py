#!/usr/bin/python3

"""
A script that:
- takes in a URL
- sends a request to the URL
- displays the body of the response
- handles HTTP status codes
"""

import sys
import requests


def fetch_and_display_response(url: str) -> None:
    """
    Fetches a URL, checks the HTTP status code, and displays the error
    code if it's greater than or equal to 400.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        response_object = requests.get(url)

        # Check if the HTTP status code indicates an error (>= 400)
        if response_object.status_code >= 400:
            print("Error code:", response_object.status_code)
        else:
            # Display the response body for successful requests
            print("Response body:")
            print(response_object.text)
    except requests.exceptions.RequestException as request_error:
        # Handle any request-related errors
        print("Error:", request_error)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]
    fetch_and_display_response(url_to_fetch)
