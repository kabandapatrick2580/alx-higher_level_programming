#!/usr/bin/python3

"""
This script performs the following tasks:
- Takes in a URL.
- Sends a request to the URL.
- Displays the body of the response (decoded in utf-8).
- Handles urllib.error.HTTPError exceptions.

Usage:
    $ ./script.py <URL>
"""

import sys
import urllib.request
import urllib.error


def fetch_and_display_response(url: str) -> None:
    """
    Fetches a URL and displays the body of the response.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        with urllib.request.urlopen(url) as response:
            # Read and decode the response body
            response_body = response.read().decode('utf-8')

            print("Response body:")
            print(response_body)
    except urllib.error.HTTPError as e:
        # Handle HTTP errors and print the HTTP status code
        print("HTTP Error code:", e.code)
    except urllib.error.URLError as e:
        # Handle URL-related errors (e.g., invalid URL)
        print("URL Error:", e)


if __name__ == "__main__":
    # Check if a URL argument is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url_input = sys.argv[1]
    fetch_and_display_response(url_input)
