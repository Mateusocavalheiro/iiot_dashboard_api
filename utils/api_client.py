import requests

import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

BASE_URL = "https://iiot-sensors-api-fastapi.onrender.com"

def get_sensores():
    return requests.get(f"{BASE_URL}/sensores/", verify=False).json()

def criar_sensor(sensor_data):
    response = requests.post(f"{BASE_URL}/sensores/", verify=False, json=sensor_data)
    return response.json()

def get_leituras(sensor_id):
    return requests.get(f"{BASE_URL}/leituras/{sensor_id}", verify=False).json()
