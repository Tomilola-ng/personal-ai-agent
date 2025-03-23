"""Main module for AI-agent."""

from agents.daily_post import DailyPostAgent


MAX_RETRIES = 3

def main():
    """Main function for AI-agent."""
    print("Starting AI-agent...")
    count = 0

    print("Generating daily post...")
    daily_post_agent = DailyPostAgent()
    get_posts = daily_post_agent.generate_post()
    # Checks if the post is too long and generates a new one when under 3 retries
    while len(get_posts) > 280:
        count += 1
        if count > MAX_RETRIES:
            raise ValueError("Post is too long, cannot post on twitter.")
        get_posts = daily_post_agent.generate_post()
        print(f"Post is too long, generating new post: {get_posts}, retrying... {count}/{MAX_RETRIES}")
    # Makes a post on twitter
    print(f"Post generated: {get_posts}")
    print("Posting on Twitter...")
    daily_post_agent.post_on_twitter(get_posts)
    print("Post successfully posted on Twitter.")
    print("AI-agent completed.")

if __name__ == "__main__":
    main()
