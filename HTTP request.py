#!/usr/bin/python3

import requests
import json
from time import *

# weather city
cityName = input("Enter city name: ")

while True:
    
    # create a json weather file
    weatherFile = open("weather.json", "w")

    weatherUrl = "https://api.openweathermap.org/data/2.5/weather?q=" + cityName + "&appid=2fb1078b1ae351cef587e0b7a1e479f0"

    rawWeatherData = requests.get(weatherUrl).json()

    json.dump(rawWeatherData, weatherFile, indent= 4)

    # reopen file in reading mode
    weatherFile.close()
    weatherFile = open("weather.json", "r")

    weatherData = json.load(weatherFile)


    
    try:
        temp = weatherData['main']['temp'] - 273.15
        description = weatherData['weather'][0]['description']
        windSpeed = weatherData['wind']['speed'] * 3.6
        airPressure = weatherData['main']['pressure']
        humidity = weatherData['main']['humidity']
        realTemp = weatherData['main']['feels_like'] - 273.15
        sunrise = ctime( weatherData['sys']['sunrise'] )
        sunset = ctime( weatherData['sys']['sunset'] )

    except KeyError :
        print("No city found")
        exit(0)



    print("Real Temperature: %.1f°C" % realTemp)
    print("Temperature: %.1f°C" % temp)
    print("Status: %s" % description)
    print("Wind Speed: %.1f km/h" % windSpeed)
    print("Pressure: %d hPa" % airPressure)
    print("Humidity: %.1f%%" % humidity)
    print()
    print("Non weather data:")
    print("Sunrise: %s" % sunrise)
    print("Sunset: %s" % sunset)

    sleep(1)
    print('\033c')

