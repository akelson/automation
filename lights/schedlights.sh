#!/bin/bash

DIR=`dirname "${BASH_SOURCE}"`

# The time 30 min before sunset.
TIME_ON=`${DIR}/sunset.py --offsetmins=-30`

# Turn the lights on.
at ${TIME_ON} < ${DIR}/cmd_ifttt_event.sh lights_on_living_room
