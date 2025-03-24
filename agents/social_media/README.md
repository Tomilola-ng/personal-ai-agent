<!-- Social Media Agent -->

# Social Media Agent

The Social Media Agent is a one of the agents that Paia has access too, it's sole purpose is to manage your social media accounts.

## Features

| Feature                       | Description                                         | Status |
| ----------------------------- | --------------------------------------------------- | ------ |
| **Create Coontent Calendars** | Create a content calendar using OpenAI and Airtable | ✅     |
| **Post Tweets**               | Post tweets based on the content calendar           | ✅     |
| **Generate Images**           | Generate images for tweets                          | ✅     |
| **More to come**              | More to come                                        | ❌     |

<!-- How It Works -->

## How It Works

It uses OpenAI's GPT-4 model to generate content based on the prompts provided.
It seeds a Sheet on Airtable to store the content calendar.
Runs on a cron job to post tweets based on the content calendar.
Generates Image Prompts using DALL-E 2 to generate images for the tweets.

It uses the following tools:

- [X API](https://docs.x.com/home)
- [Airtable API](https://airtable.com/api)
- [OpenAI API](https://platform.openai.com/docs/overview)
- [DALL-E 2](https://platform.openai.com/docs/guides/image-generation)
