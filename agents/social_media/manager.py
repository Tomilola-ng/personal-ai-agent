""" 
    Module for managing social media agents.
    - It assigns the content calendar generator on a monthly basis.
    - It assigns the daily post agent on a daily basis.
    - It validates the posts going out on social media.
"""

import os
import uuid
from datetime import datetime
from dotenv import load_dotenv
from pyairtable import Api as airtableApi
from agents.social_media.content_creator import generate_content, seed_airtable_calendar
from agents.social_media.post_publisher import PostPublisher

print("[Agent Report] Initializing Social Media Manager Agent...")

# Load environment variables
print("[Agent Report] Loading environment variables...")
load_dotenv()

# Constants
AIRTABLE_API_KEY = os.getenv("AIRTABLE_API_KEY")
AIRTABLE_BASE_ID = os.getenv("AIRTABLE_BASE_ID")
AIRTABLE_TABLE_NAME = os.getenv("AIRTABLE_TABLE_NAME")

print("[Agent Report] Validating Airtable authentication tokens...")
if not all([AIRTABLE_API_KEY, AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME]):
    print("[Agent Report] Error: Missing Airtable authentication tokens!")
    raise ValueError(
        "One or more Airtable authentication tokens are not set in the environment variables.")
print("[Agent Report] Airtable authentication successful.")

# Airtable Table Initialization
print("[Agent Report] Establishing Airtable connection...")
airtable = airtableApi(AIRTABLE_API_KEY)
tweets_table = airtable.table(AIRTABLE_BASE_ID, AIRTABLE_TABLE_NAME)
print("[Agent Report] Airtable connection established.")


class SocialMediaManager:
    """ Agent for managing social media. """

    def __init__(self):
        """Initializes the SocialMediaManager."""
        self.id = uuid.uuid4()
        print(
            f"[Agent Report] Social Media Manager initialized with ID: {self.id}")

    def get_today_content(self):
        """Checks if the content is available for the current date."""
        print("[Agent Report] Checking for today's scheduled content...")
        if not tweets_table.all():
            print("[Agent Report] No content found in the table.")
            return None
        tt_sheet = tweets_table.all()
        today = datetime.strftime(datetime.now(), "%Y-%m-%d")
        for tweet in tt_sheet:
            if tweet["fields"]["Day"] == today:
                if tweet["fields"]["Time"] == self.time_of_day():
                    print(
                        f"[Agent Report] Found content scheduled for {today} during {self.time_of_day()}.")
                    return tweet
        print("[Agent Report] No content scheduled for the current time slot.")
        return None

    def change_status(self, tweet_id):
        """Changes the status of the tweet. """
        print(
            f"[Agent Report] Updating status of tweet ID {tweet_id} to 'Posted'...")
        tweets_table.update(tweet_id, {"Status": "Posted"})
        print("[Agent Report] Status update complete.")
        return True

    def time_of_day(self):
        """Returns the time of day. """
        now = datetime.now()
        hour = now.hour
        if hour < 12:
            return "Morning"
        elif hour < 18:
            return "Afternoon"
        else:
            return "Evening"

    def assign_content_calendar_generator(self):
        """Assigns the content calendar generator on a monthly basis."""
        print("[Agent Report] Generating monthly content calendar...")
        generated_content = generate_content()
        print("[Agent Report] Seeding generated content to Airtable...")
        seed_airtable_calendar(generated_content)
        print(
            "[Agent Report] Monthly content calendar successfully generated and saved.")
        return True

    def assign_daily_post_agent(self):
        """Assigns the daily post agent on a daily basis."""
        print("[Agent Report] Initializing post publisher agent...")
        post_publisher = PostPublisher()
        content = self.get_today_content()

        if not content:
            print("[Agent Report] No content to publish. Aborting post process.")
            return False

        print("[Agent Report] Publishing content to social platform...")
        post_publisher.post_on_twitter(content["fields"]["Content"])
        print("[Agent Report] Content published successfully.")

        self.change_status(content["id"])
        print("[Agent Report] Content status updated to 'Posted'.")
        return True

    def validate_posts(self):
        """Validates the posts going out on social media."""
        print("[Agent Report] Validating scheduled posts for today...")
        today_content = self.get_today_content()
        if today_content:
            if today_content["fields"]["Status"] == "Pending":
                print("[Agent Report] Valid pending post found.")
                return True
        print("[Agent Report] No valid pending posts found.")
        return False

    def run(self):
        """Runs the SocialMediaManager."""
        print("[Agent Report] Social Media Manager agent execution started...")
        if self.validate_posts():
            print("[Agent Report] Valid content confirmed. Proceeding to publish...")
            self.assign_daily_post_agent()
            print("[Agent Report] Content publishing routine completed successfully.")
        else:
            print("[Agent Report] No content ready for publishing. Standing by.")
