import requests

APIkey = '<enter your API key here>'
def get_data(place, days):
    URL = f'http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={APIkey}&units=metric'
    response = requests.get(URL)
    data = response.json()
    # API gets data every 3 hours, 8 records per day
    filtered_data = data['list'][:8*days]
    return filtered_data
