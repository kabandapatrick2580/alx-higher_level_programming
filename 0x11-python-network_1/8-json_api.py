#!/usr/bin/python3

"""
A script that:
- takes in a letter as an argument
- sends a POST request to http://0.0.0.0:5000/search_user with the
  letter as a parameter
- handles the response based on JSON formatting and content
"""

import sys
import requests


def search_user_by_letter(letter_argument: str) -> None:
    """
    Sends a POST request to search for a user with the
    given letter as a parameter.

    Args:
        letter_argument (str): The letter to search for.

    Returns:
        None
    """
    try:
        # Define the URL
        search_url = 'http://0.0.0.0:5000/search_user'

        # Set the letter as a parameter
        search_params = {'q': letter_argument}

        # Send a POST request with the parameter
        response_object = requests.post(search_url, data=search_params)

        # Check if the response is JSON and not empty
        if response_object.headers.get('content-type') == 'application/json':
            if response_object.text:
                user_data = response_object.json()
                if 'id' in user_data and 'name' in user_data:
                    print("[{}] {}".format(user_data['id'], user_data['name']))
                else:
                    print("No matching result found")
            else:
                print("Response is empty")
        else:
            print("Response is not a valid JSON")

    except requests.exceptions.RequestException as request_error:
        # Handle any request-related errors
        print("Error:", request_error)


if __name__ == "__main__":
    # Check if an argument is provided, otherwise set letter=""
    letter_to_search = sys.argv[1] if len(sys.argv) > 1 else ""

    # Call the search_user_by_letter function with the letter argument
    search_user_by_letter(letter_to_search)
