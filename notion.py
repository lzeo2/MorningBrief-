import requests
import os
from dotenv import load_dotenv
from datetime import date

load_dotenv()

def get_notion():
    date_rn = date.today()
    notion = os.getenv("NOTION_KEY")
    url = "https://api.notion.com/v1/databases/302b52c9881981a1add0e9835db85af1/query"
    headers = {
        "Authorization": f"Bearer {notion}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    payload = {
        "filter": {
            "property": "Date",
            "date": {"equals": str(date_rn)}
        }
    }
    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    results = []
    for item in data.get("results", []):
        status_obj = item["properties"].get("Status", {}).get("status", {})
        if status_obj.get("name") == "Done":
            continue
        results.append({
            "name": item["properties"]["Name"]["title"][0]["plain_text"],
            "subject": item["properties"]["Subject"]["select"]["name"],
            "Status": status_obj.get("name")
        })
    return results
