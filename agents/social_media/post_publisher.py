""" Module for publishing posts on demand """

# pylint: disable=missing-timeout

import os
import uuid
import requests

from dotenv import load_dotenv
from requests_oauthlib import OAuth1

# Load environment variables
print("[Agent Report] Loading environment variables...")
load_dotenv()

# Constants
X_ENDPOINT = "https://api.twitter.com/2/tweets"
X_API_KEY = os.getenv("X_API_KEY")
X_API_KEY_SECRET = os.getenv("X_API_KEY_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")

# Validate environment variables
print("[Agent Report] Validating environment variables...")
if not all([X_API_KEY, X_API_KEY_SECRET, X_ACCESS_TOKEN, X_ACCESS_TOKEN_SECRET]):
    print("[Agent Report] Environment variable check failed.")
    raise ValueError(
        "One or more X authentication tokens are not set in the environment variables.")
print("[Agent Report] Environment variables validated successfully.")


class PostPublisher:
    """ Agent for publishing post."""

    def __init__(self):
        """Initializes the PostPublisher."""
        self.id = uuid.uuid4()
        print(f"[Agent Report] Initialized PostPublisher with ID: {self.id}")

    def post_on_twitter(self, post: str) -> str:
        """Posts the generated post on Twitter.

        Args:
            post (str): The generated post.
        """
        print("[Agent Report] Preparing payload for post...")
        payload = {
            "text": post,
            "for_super_followers_only": False,
        }

        print("[Agent Report] Setting up OAuth authentication...")
        auth = OAuth1(
            X_API_KEY,
            client_secret=X_API_KEY_SECRET,
            resource_owner_key=X_ACCESS_TOKEN,
            resource_owner_secret=X_ACCESS_TOKEN_SECRET
        )

        headers = {
            "Content-Type": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
        }

        print("[Agent Report] Sending post request to Twitter API...")
        response = requests.post(
            X_ENDPOINT, json=payload, headers=headers, auth=auth)

        print("=" * 20)
        print(response.json())
        print("=" * 20)

        print(
            f"[Agent Report] Response received with status code: {response.status_code}")

        if response.status_code != 201:
            print("[Agent Report] Post failed to publish.")
            return "500 Error"
        elif response.status_code == 401:
            print("[Agent Report] Unauthorized. Check credentials.")
            return "401 Unauthorized"
        else:
            print("[Agent Report] Post published successfully.")
            return "200 OK"
