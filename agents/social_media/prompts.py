"""
    - Prompts
"""

import uuid
from datetime import datetime


class TweetPrompt:
    """Prompt for generating a tweets calendar."""

    def __init__(self):
        """
            Initialize the TweetPrompt class.
        """
        self.id = str(uuid.uuid4())

    def get_today(self):
        """ Returns today's date """
        today = datetime.now()
        date_context = f"Today's date is {today.strftime('%A, %B %d, %Y')}."
        return date_context

    def get_morning_prompt(self, previous_tweets="", knowledge_base=""):
        """ Morning """
        return f"""
            You are an AI assistant creating a monthly Twitter content calendar for my Morning posts (1 tweet per day). Here’s the context:

            Constraints:
                - 280 character limit
                - Must provide clear value or insight
                - Avoid sales pitches
                - Use compelling, professional language

            - {self.get_today}
            - **My Bio**: "AI Agent Developer - Building AI systems that automate processes, streamline operations and implement solutions that scale (with) your business; Software Engineer - I provide AI Agent Development, Fullstack Web Development | Mobile App Development Services | ( ALX & HNG Alumni )"
            
            - **Theme**: Positive affirmations, good morning greetings, trendy reposts (AI/tech), opinions, predictions, or peaceful messages, tips, productivity hacks, or tool recommendations.
            - **Tone**: Uplifting, engaging, thought-provoking.
            - **Repetition Rule**: Do not repeat ideas, phrases, or synonyms of prior posts. If I provide a list of previous tweets, ensure new ones differ significantly.
            - **Blanks**: Leave 3 posts per week blank (e.g., 12 blanks over 4 weeks) marked as "[User Input]" for me to fill in.

            **Previous Tweets (if any)**: {previous_tweets}
            **Knowledge base (if any)**: {knowledge_base}
            **Task**: Generate Morning posts for the rest of the month. {self.get_today()} Avoid repeating ideas from the Previous Tweets list.
        """

    def get_afternoon_prompt(self, previous_tweets="", knowledge_base=""):
        """ Afternoon """
        return f"""
            You are an AI assistant creating a monthly Twitter content calendar for my Afternoon posts (1 tweet per day). Here’s the context:

            Constraints:
                - 280 character limit
                - Must provide clear value or insight
                - Avoid sales pitches
                - Use compelling, professional language

            - {self.get_today}
            - **My Bio**: "AI Agent Developer - Building AI systems that automate processes, streamline operations and implement solutions that scale (with) your business; Software Engineer - I provide AI Agent Development, Fullstack Web Development | Mobile App Development Services | ( ALX & HNG Alumni )"
            - **Theme**: Business-focused—case studies, user reviews, benefits of my services, why clients choose me, or my services (AI Agent Dev, Fullstack Web Dev, Mobile App Dev), the results I delivered for my clients, and the impact I had on their businesses, actual numerical/countable impacts e.g "100% increase in revenue" or "50% reduction in costs".
            - **Tone**: Professional, value-driven, expertise-focused.
            - **Repetition Rule**: Do not repeat ideas, phrases, or synonyms of prior posts. Use the Previous Tweets list to ensure variety.
            - **Blanks**: Leave 3 posts per week blank (e.g., 12 blanks over 4 weeks) marked as "[User Input]" for me to fill in.

            **Previous Tweets (if any)**: {previous_tweets}
            **Knowledge base (if any)**: {knowledge_base}
            **Task**: Generate Afternoon posts for the rest of the month. {self.get_today()} Avoid repeating ideas from the Previous Tweets list.
        """

    def get_evening_prompt(self, previous_tweets="", knowledge_base=""):
        """ Evening """
        return f"""
            You are an AI assistant creating a monthly Twitter content calendar for my Evening posts (1 tweet per day). Here’s the context:

            Constraints:
                - 280 character limit
                - Must provide clear value or insight
                - Avoid sales pitches
                - Use compelling, professional language

            - {self.get_today}
            - **My Bio**: "AI Agent Developer - Building AI systems that automate processes, streamline operations and implement solutions that scale (with) your business; Software Engineer - I provide AI Agent Development, Fullstack Web Development | Mobile App Development Services | ( ALX & HNG Alumni )"
            **Theme**: Lead conversion—how to reach me, calls-to-action (CTAs), nudging leads to clients, use results of past work to nudge, use FOMO to nudge, Plead sometimes, promise excellence, and use the results of past work to nudge.
            - **Tone**: Direct, actionable, friendly.
            - **Repetition Rule**: Do not repeat ideas, phrases, or synonyms of prior posts. Use the Previous Tweets list to ensure variety.
            - **Blanks**: Leave 3 posts per week blank (e.g., 12 blanks over 4 weeks) marked as "[User Input]" for me to fill in.

            **Previous Tweets (if any)**: {previous_tweets}
            **Knowledge base (if any)**: {knowledge_base}
            **Task**: Generate Evening posts for the rest of the month. {self.get_today()} Avoid repeating ideas from the Previous Tweets list.
        """
