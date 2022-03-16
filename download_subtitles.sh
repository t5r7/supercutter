#!/bin/bash

# loop over every webm file in the current folder
for v in *.webm; do
    # cut out the video ID from the filename
    # by default yt-dlp downloads videos as
    # "Video Title [videoid].xyz"
    thisVideoID=$(echo $v | cut -d"]" -f1 | cut -d"[" -f2)
    echo $thisVideoID
    
    # if we've not already got the transcript
    if [ ! -f "$v.json" ]
    then
        # https://github.com/jdepoix/youtube-transcript-api#cli
        youtube_transcript_api "$thisVideoID" --languages en --format json > "$v.json"
    fi

done