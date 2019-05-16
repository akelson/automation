import argparse
import requests
import json
import os

def getConfig():
    config_path = os.path.expanduser('~/moosefood.json')
    with open(config_path) as f:
        return json.loads(f.read())

def feed(grams):
    config = getConfig()
    url = config['url']
    grams_per_sec = float(config['grams_per_min']) / 60
    feed_dur_sec = str(int(grams / grams_per_sec))
    print feed_dur_sec
    r = requests.get(url + '/feed', params = {'seconds' : feed_dur_sec})
    print r
    print r.content

if '__main__' == __name__:
    parser = argparse.ArgumentParser(description = 'Feed the Moose.')
    parser.add_argument('grams', type = float, help = 'Dispense food.')

    args = parser.parse_args();

    feed(args.grams)
