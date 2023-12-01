#!/usr/bin/python3

"""
A script that fetches https://alx-intranet.hbtn.io/status using the
requests package.
"""

import requests


def fetch_and_display_status(url: str) -> None:
    """
    Fetches the specified URL and displays the body of the response
    with tabulation.

    Args:
        url (str): The URL to fetch.

    Returns:
        None
    """
    try:
        # Send a GET request to the specified URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            body = response.text
            print("Body response:")
            print(f"\t- type: {type(body)}")
            print(f"\t- content: {body}")
        else:
            print(f"Error: HTTP Status Code {response.status_code}")

    except requests.exceptions.RequestException as e:
        # Handle any request-related errors
        print("Error:", e)


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch_and_display_status(url)
