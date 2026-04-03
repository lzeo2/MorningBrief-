import requests
import os 
from dotenv import load_dotenv
load_dotenv()

news = os.getenv("NEWS_KEY")
api_url = f"https://newsapi.org/v2/top-headlines?sources=abc-news-au&pageSize=5&apiKey={news}"



def get_news():
    response = requests.get(api_url)
    data = response.json()
    
    # Grab the 'articles' list and slice the first 5
    top_five = data["articles"][:5]
    
    results = []
    for i in range(len(top_five)):
        results.append(f"{i+1}. {top_five[i]['title']}")
        
    return results
print(get_news())