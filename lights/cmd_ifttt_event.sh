#!/bin/bash

if [[ $#  -ne 1 ]]; then
	echo "Must provide event argument."
	exit 1
fi

read KEY < ~/ifttt_maker_key
EVENT=$1
curl -X POST https://maker.ifttt.com/trigger/${EVENT}/with/key/${KEY}
echo
