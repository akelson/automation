#!/bin/bash

DIR=`dirname "${BASH_SOURCE}"`

# The time 30 min before sunset.
TIME_ON=`${DIR}/sunset.py --offsetmins=-30`

# Turn the lights on at sunset.
at ${TIME_ON} < ${DIR}/lightson.sh
