"""
    - Content Creator

    This agent is responsible for creating content for social media accounts.
    It uses OpenAI's GPT-4 model to generate content based on the prompts provided.
    It seeds a Sheet on Airtable to store the content calendar.
"""

import os
from datetime import datetime, timedelta
import json

from openai import OpenAI
from dotenv import load_dotenv
from pyairtable import Api as airtableApi
from pydantic import BaseModel, Field, ValidationError

from agents.social_media.schemas import TweetSheet, TweetFields
from agents.social_media.prompts import TweetPrompt

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
        print("Test Passed: Airtable API Key is working")
        print(tweets_table.all())
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


def seed_airtable_calendar(table_array):
    """
        Seed the Airtable calendar with the generated content.
        Expects a list of TweetFields objects.
    """
    print("=" * 20)
    print("Seeding Airtable Calendar")
    if not table_array:
        print("Table array is empty; nothing to seed.")
        raise ValueError("Table array is empty; nothing to seed.")

    # Prepare records for Airtable (convert TweetFields to dict)
    records = [
        {
            "Time": tweet.Time.value,
            "Status": tweet.Status.value,
            "Content": tweet.Content,
            "Day": tweet.Date
        }
        for tweet in table_array
    ]

    batch_size = 10
    for i in range(0, len(records), batch_size):
        batch = records[i:i + batch_size]
        tweets_table.batch_create(batch)
        print(
            f"Seeded {len(batch)} records into Airtable (batch {i // batch_size + 1})")

    print(f"Total records seeded: {len(records)}")


def generate_content():
    """
        Generate Content for Morning, Afternoon, and Evening posts.
        Returns a table array matching TweetSheet schema.
    """
    client = OpenAI()
    prompt = TweetPrompt()
    # chat = OpenAIClient().chat

    # print(chat(prompt.get_afternoon_prompt()))
    # return []

    # Define the response format for OpenAI
    class TweetResponse(BaseModel):
        """ Response format from OpenAI """
        start_date: str = Field(
            description="The date should allow this format type: %Y-%m-%d")
        content: list[str]

    table_array = []

    time_slots = [
        ("Morning", prompt.get_morning_prompt),
        ("Afternoon", prompt.get_afternoon_prompt),
        ("Evening", prompt.get_evening_prompt)
    ]

    print("=" * 20)
    print("Generating Content")
    for time, prompt_func in time_slots:
        print(f"Generating {time} content...")
        response = client.responses.parse(
            model="gpt-4o",
            input=prompt_func(),
            text_format=TweetResponse,
        )
        response_model = response.output[0].content[0].parsed

        start_date = response_model.start_date
        contents = response_model.content

        for i, content in enumerate(contents):
            date = (datetime.strptime(start_date, "%Y-%m-%d") +
                    timedelta(days=i)).strftime("%Y-%m-%d")
            table_array.append(
                TweetFields(
                    Time=time,
                    Status="Pending",
                    Content=content,
                    Date=date
                )
            )

    print("=" * 20)
    print("Table Array:")
    print(json.dumps([tweet.model_dump() for tweet in table_array], indent=2))
    return table_array
