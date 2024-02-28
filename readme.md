# System Temperature Monitor

# Farm Project Temperature Monitoring Overview

This project is developed to monitor temperature using a Raspberry Pi 4B and wired temperature sensor (W1ThermSensor).
Three UDP clients structure the system, which transmits temperature values to a server that tracks the information. There's also a warning system for extremely high or low temperatures.

## Requirements

- Raspberry Pi 4B
- W1ThermSensor (Wired Temperature Sensor)
- Python 3.x
- Visual Studio Code
- Windows 10 on ASUS laptop Intel Core i7

## Installation

1. **Raspberry Pi Setup:**
   - Connected the W1ThermSensor to the Raspberry Pi.
   - Raspberry Pi is properly configured and connected to the internet.

2. **Python Environment:**
   - Installed Python 3.x on the Raspberry Pi.

3. **Install Dependencies:**
   - Installed the necessary Python packages. 
    
## Usage

1. **Run the Temperature Monitoring Script:**
   - Executed the Python script that reads temperature data from the W1ThermSensor.
     
2. **View Temperature Data:**
   - View the temperature data on the console and integrate the script with a data logging system or a web interface.

## Project Structure

- `source_temp`: Main script for reading and displaying temperature data.
- `doc`: Documentation folder.
- `exemples`: Example code or configuration files.
- `templates`: coding templates
- `tests`: tests to confirm the reliability of the system

## License

This project is licensed under the [Star Wars Solutions](CR2-D2).

## Acknowledgments

- The equipment used in this project was a low-cost, second-hand purchase, improving the environment and sustainability of the Earth planet.

## Contact

For any inquiries, please contact [Suzanne Freitas] at [L00179723@atu.ie].

