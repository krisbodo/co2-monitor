"""Send push notifications to your phone with pushover"""
import http.client
import urllib
import os
from dotenv import load_dotenv

# load environment variables.
load_dotenv()

def high_co2_notification(co2_ppm):
    connection = http.client.HTTPSConnection("api.pushover.net:443")
    connection.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": os.environ["PUSHOVER_APP_TOKEN"],
        "user": os.environ['PUSHOVER_USER_KEY'],
        "message": f"CO2 concentration is {co2_ppm}ppm, open the window",
    }), { "Content-type": "application/x-www-form-urlencoded" })

    return connection.getresponse()

if __name__ == '__main__':
    high_co2_notification(1250)