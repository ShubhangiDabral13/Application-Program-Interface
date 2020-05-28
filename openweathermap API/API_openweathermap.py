# Python program to find current
# weather details of any city
# using openweathermap api

# import required modules
import urllib.request
import json
import pandas as pd

api_endpoint = "http://api.openweathermap.org/data/2.5/weather"

# Give city name
city = input("Enter the city whose weather you need to find out")

#Enter your API key here
apikey = "enter your api key"

# base_url variable to store url
url = api_endpoint + "?q=" + city + "&appid=" + apikey

#print the url
print(url)


response = urllib.request.urlopen(url).read()
parseresponse = json.loads(response)


detail = {}
detail["name_city"] = parseresponse["name"]
detail["temperature"] = (parseresponse['main']['temp'] - 273.15)
detail["weather"] = parseresponse['weather'][0]['description']

#converting dictionary to Series
df = pd.Series(detail)
print(df)

"""
Output for the day 19/04/2020

Input 1 :- Dehradun
Output 1:-name_city        Dehradun
          temperature        30.31
          weather        clear sky

Input 2 :- Delhi
Output 2:-name_city       Delhi
          temperature    31.57
          weather          haze

Input 3: - Chennai
Output 3:-name_city               Chennai
          temperature               33.28
          weather        scattered clouds          
"""
