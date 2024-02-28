# temperature_client.py
import socket
from w1thermsensor import W1ThermSensor
import time

def get_temperature(sensor_id=1):
    sensor = W1ThermSensor(sensor_id)
    return sensor.get_temperature()

def send_temperature(host, port, sensor_id=2):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

  
if __name__ == "__main__":
    server_host = "localhost"
    server_port = 5555
    client_sensor_id = 2

    send_temperature(server_host, server_port, client_sensor_id)
