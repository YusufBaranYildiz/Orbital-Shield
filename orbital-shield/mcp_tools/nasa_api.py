import requests

def fetch_neo_feed():
    """NASA NeoWs API'sinden son 7 günlük yakın geçiş verisini çeker."""
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {"api_key": "DEMO_KEY"}
    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
