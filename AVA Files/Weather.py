import requests
import AssistantSpeak as ASpeak

#Speaks out the weather of a city(Input)
def weatherreport(City):
    #Url Components 
    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
    City = City.capitalize()
    API_KEY = "ab0d5e80e8dafb2cb81fa9e82431c1fa"

    # Joining the Url components to makeup a URL
    # '&units=metrics' converts the temperature from kelvin to celcius
    URL = BASE_URL + "q=" + City + "&appid=" + API_KEY + "&units=metric"

    response = requests.get(URL)

    if response.status_code == 200:
        data = response.json()
        main = data['main']

        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']

        report = data['weather']
        print("\n" + City.capitalize())
        
        #print(f"Temperature: {temperature}")
        ASpeak.speak(f"Temperature: {temperature}")

        #print(f"Humidity: {humidity}")
        ASpeak.speak((f"Humidity: {humidity}"))

        #print(f"Pressure: {pressure}")
        ASpeak.speak(f"Pressure: {pressure}")

        #print(f"Weather : {report[0]['description']}")
        ASpeak.speak(f"Weather : {report[0]['description']}")
    else:
        # showing the error message
        #print("Error in the HTTP request")
        ASpeak.print("Error in the HTTP request")
