import os
import json
import http.client, urllib
import logging

logging.basicConfig(
    filename = 'homeautomation.log', 
    level = logging.INFO,
    format = '%(asctime)s %(levelname)s: %(message)s')

def readConfig():
    config_path = os.path.expanduser('~/ha_config.json')
    with open(config_path) as f:
        return json.loads(f.read())

def sendNotification(msg):
    logging.info("sending notification: {}".format(msg))
    config = readConfig()
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
      urllib.parse.urlencode({
        "token": config["pushover"]["APP_TOKEN"],
        "user": config["pushover"]["USER_KEY"],
        "message": msg,
      }), { "Content-type": "application/x-www-form-urlencoded" })
    logging.info("pushover api response: {}".format(conn.getresponse().status))

