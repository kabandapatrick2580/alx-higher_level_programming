#!/usr/bin/python3
import urllib.request
import sys


def get_x_request_id(url):
    """
    Sends a request to the given URL and displays the
    value of the X-Request-Id variable.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable.
    """
    try:
        with urllib.request.urlopen(url) as response:
            x_request_id = response.headers.get('X-Request-Id')
            return x_request_id
    except urllib.error.URLError as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]

    x_request_id_result = get_x_request_id(url_to_fetch)

    if x_request_id_result:
        print(x_request_id_result)
    else:
        print("Failed to retrieve X-Request-Id.")
