"""Tests for AI-agent."""

import os

from dotenv import load_dotenv
from utils.openai import OpenAIClient


# Load environment variables
load_dotenv()

# Constants
X_ENDPOINT = "https://api.twitter.com/2/tweets"
X_BEARER_TOKEN = os.getenv("X_BEARER_TOKEN")
X_API_KEY = os.getenv("X_CLIENT_ID")
X_API_KEY_SECRET = os.getenv("X_API_KEY_SECRET")
X_API_SECRET = os.getenv("X_CLIENT_SECRET")
X_ACCESS_TOKEN = os.getenv("X_ACCESS_TOKEN")
X_ACCESS_TOKEN_SECRET = os.getenv("X_ACCESS_TOKEN_SECRET")


def test_main():
    """Test function for AI-agent."""
    print("Testing AI-agent...")
    client = OpenAIClient()
    response = client.chat("Hello!")
    if response:
        print(response)
    print("---\n Done testing AI-agent. \n---")


if __name__ == "__main__":
    test_main()
