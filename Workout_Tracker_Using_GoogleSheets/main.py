import requests
from datetime import datetime

# User details
GENDER = "YOUR SEX HERE"
WEIGHT = YOUR WEIGHT HERE (float)
HEIGHT = YOUR HEIGHT HERE (float)
AGE = YOUR AGE HERE (int)
APP_ID = "YOUR nutritionix APP ID"  # Obtained from https://trackapi.nutritionix.com
API_KEY = "YOUR nutritionix API KEY"   # Obtained from https://trackapi.nutritionix.com
bearer_headers = {
    "Authorization": "Bearer Your self-generated token here"
}

# Sheety and Exercise Endpoints
sheety_url = 'https://api.sheety.co/userID/ProjectName/SheetName'  # Check your sheety account Dashboard for URL
exercise_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

# Get Exercise Stats with Natural Language Queries
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

params = {
    "query": input("Tell me which exercises you did today?"),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE,
}
response = requests.post(url=exercise_url, json=params, headers=headers)
response.raise_for_status()
result = response.json()
print(result)

# Getting today's date and time 
today = datetime.now()

# Iterating through every exercise given by the user
for workout in range(len(result["exercises"])):
    # Write exercise to google sheets using sheety
    sheety_params = {

        "workout": {
            "date": today.strftime("%d/%m/%Y"), # formatting the date in day/month/year format
            "time": today.strftime("%X"), 
            "exercise": (result["exercises"][workout]["name"]).title(),
            "duration": result["exercises"][workout]["duration_min"],
            "calories": result["exercises"][workout]["nf_calories"],

        }
    }
    sheety_response = requests.post(url=sheety_url, json=sheety_params, headers=bearer_headers)
    print(sheety_response.text)
