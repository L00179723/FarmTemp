# temperature_alert.py

from source_temp.directory_utilities import log_temperature

def check_alert(w1thermsensor):
    if log_temperature < -3:
        return f"Low temperature!Check area!({log_temperature:.2f} °C)"
    elif log_temperature > 30:
        return f"High temperature! Attention need! ({log_temperature:.2f} °C)"
    else:
        return None

