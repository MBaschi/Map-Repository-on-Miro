import requests
from config import BOARD_URL, API_TOKEN
url = BOARD_URL+"/items"
headers = {
    "accept": "application/json",
    "authorization": f"Bearer {API_TOKEN}",
    "content-type": "application/json"
}
response = requests.get(url, headers=headers)
if response.status_code == 201:
    print("Request successful")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

url = "https://api.miro.com/v2/boards/uXjVN9EIUF8%3D/shapes"
data = {
    "data": {
        "shape": "rectangle"
    }
}
response = requests.post(url, headers=headers, json=data)
if response.status_code == 201:
    print("Request successful")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)



headers = {
    "accept": "application/json",
    "authorization": f"Bearer {API_TOKEN}",
    "content-type": "application/json"
}
url=BOARD_URL+"/texts"
data = {
              "data": {
                "content": "prova",
                
              },
              "style": {
                "fillColor": "#FAC710",
                "fontSize": int(47500/100)
              },
              "position": {
                "x": 2875.0,
                "y": 2875.0
              },
              "geometry": {
                "width": 47500
              }
            }
response = requests.post(url, headers=headers, json=data)
if response.status_code == 201:
    print("Request successful")
    print(response.json())
else:
    print(f"Request failed with status code {response.status_code}")
    print(response.text)

