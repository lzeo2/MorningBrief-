import requests
import json
import os 
from dotenv import load_dotenv
from datetime import date
load_dotenv()

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
    "date": {
      "equals": f"{date_rn}"
    }
  }
}
response = requests.post(url, headers=headers, json = payload)

data = response.json()
def get_notion():
    undonelist = []
    for item in data.get("results", []):
        status_obj = item["properties"].get("Status", {}).get("status", {})
        status_name = status_obj.get("name")

        if status_name == "Done":
            continue 
        else:
            undonelist.append(item)
    results = []
    for thing in undonelist:
        results.append({"name":thing["properties"]["Name"]["title"][0]["plain_text"],"subject":thing["properties"]["Subject"]["select"]["name"], "Status" : thing["properties"]["Status"]["status"]["name"]})
    return results

get_notion()
