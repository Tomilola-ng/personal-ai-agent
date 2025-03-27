"""Main module for AI-agent."""

from agents.social_media.manager import SocialMediaManager


MAX_RETRIES = 3


def main():
    """Main function for AI-agent."""
    print("Starting AI-agent...")
    smm_agent = SocialMediaManager()
    print(smm_agent.run())


if __name__ == "__main__":
    main()
