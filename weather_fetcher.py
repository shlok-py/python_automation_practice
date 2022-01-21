from urllib import response
from wsgiref.util import request_uri
import requests


#Get API_KEY from "https://home.openweathermap.org/api_keys"
API_KEY = "e48987b0eeeb7bd8a62a493115cffaa4"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city  = input("Enter the city of which you want to know the weather")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    for x,y in data:
        print(x, ":" , y)
else:
    print("An error occured")
