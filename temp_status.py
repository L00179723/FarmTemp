## Temperature status

from source_temp.directory_utilities import log_temperature


if __name__ == "__main__":
   
    sensor_id = 1

    temperature = log_temperature(1)

        # Actions based on the temperature value
if temperature > 30:
    print("High temperature! Attention need!")
elif temperature < -3:
    print("Low temperature! Check area!")            
else:
    print("Failed to measure")
