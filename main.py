import os
import requests
from datetime import datetime, timezone
import smtplib

MY_LAT = 13.435979
MY_LONG = 79.952507

My_email = os.environ["MY_EMAIL"]
My_password = os.environ["MY_PASSWORD"]

def iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (MY_LAT-5 <= iss_latitude <= MY_LAT+5) and (MY_LONG-5 <= iss_longitude <= MY_LONG+5)

def is_night():
    parameters = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0}
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()["results"]
    sunrise = datetime.fromisoformat(data["sunrise"])
    sunset = datetime.fromisoformat(data["sunset"])
    now = datetime.now(timezone.utc)
    return now < sunrise or now > sunset

def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=My_email, password=My_password)
        connection.sendmail(
            from_addr=My_email,
            to_addrs="gokuluebejev@gmail.com",
            msg="Subject:Look Up!\n\nThe ISS is above you in the sky!"
        )

if iss_overhead() and is_night():
    send_mail()
    print("Email sent successfully")
