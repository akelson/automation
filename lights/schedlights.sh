#!/bin/bash

DIR=`dirname "${BASH_SOURCE}"`

# The time 30 min before sunset.
TIME_ON=`${DIR}/sunset.py --offsetmins=-30`

# Turn the lights on.
echo "${DIR}/cmd_ifttt_event.sh lights_on_living_room" | at ${TIME_ON}

# Turn the lights off.
echo "${DIR}/cmd_ifttt_event.sh lights_off_living_room" | at 22:30
