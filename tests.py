"""Tests for AI-agent."""

import os
import requests

from dotenv import load_dotenv
from requests_oauthlib import OAuth1
from utils.openai import OpenAIClient

from agents.social_media.content_creator import test as test_content_creator


# Load environment variables
load_dotenv()

# Constants
X_ENDPOINT = "https://api.twitter.com/2/tweets"
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
X_API_KEY = os.getenv("X_CLIENT_ID")
X_API_SECRET = os.getenv("X_CLIENT_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")


def test_main():
    """Test function for AI-agent."""
    # TODO: Add tests for AI-agent
    print("Testing AI-agent...")
    client = OpenAIClient()
    response = client.chat("Hello!")
    if response:
        print(response)
    print("---\n Done testing AI-agent. \n---")


def test_auth():
    """Test function for authentication."""
    url = "https://api.twitter.com/2/users/me"
    auth = OAuth1(
        X_API_KEY,
        client_secret=X_API_SECRET,
        resource_owner_key=X_ACCESS_TOKEN,
        resource_owner_secret=X_ACCESS_TOKEN_SECRET
    )
    response = requests.get(url, auth=auth)
    print(f"Test Status: {response.status_code}")
    print(f"Test Response: {response.text}")


if __name__ == "__main__":
    test_content_creator()
    # test_auth() BUG: Fix this
    test_main()
