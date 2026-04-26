# Morning Briefing

An automated daily briefing service that compiles weather, news, sports scores, and task deadlines into a beautifully formatted email.

## Features

- **Weather**: Current temperature, humidity, and UV index for Canberra
- **News**: Top headlines from ABC News Australia with AI-generated summaries
- **Sports**: Latest scores from Premier League and La Liga
- **Deadlines**: Tasks due today from Notion database
- **Delivery**: Professional dark-mode HTML email sent daily

## Prerequisites

- Python 3.11+
- GitHub account (for Actions workflow)
- API keys for:
  - [Resend](https://resend.com) (email delivery)
  - [NewsAPI](https://newsapi.org) (news headlines)
  - [WeatherAPI](https://www.weatherapi.com) (weather data)
  - [Notion](https://www.notion.so) (task integration)
  - [NVIDIA AI](https://www.nvidia.com/en-us/ai/) (Llama 3.1 for summarization)

## Setup

### 1. Clone the Repository

```bash
git clone <repository-url>
cd MorningBriefingReview
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Create a `.env` file in the project root:

```env
RESEND_API_KEY=re_xxxxxxxxxxxxxxxxxxxxxxxxxx
NEWS_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
NOTION_KEY=secret_xxxxxxxxxxxxxxxxxxxxxxxx
LLM_API_KEY=nvapi-xxxxxxxxxxxxxxxxxxxxxxxx
WEATHER_KEY=xxxxxxxxxxxxxxxxxxxxxxxx
RECIPIENT_EMAIL=your-email@example.com
```

### 4. Set Up Notion Database

Create a Notion database with:
- **Name** (Title)
- **Subject** (Select)
- **Status** (Status: To-do, In progress, Done)
- **Date** (Date)

Get the database ID from the URL and update it in `notion.py`.

## Usage

### Run Locally

```bash
python gmail.py
```

### GitHub Actions (Recommended)

The included workflow runs automatically at 7:00 AM AEST daily. To enable:

1. Go to repository **Settings** → **Secrets and variables** → **Actions**
2. Add all required secrets:
   - `RESEND_API_KEY`
   - `NEWS_KEY`
   - `NOTION_KEY`
   - `LLM_API_KEY`
   - `WEATHER_KEY`
3. The workflow will run on schedule or trigger manually via **Actions** tab

## Project Structure

```
.
├── .github/
│   └── workflows/
│       └── morning_brief.yml    # GitHub Actions automation
├── gmail.py                      # Main entry point & email composition
├── news.py                       # News API integration
├── notion.py                     # Notion API integration
├── score.py                      # ESPN sports scores
├── summariser.py                 # NVIDIA LLM summarization
├── weather.py                    # Weather API integration
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## Configuration

### Customizing the Schedule

Edit `.github/workflows/morning_brief.yml`:

```yaml
on:
  schedule:
    - cron: '00 21 * * *'  # 7AM AEST (21:00 UTC previous day)
```

### Changing Location

Update the location in `weather.py`:

```python
api_url = f"https://api.weatherapi.com/v1/current.json?key={weathers}&q=YourCity"
```

### Modifying News Sources

Update the news source in `news.py`:

```python
api_url = f"https://newsapi.org/v2/top-headlines?sources=your-preferred-source&pageSize=5&apiKey={news}"
```

## Dependencies

- `requests` - HTTP requests for APIs
- `openai` - NVIDIA LLM API client, plug and play with BYOK
- `resend` - Email delivery service
- `python-dotenv` - Environment variable management

## Troubleshooting

### Email not sending
- Verify Resend API key is valid and email is verified in Resend dashboard
- Check that recipient email is on Resend's allowed list

### News API errors
- Free tier has 100 requests/day limit
- Ensure API key is active

### Notion integration fails
- Verify database ID is correct
- Ensure integration has database access
- Check database property names match exactly

### Weather data unavailable
- Free tier includes 1 million calls/month
- Verify API key is active

## License

[License information]

## Contributing

Contributions welcome. Please ensure:
- Code follows PEP 8 style
- Functions include docstrings
- Changes are tested locally before submitting
