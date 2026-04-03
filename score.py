import requests
import json
import os 
from dotenv import load_dotenv
from datetime import date, timedelta
# https://site.api.espn.com/apis/site/v2/sports/soccer/{league}/scoreboard?dates=YYYYMMDD
yesterday = date.today() - timedelta(days=1)
formatted_date = yesterday.strftime("%Y%m%d")
def get_data(league, date):
  response = requests.get(f"https://site.api.espn.com/apis/site/v2/sports/soccer/{league}/scoreboard?dates={date}")
  data = response.json()
  if not data["events"]:
    return []
  results = []
  for event in data['events']:
    results.append({"home":event["competitions"][0]["competitors"][0]["team"]["displayName"], "home_score":event["competitions"][0]["competitors"][0]["score"], "away":event["competitions"][0]["competitors"][1]["team"]["displayName"], "away_score":event["competitions"][0]["competitors"][1]["score"]})

  else:
    return results
  
def get_scores():
  return get_data("eng.1", formatted_date)

  return get_data("esp.1", formatted_date)
  