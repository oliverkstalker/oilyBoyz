from matplotlib.pyplot import text
import CountryFunction as cf
import WeatherAPI as wa
from flask import Flask, render_template, request,redirect,url_for

app = Flask(__name__)

'''destination = input("Enter in (city, country) format: ")
cityTemperature, cityWeather = wa.Weather_Information(destination)'''

@app.route('/')
def my_form():
    return render_template('my-form.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']
    processed_text = text
    value = processed_text
    cityTemperature, cityWeather = wa.Weather_Information(value)
    return ("It is "+str(cityTemperature)+" degrees and "+cityWeather+".")




    
#new for searches
if __name__ == "__main__":
    app.run()