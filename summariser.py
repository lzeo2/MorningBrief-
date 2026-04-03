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
                    "You are Leo's professional Executive Assistant. Your task is to provide "
                    "high-level, efficient news briefings. Your tone should be formal, "
                    "intelligent, and direct. Start each briefing by addressing Leo, "
                    "then provide the key facts without any unnecessary fluff."
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
