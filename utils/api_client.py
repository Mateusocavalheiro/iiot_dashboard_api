import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://iiot-fastapi.onrender.com"

def get_sensores():
    return requests.get(f"{BASE_URL}/sensores/", verify=False).json()

def criar_sensor(sensor_data):
    response = requests.post(f"{BASE_URL}/sensores/", verify=False, json=sensor_data)
    return response.json()

def get_leituras(sensor_id):
    return requests.get(f"{BASE_URL}/leituras/{sensor_id}", verify=False).json()


def get_leituras_by_dates(sensor_id, start=None, end=None):
    params = {}
    if start:
        params["start"] = start
    if end:
        params["end"] = end

    response = requests.get(f"{BASE_URL}/leituras/{sensor_id}", params=params, verify=False)
    return response.json()