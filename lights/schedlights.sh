#!/bin/bash

DIR=`dirname "${BASH_SOURCE}"`

# The time 30 min before sunset.
TIME_ON=`${DIR}/sunset.py --offsetmins=-30`

# Turn the light on.
echo "${DIR}/cmd_ifttt_event.sh light_on_living_room" | at ${TIME_ON}

# Turn the light off.
echo "${DIR}/cmd_ifttt_event.sh light_off_living_room" | at 22:30
