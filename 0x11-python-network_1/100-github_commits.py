#!/usr/bin/python3

"""
A script that:
- fetches the most recent 10 commits (from the most recent to oldest)
- of the repository specified by the user
- from the owner specified by the user
- using the GitHub API
- and prints all commits in the format: <sha>: <author name> (one per line)
"""

import sys
import requests


def fetch_recent_commits(owner_name_input: str, repo_name_input: str) -> list:
    """
    Fetches the 10 most recent commits from a GitHub repository.

    Args:
        owner_name_input (str): The owner (username or organization) of the repository.
        repo_name_input (str): The name of the repository.

    Returns:
        list: A list of commit information in the format "<sha>:
        <author name>".
    """
    try:
        # Define the GitHub API endpoint for commits
        commits_api_url = f"https://api.github.com/repos/{owner_name_input}/{repo_name_input}/commits"

        # Send a GET request to the GitHub API
        commits_response = requests.get(commits_api_url)

        # Check if the request was successful
        if commits_response.status_code == 200:
            commits_data = commits_response.json()
            commits_list = []

            # Iterate through commits until 10 commits are processed
            for commit in commits_data[:10]:
                commit_sha = commit["sha"]
                commit_author_name = commit["commit"]["author"]["name"]
                formatted_commit = f"{commit_sha}: {commit_author_name}"
                commits_list.append(formatted_commit)

            return commits_list
        else:
            print("Failed to fetch commits. Status code:", commits_response.status_code)
            return []
    except requests.exceptions.RequestException as request_error:
        # Handle any request-related errors
        print("Error:", request_error)
        return []


if __name__ == "__main__":
    # Parse command-line arguments
    repository_name_input = sys.argv[1]
    owner_name_input = sys.argv[2]

    # Fetch and print the commits
    commits_result = fetch_recent_commits(owner_name_input, repository_name_input)

    for commit in commits_result:
        print(commit)
