import argparse
import requests
import json
import os
import logging

def getConfig():
    config_path = os.path.expanduser('~/moosefood.json')
    with open(config_path) as f:
        return json.loads(f.read())

def feed(grams):
    config = getConfig()
    url = config['url']
    grams_per_sec = float(config['grams_per_min']) / 60
    feed_dur_sec = str(int(grams / grams_per_sec))

    logging.info("Feeding {} grams in {} sec.".format(grams, feed_dur_sec))
    r = requests.get(url + '/feed', params = {'seconds' : feed_dur_sec})
    logging.info("status_code: {}".format(r.status_code))

def main():
    logging.basicConfig(
        filename = 'moosefood.log', 
        level = logging.INFO,
        format = '%(asctime)s %(levelname)s: %(message)s')

    parser = argparse.ArgumentParser(description = 'Feed the Moose.')
    parser.add_argument('grams', type = float, help = 'Grams of food to dispense..')

    args = parser.parse_args();

    feed(args.grams)

if '__main__' == __name__:
    main()
