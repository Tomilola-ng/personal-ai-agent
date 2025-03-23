"""Main module for AI-agent."""

from agents.daily_post import DailyPostAgent


def main():
    """Main function for AI-agent."""
    daily_post_agent = DailyPostAgent()
    get_posts = daily_post_agent.generate_post()
    print(get_posts)


if __name__ == "__main__":
    main()
