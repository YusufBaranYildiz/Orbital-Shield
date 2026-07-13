import datetime
import os
import requests

def fetch_neo_feed():
    """NASA NeoWs API'sinden güncel yakın geçiş verisini çeker."""
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    
    # Bugünün tarihini başlangıç yapalım
    start_date = datetime.date.today()
    # 7 gün sonrasını bitiş yapalım (API maksimum 7 günlük aralığı destekler)
    end_date = start_date + datetime.timedelta(days=7)
    
    api_key = os.environ.get("NASA_API_KEY", "DEMO_KEY")
    
    params = {
        "start_date": start_date.strftime("%Y-%m-%d"),
        "end_date": end_date.strftime("%Y-%m-%d"),
        "api_key": api_key
    }
    
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()

