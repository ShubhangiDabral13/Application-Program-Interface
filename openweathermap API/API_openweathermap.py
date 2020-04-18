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

# "404", means city not  found otherwise,
# city is been found
if parseresponse["code"] != "404":
    detail = {}
    detail["name_city"] = parseresponse["name"]
    detail["temperature"] = parseresponse['main']['temp']
    detail["weather"] = parseresponse['weather'][0]['description']

    #converting dictionary to Series
    df = pd.Series(detail)
    print(df)

else:
    print("City Not found")
