#!/usr/bin/python3
import urllib.request
import urllib.parse
import sys

def post_email(url, email):
    """
    Sends a POST request to the given URL with the email as a parameter and displays the response body.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email to include in the request.

    Returns:
        str: The decoded content of the response.
    """
    try:
        data = urllib.parse.urlencode({'email': email}).encode('utf-8')
        with urllib.request.urlopen(url, data=data) as response:
            content = response.read().decode('utf-8')
            return content
    except urllib.error.URLError as e:
        return f"Error sending POST request: {e}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url_to_post = sys.argv[1]
    email_to_send = sys.argv[2]

    response_content = post_email(url_to_post, email_to_send)

    print(response_content)
