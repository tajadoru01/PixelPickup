import requests

response = requests.post("http://127.0.0.1:5000/get_route", json={
    "start": [-79.3957, 43.6629],
    "end": [-79.3806, 43.6544]
})

print(response.status_code, response.json())