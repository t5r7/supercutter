# SuperCutter - "another good size repo actually"

Extract segments from downloaded YouTube videos based on their captions.

Created after I noticed that [CGP Estate Agents](https://www.cgpooks.co.uk/) used phrases such as "a large size room" or "a good size" comically often during [their tours](https://www.youtube.com/channel/UCfcoX8GszBlY-NFidzD_h9A). After manually editing [a supercut](https://www.youtube.com/watch?v=9Fi1-D0Ss3g) of some occurrences, I endeavored to (somewhat) automate the process.

# How to Use
Before starting, update the keywords at the top of `cutter.py`.


## For multiple videos
1. Download videos using whichever method you prefer. I use [yt-dlp](https://github.com/yt-dlp/yt-dlp) since it has proven to be faster than youtube-dl.
2. Scrape subtitles using `download_subtitles.sh`. Make sure to modify this file if your video files are named differently.
3. Run `every_vid_in_folder.sh` in the folder containing the videos. Make sure to modify the output folder if you'd like. Note that it assumes the subtitle files are named video.mp4.json.

## For a single video
1. Run `cutter.py` with the arguments `[video file]`, `[subtitle file]`, `[clips output directory]`

# Notes
The subtitles must be in the JSON format as obtained by [youtube_transcript_api](https://github.com/jdepoix/youtube-transcript-api#cli)

# Improvements to be Made
- Automate video and subtitle downloading; feed the program a list of video IDs and have it work
- Improve handling of arguments and configuration
