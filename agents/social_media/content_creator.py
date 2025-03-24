"""
    - Content Creator

    This agent is responsible for creating content for social media accounts.
    It uses OpenAI's GPT-4 model to generate content based on the prompts provided.
    It seeds a Sheet on Airtable to store the content calendar.
"""

import os

from dotenv import load_dotenv
from pyairtable import Api as airtableApi
from pydantic import ValidationError

from utils.openai import OpenAIClient
from agents.social_media.schemas import TweetSheet

# Load environment variables
load_dotenv()


# Constants
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

if not all([AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME]):
    raise ValueError(
        "One or more Airtable authentication tokens are not set in the environment variables.")

# Airtable Table Initialization
airtable = airtableApi(AIRTABLE_API_KEY)
tweets_table = airtable.table(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)


def test():
    """
        Test Function
    """
    print("=" * 20)
    print("Testing If The Airtable API Key Is Working")
    if tweets_table.all():
        print("Test Passed")
    print("=" * 20)
    print("Testing If The content matches the schema")
    try:
        for tweet in tweets_table.all():
            TweetSheet(**tweet)
        print("Test Passed")
    except ValidationError as e:
        print(e)
        print("Test Failed")
        print("=" * 20)


def generate_content():
    """
        Generate Content
    """
    openai = OpenAIClient()
    system_prompt = """
        You are a content creator for a social media account.
        Your task is to create content for the account.
        You must follow the following guidelines:
        - Use a conversational tone.
        - Be concise and to the point.
        - Use emojis to express emotions.
        - Use hashtags to categorize the content.
        """
    # content = openai.chat()
