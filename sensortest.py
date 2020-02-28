#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import Adafruit_DHT
import requests
import json

pin = 4
sensor = Adafruit_DHT.DHT11
apikey = "XXXXXXXXXXXXXXXXXXXXX" # Replace with apikey

# Enable pull up
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        print("%s°C %s%%" % (temperature, humidity))
        data = {"temperature": temperature, "humidity": humidity}
        r = requests.post('http://palamoa.de/json/' + apikey, data=json.dumps(data))
        if r.status_code != 200:
            print(r)
        time.sleep(60) # Limit of Palamoa
    except Exception as e:
        print("error", e)
        time.sleep(1)
