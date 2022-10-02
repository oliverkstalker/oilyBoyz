#Learning how to use API'S
#use the "request" library as it allows you to access web databases and servers

#intended API'S to use
''' 
    This script pertains to the code written for the weather collection using the OpenWeatherMap API
    Link of API documentation: https://openweathermap.org/forecast5#name5
    
    Link of API CALL: https://api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key} 
'''

from os import waitid
import requests
import cgi
import CountryFunction

#function which converts degrees in celsius to degrees in farenheit
def Celsius_to_Fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

def Weather_Information(destination):
#1) Experimenting with the OpenWeatherApp API
#Link for API by city: "https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}"
    user_api = "9811532f09e0d432f872927e531e7223"
    city = destination.split(",")[0]
    country = destination.split(",")[1]
    country = country[1:]


#using the imported CountryFunction.py file to determine the proper country Code
    countryCode = CountryFunction.CountryCodeFunction(country)



#this is the complete api link including the inputted city location and the key
    complete_api_link = "https://api.openweathermap.org/data/2.5/forecast?q="+city+","+countryCode+"&appid="+user_api #this api link involves city and ISO 3166 CODE

#starting the API request
    weatherResponse = requests.get(complete_api_link)
    specifiedCityData = weatherResponse.json()



#checking if error is found in api call
    if specifiedCityData['cod'] == "404":
        print("Error: No existing location in Application")
#interpretting API call if no error is found
    else:
    #Path of the API always begin with the key ['list'], continuing path depends on desired output
    
    #determining temperature of inputted city(it follows the API key path ['list][0]['main]['temp])
        cityTemperatureCelsius = ((specifiedCityData['list'][0]['main']['temp']) - 273.15)
        cityTemperatureFahrenheit = Celsius_to_Fahrenheit(cityTemperatureCelsius)

    #finding current description of weather(it follows the API key path ['list']['weather'][0]['description']
        cityWeatherDescription = specifiedCityData['list'][0]['weather'][0]['description']
    


#returns of API returning the temperature and weather of inputted location
    return round(cityTemperatureFahrenheit) , cityWeatherDescription



