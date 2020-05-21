#!/bin/bash
expressvpn status &> /tmp/expressstatus
output=$(tr -d '\0' </tmp/expressstatus)
if [[ $output = *"Connected to"* ]]; then
    echo " "
    exit 0
elif [[ $output = *"Not connected"* ]]; then
    echo " "
    exit 0
else
    echo " "
    exit 0
fi
exit

