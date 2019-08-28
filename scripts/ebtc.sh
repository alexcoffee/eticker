#!/bin/bash

PRICE=$(curl -s https://api.coindesk.com/v1/bpi/currentprice/usd.json | grep -o 'rate":"[^"]*' | cut -d\" -f3 | cut -d\. -f1)
DATE=$(date "+%_I:%M %p")

LINE1="BTC Price"
LINE2="$DATE"
LINE3="\$$PRICE"

/usr/local/bin/papirus-write "$LINE1"$'\n'"$LINE2"$'\n'"$LINE3" --fsize 30
