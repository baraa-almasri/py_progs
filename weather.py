#!/usr/bin/python3

import requests
import json
from time import *

class Weather:

    # constructor
    def __init__(self, cityName: str):
        # set city name
        self.__cityName = cityName
        # weather json variables
        self.__weatherData = None

        self.__downloadWeatherData()

    def getWeather(self):
        
        while True:

            self.__updateWeatherVaraibles()

            print("City: %s\n" % self.__cityName)
            print("Real Temperature: %.1f°C" % self.__realTemp)
            print("Temperature: %.1f°C" % self.__temp)
            print("Status: %s" % self.__description)
            print("Wind Speed: %.1f km/h" % self.__windSpeed)
            print("Pressure: %d hPa" % self.__airPressure)
            print("Humidity: %.1f%%" % self.__humidity)
            print()
            print("Non weather data:")
            print("Sunrise: %s" % self.__sunrise)
            print("Sunset: %s" % self.__sunset)

            # refresh every 5 seconds
            sleep(5)
            # clear screen
            print('\033c')


    def __updateWeatherVaraibles(self):

        self.__downloadWeatherData()

        try:
            self.__temp = self.__weatherData['main']['temp'] - 273.15
            self.__description = self.__weatherData['weather'][0]['description']
            self.__windSpeed = self.__weatherData['wind']['speed'] * 3.6
            self.__airPressure = self.__weatherData['main']['pressure']
            self.__humidity = self.__weatherData['main']['humidity']
            self.__realTemp = self.__weatherData['main']['feels_like'] - 273.15
            self.__sunrise = ctime( self.__weatherData['sys']['sunrise'] )
            self.__sunset = ctime( self.__weatherData['sys']['sunset'] )

        except KeyError :
            print("No city found")
            exit(0)


    def __downloadWeatherData(self):
        # set url
        weatherUrl = "https://api.openweathermap.org/data/2.5/weather?q=" + self.__cityName + "&appid=2fb1078b1ae351cef587e0b7a1e479f0"
        # get weather data from the given url
        self.__weatherData = requests.get(weatherUrl).json()


if __name__ == "__main__":

    w = Weather("Damascus")
    w.getWeather()