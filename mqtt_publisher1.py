import paho.mqtt.client as mqtt
import time
import requests
def getCurrentTemp():
    api_key = "c008cf246556a06a03c197b39b088b1a"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    city_name = "Ribeirão Preto"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name + "&units=metric"
    response = requests.get(complete_url)
    x = response.json()

    if x["cod"] != "404":
        y = x["main"]

        current_temperature = y["temp"]

        return current_temperature

    else:
        return "error"


mqttBroker = "192.168.0.39"
client = mqtt.Client("Ribeirao_Temperature")
client.connect(mqttBroker)

while True:
    current_temp = getCurrentTemp()
    client.publish("RIBEIRAO_TEMPERATURE", current_temp)
    print("Just published "+ str(current_temp) + " to Topic RIBEIRAO_TEMPERATURE")
    time.sleep(10)