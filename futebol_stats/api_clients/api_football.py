import requests
from datetime import datetime

API_KEY = 'SUA_API_KEY'
BASE_URL = 'https://v3.football.api-sports.io'

HEADERS = {
    'x-apisports-key': '79814fec0b2853b54158d8de3d06ca9b'

}

def get_matches_today():
    date = datetime.now().strftime('%Y-%m-%d')
    url = f'{BASE_URL}/fixtures?date={date}'
    response = requests.get(url, headers=HEADERS)
    return response.json()
