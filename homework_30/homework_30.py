import random
import requests
import json
from pprint import pprint
# 1
websites = [
    "google.com",
    "facebook.com",
    "twitter.com",
    "amazon.com",
    "apple.com"
]


random_website = random.choice(websites)
response = requests.get(f"http://{random_website}")
status_code = response.status_code
website_name = random_website
html_length = len(response.text)

print("Статус-код:", status_code)
print("Назва сайту:", website_name)
print("Довжина HTML-коду:", html_length)

#2


city = input("Enter your city:")
weather = f'https://geocoding-api.open-meteo.com/v1/search?name={city}'
res = requests.get(weather).json()
result = res['results'][0]
geo = dict()
lat = geo['latitude'] = result['latitude']
lng = geo['longitude'] = result['longitude']
req = requests.get(f'https://api.open-meteo.com/v1/forecast?latitude={lat}&timezone=Europe%2FBerlin&longitude={lng}&current_weather=true')
pprint(req.json())