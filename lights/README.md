# Perform light automation tasks

The lights are turned on before sunset. It is possible to turn lights on at
sunset with IFTTT using a sunset trigger from Weather Underground, but it is 
not possible to turn the lights on before sunset.

A python script using [PyEphem](http://rhodesmill.org/pyephem/) is used to 
determine when sunset will occur.

The lights are controlled by a Smart Life socket and using an IFTTT maker 
[Webhooks](https://ifttt.com/maker_webhooks) action.

My IFTTT maker key is located at ~/ifttt_maker_key.

The automation is performed in three steps:
1. A crontab job runs every night at midnight and kicks off schedlights.sh.
1. The schedlights.sh script uses the Linux 'at' command to schedule scripts to 
   turn the lights on or off at certain times of day.
1. The lights are turned on or off by scripts which performs web requests
   to maker.ifttt.com to trigger events.
