#!/bin/bash

read KEY < ~/ifttt_maker_key
EVENT=light_on_living_room

curl -X POST https://maker.ifttt.com/trigger/${EVENT}/with/key/${KEY}
echo
