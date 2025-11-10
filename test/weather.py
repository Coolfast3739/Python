import requests
import datetime as dt 
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "017d4904463a4fa7bbdc6c8f40767f84"
CITY = input("Enter city name: ")
URL = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(URL).json()
print(response)

input("Press Enter to exit...")