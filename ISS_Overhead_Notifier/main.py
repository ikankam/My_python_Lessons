import time

import requests
from datetime import datetime
import smtplib
import datetime

MY_LAT = "Your Location LAT Here"
MY_LONG = "Your Location LONG Here"

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}


# -------------Making the API request and getting the position of the ISS-------------#
def iss_position():
    """Getting the ISS longitude and latitude"""
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()
    longitude = iss_response.json()["iss_position"]["longitude"]
    latitude = iss_response.json()["iss_position"]["latitude"]
    position = (float(latitude), float(longitude))
    #print(position)

    if MY_LAT - 5 <= iss_position[0] <= MY_LAT + 5 and MY_LONG - 5 <= iss_position[0] <= MY_LONG + 5:
        return True


# -------Making the API request and getting the sunrise and sunset times of user location----------#
def nighttime():
    """Getting user location sunrise and sunset times and current user time to
    compare if it is indeed nighttime"""
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])
    print(sunrise, sunset)
    current_hour = datetime.now().hour
    if current_hour <= sunrise or current_hour >= sunset:
        return True


while True:
    time.sleep(60)   #refresh every 60 secs
    if nighttime() and iss_position():
        email = "my_email@gmail.com"
        password = "my_password_here"
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email,
                                msg="ISS overhead reminder! :)\n\n Look up to view the ISS!")
