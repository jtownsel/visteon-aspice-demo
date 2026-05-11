CALIBRATION_OFFSETS = {
    "temperature": {"min": -40, "max": 125, "offset": 0.3, "unit": "celsius"},
    "pressure": {"min": 0, "max": 400, "offset": 1.2, "unit": "kPa"},
    "ambient_light": {"min": 0, "max": 100000, "offset": 50, "unit": "lux"},
}

def get_offset(sensor_type: str) -> float:
    if sensor_type not in CALIBRATION_OFFSETS:
        raise ValueError(f"Unknown sensor: {sensor_type}")
    return CALIBRATION_OFFSETS[sensor_type]["offset"]
