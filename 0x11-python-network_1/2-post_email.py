#!/usr/bin/python3

"""
This script sends a POST request to a specified URL with an email parameter
and displays the body of the response (decoded in utf-8).

Usage:
    $ ./script.py <URL> <email>
"""

import sys
import urllib.request
import urllib.parse


def send_post_request(url: str, email: str) -> None:
    """
    Sends a POST request to the specified URL with the email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include as a parameter.

    Returns:
        None
    """
    try:
        # Create a dictionary containing the email parameter
        params = {"email": email}

        # Encode the data as ASCII
        data = urllib.parse.urlencode(params).encode("ascii")

        # Create a POST request with the data
        request = urllib.request.Request(url, data)

        # Send the POST request and get the response
        with urllib.request.urlopen(request) as response:
            # Read and decode the response body as utf-8
            print(response.read().decode("utf-8"))
    except urllib.error.URLError as e:
        # Handle any URL-related errors
        print("Error:", e)


if __name__ == "__main__":
    # Check if both URL and email arguments are provided
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url_input = sys.argv[1]
    email_input = sys.argv[2]
    send_post_request(url_input, email_input)
