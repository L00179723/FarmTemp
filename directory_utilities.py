"""
directory_utilities.py
By: Suzanne Freitas
Date: 19NOV23
"""
# directory_utilities.py

from w1thermsensor import W1ThermSensor
import time
import datetime
import os

def measure_temperature(sensor_id=1):
        
    try:
        sensor = W1ThermSensor(sensor_id)
        temperature = sensor.get_temperature(1)
        return temperature
    
    except Exception as e:
        print(f"Error: {e}")
        return None

def log_temperature(temperature, log_file="temp_status.txt"):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    log_entry = f"{timestamp} - Temperature: {temperature:.2f} °C\n"

    try:
        with open(log_file, "a") as file:
            file.write(log_entry)
        print("Temperature logged successfully.")
    except Exception as e:
        print(f"Error logging temperature: {e}")

if __name__ == "__main__":
   
    sensor_id = 1

    temperature = measure_temperature(1)

    if temperature is not None:
        log_temperature(temperature)
        
        if temperature > 30:
            print("High temperature! Attention need!.")
        elif temperature < 10:
            print("Low temperature! Check area!.")
            
        else:
            print("Failed to measure temperature.")
