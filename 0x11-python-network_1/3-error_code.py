#!/usr/bin/python3
import urllib.request
import urllib.error
import sys


def fetch_url_content(url):
    """
    Sends a request to the given URL and displays the body of the response.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The decoded content of the response.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            return content
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
        return None
    except urllib.error.URLError as e:
        return f"Error fetching URL: {e}"


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <URL>")
        sys.exit(1)

    url_to_fetch = sys.argv[1]

    response_content = fetch_url_content(url_to_fetch)

    if response_content is not None:
        print(response_content)
