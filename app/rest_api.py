import requests
import time


def post_api(image_path):
    url = 'https://example.com/'
    # Mockserver
    # url = "http://192.168.110.131:3000/"
    request_timestamp = int(time.time())
    response = requests.post(url)
    response_timestamp = int(time.time())
    
    parameter = {
        'image_path': image_path,
    }
    response = requests.post(url, json=parameter).json()

    
    return response, request_timestamp, response_timestamp
