#!/usr/bin/python3
import urllib.request

def fetch_url_content(url):
    """
    Fetches the content of a given URL using urllib.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The content of the URL.
    """
    try:
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')
            return content
    except urllib.error.URLError as e:
        return f"Error fetching URL: {e}"

if __name__ == "__main__":
    url_to_fetch = "https://alx-intranet.hbtn.io/status"

    content_result = fetch_url_content(url_to_fetch)

    print("Body response:")
    print("\t- type:", type(content_result))
    print("\t- content:", content_result)
