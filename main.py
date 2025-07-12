
import schedule
import time
import requests
from datetime import datetime

BOT_TOKEN = "your_token_here"
CHAT_ID = "your_chat_id_here"

def send_message(text):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": text,
        "parse_mode": "Markdown"
    }
    requests.post(url, data=payload)

def job():
    today = datetime.now().strftime('%A')
    content = {
        "Monday": "🎥 *Who are Crime Mob?*\n\nMore than just *Knuck If You Buck*. They were pioneers in Crunk with female MCs. Princess is a legend – and I got a track with her coming.",
        "Tuesday": "🎧 *New Teaser: CRUNK IS STILL ALIVE*\n\nSingle with Don P from Trillville drops soon. Stay tuned.",
        "Wednesday": "🎨 *Artwork Drop*\n\nJust dropped a new cover for Zaytoven & E-40 collab. Honored to be part of it.",
        "Thursday": "🎤 *Track Story*\n\nHere’s how I made a song with YoungBloodz. One message. One idea. One collab.",
        "Friday": "🧠 *Did you know?*\n\nCrunk didn’t start with Lil Jon. It started in Memphis with DJ Spanish Fly in 1991.",
        "Saturday": "🔁 *Shoutout Saturday*\n\nOGs reacting to my work. Respect from legends.",
        "Sunday": "👑 *CRUNK STILL LIVES*\n\nI’m from Poland. I make music with OGs from Atlanta. Crunk is alive – and you’ll feel it."
    }
    message = content.get(today, "Stay Crunk.")
    send_message(message)

schedule.every().day.at("05:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(60)
