import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def get_summary(news):
    # Retrieve your API key from the .env file
    llmkey = os.getenv("LLM_API_KEY")

    client = OpenAI(
        base_url="https://integrate.api.nvidia.com/v1",
        api_key=llmkey
    )

    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are writing a short daily news summary for Leo. "
                    "Write like a smart, direct person texting a friend — not a corporate assistant. "
                    "No 'Good morning', no sign-off, no fluff. "
                    "Just bullet points, one line each, plain English. "
                    "State the fact, add brief context if it actually matters. "
                    "Don't use words like 'significant', 'milestone', 'pivotal', or 'marking a major achievement'. "
                    "Don't editorialize. Just say what happened."
                )
            },
            {
                "role": "user", 
                "content": f"I need a concise briefing on the following report: {news}"
            }
        ],
        temperature=0.5, # Lowered slightly for more consistent, professional output
        top_p=1,
        max_tokens=1024,
        stream=False
    )

    return completion.choices[0].message.content

# Example usage:
