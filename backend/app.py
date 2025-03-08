import os, requests
from flask import Flask, request, jsonify
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

ORS_API_KEY = os.getenv("OPENROUTESERVICE_API_KEY")
if not ORS_API_KEY:
    raise ValueError("ORS_API_KEY is missing! Check your .env file.")

@app.route("/get_route", methods=["POST"])
def get_route():
    data = request.json
    url = "https://api.openrouteservice.org/v2/directions/driving-car"
    
    headers = {
        "Authorization": ORS_API_KEY,  # ✅ Fix: Ensure API key is included
        "Content-Type": "application/json"
    }
    
    response = requests.post(url, json={"coordinates": [data["start"], data["end"]]}, headers=headers)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
