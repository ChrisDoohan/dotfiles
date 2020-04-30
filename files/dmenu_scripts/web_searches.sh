#!/bin/bash

key=$(echo $'g\nimg\nyt' | dmenu)
if [[ $key == *"yt"* ]]
then
    echo "youtube"
	base_url="youtube.com/results?search_query="
elif [[ $key == *"img"* ]]
then
    echo "images"
	base_url="images.google.com/search?q="
else [[ $key == *"g" ]]
    echo "google"
	base_url="google.com/search?q="
fi

