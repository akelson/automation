#!/usr/bin/python

import argparse
import datetime
import ephem

parser = argparse.ArgumentParser('Output the time of the next sunset in HH:MM format.')
parser.add_argument('--offsetmins', dest='offsetmins', 
		help='apply an offset in minutes to the time output')
args = parser.parse_args()

# Denver
observer = ephem.Observer()
observer.lat = '39.7392'
observer.lon = '-104.9903'
observer.elevation = 5280

sun = ephem.Sun()

# Python datetime object
sunset = ephem.localtime(observer.next_setting(sun))

# Apply offset if provided
if (args.offsetmins):
	sunset += datetime.timedelta(minutes=int(args.offsetmins))

print sunset.strftime("%H:%M")
