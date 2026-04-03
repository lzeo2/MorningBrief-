import os 
import resend 
from weather import get_weather
from news import get_news
from notion import get_notion
from dotenv import load_dotenv
from score import get_scores
from summariser import get_summary

load_dotenv()
resend.api_key = os.environ["RESEND_API_KEY"]

# Data Retrieval
news = get_news()
weather = get_weather()
deadlines = get_notion()

scores = get_scores()

summaryai = get_summary(news)

def email_sender(weather, news, deadlines, scores):
    # Professional dark-mode dashboard styling
    html_content = f"""
    <div style="font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; background-color: #121212; padding: 40px 10px;">
        <div style="max-width: 600px; margin: auto; background-color: #1e1e1e; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            
            <div style="background: linear-gradient(135deg, #2c3e50, #000000); padding: 30px; text-align: left; border-bottom: 1px solid #333;">
                <h1 style="margin: 0; color: #ffffff; font-size: 26px; font-weight: 700;">Good Morning, Leo</h1>
                <p style="margin: 5px 0 0 0; color: #aaa; font-size: 14px;">Your Executive Briefing</p>
            </div>
            
            <div style="padding: 30px;">
                
                <div style="background-color: #252525; padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 4px solid #00d2ff;">
                    <h2 style="color: #00d2ff; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 10px 0;">🌤 Local Forecast</h2>
                    <p style="color: #eee; margin: 0; font-size: 16px;">
                        Currently <b>{weather['temp']}°C</b> with {weather['humidity']}% humidity.
                        <span style="color: #888; font-size: 13px;">UV Index: {weather['uv']}</span>
                    </p>
                </div>
                
                <div style="background-color: #252525; padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 4px solid #bb86fc;">
                    <h2 style="color: #bb86fc; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 10px 0;">📰 Intelligence Summary</h2>
                    <div style="color: #ddd; font-size: 15px; line-height: 1.6;">{summaryai}</div>
                </div>

                <div style="background-color: #252525; padding: 20px; border-radius: 10px; margin-bottom: 25px; border-left: 4px solid #03dac6;">
                    <h2 style="color: #03dac6; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 10px 0;">🏆 Sports Update</h2>
                    <p style="color: #eee; margin: 0; font-size: 15px; line-height: 1.8;">
                        {"".join([f"<b>{s['home']}</b> {s['home_score']} — {s['away_score']} <b>{s['away']}</b><br>" for s in scores])
                        if scores else "Nothing to see here.. no matches played"}
                    </p>
                </div>
                
                <div style="background-color: #252525; padding: 20px; border-radius: 10px; border-left: 4px solid #cf6679;">
                    <h2 style="color: #cf6679; font-size: 14px; text-transform: uppercase; letter-spacing: 1px; margin: 0 0 10px 0;">⏳Deadlines</h2>
                    <p style="color: #eee; margin: 0; font-size: 15px; line-height: 1.8;">
                        {"".join([f"• {d['name']} <span style='color: #888;'>({d['subject']})</span><br>" for d in deadlines])}
                    </p>
                </div>

            </div>
            
            <div style="padding: 20px; text-align: center; border-top: 1px solid #333; color: #555; font-size: 11px;">
                <p style="margin: 0;">Automated for Leo | Briefing Service v2.0</p>
            </div>
        </div>
    </div>
    """

    params: resend.Emails.SendParams = {
        "from": "Assistant <onboarding@resend.dev>",
        "to": ["pengpengjin1@gmail.com"],
        "subject": f"Leo's Daily Briefing",
        "html": html_content,
    }

    try:
        email = resend.Emails.send(params)
        print("Success: Briefing sent to Leo.")
    except Exception as e:
        print(f"Error: {e}")

email_sender(weather, news, deadlines, scores)
