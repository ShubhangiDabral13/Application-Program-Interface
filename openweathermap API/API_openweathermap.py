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
apikey = "8fadb93a7fca0bc168267f9af1777762"

# base_url variable to store url
url = api_endpoint + "?q=" + city + "&appid=" + apikey

#print the url
print(url)

response = urllib.request.urlopen(url).read()
parseresponse = json.loads(response)


detail = {}
detail["name_city"] = parseresponse["name"]
detail["temperature"] = parseresponse['main']['temp']
detail["weather"] = parseresponse['weather'][0]['description']

#converting dictionary to Series
df = pd.Series(detail)
print(df)

"""
Input 1 :- Dehradun
Output 1:-name_city        Dehradun
          temperature        293.57
          weather        light rain

Input 2 :- Delhi
Output 2:-name_city       Delhi
          temperature    303.42
          weather          haze
"""          
