Perform light automation tasks.

The lights are controlled by a Smart Life socket and using an IFTTT maker WebHooks action.

Information about IFTTT maker WebHooks can be found at:
https://ifttt.com/maker_webhooks

My IFTTT maker key is located at ~/ifttt_maker_key.

The automation is performed in three steps:
1. A crontab job runs ever night at midnight and kicks off schedlights.sh.
2. The schedlights.sh script uses the Linux 'at' command to schedule scripts to 
   turn the lights lights on or off at certain times of day.
3. The lights are turned on or off by scripts which performs web requests
   to maker.ifttt.com to trigger events.
