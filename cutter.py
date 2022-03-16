import json, sys, os, re

# SUPERCUTTER
# https://github.com/itsmeimtom/supercutter

# words to clip segments of
keywords = [
    "good size",
    "nice size",
    "generous",
    "not just a"
]
# segments longer than this
# won't be exported
maxClipLength = 6

if(not sys.argv[1]):
    print("missing arg: video file")
    quit()
if(not sys.argv[2]):
    print("missing arg: subtitle file")
    quit()
if(not sys.argv[2]):
    print("missing arg: output folder")
    quit()

videoFilePath = sys.argv[1]
subsFilePath = sys.argv[2]
outputFolder = sys.argv[3]
 
print("""
!!SUPERCUTTER STARTING!!

Video File: "%s"
Subs  File: "%s"
Out Folder: "%s"
"""%(videoFilePath,subsFilePath,outputFolder))

subsFile = open(subsFilePath, "r")
subs = json.loads(subsFile.read())


# convert from seconds to hh:mm:ss for ffmpeg
# https://www.geeksforgeeks.org
# /python-program-to-convert-seconds-into-hours-minutes-and-seconds/
def hms(seconds):
    min, sec = divmod(seconds, 60)
    hour, min = divmod(min, 60)
    return "%d:%02d:%02d" % (hour, min, sec)


# cut the clip using ffmpeg
# todo: use python ffmpeg implementation rather
#       than using os.system
def cut_segment(inputPath,startTime,duration,outputPath):
    startTime = hms(round(startTime))
    duration = round(duration)
    if(maxClipLength and duration > maxClipLength):
        print("skipping this one (over %s secs - is %s seconds long)"%(maxClipLength, duration))
        return # skip over long clips
    else:
        os.system('ffmpeg -n -hide_banner -loglevel error -ss %s -i "%s" -t %s "%s" '%(startTime, inputPath, duration, outputPath))


# loop over every caption in the subtitle file
for caption in subs[0]:
    if(not caption["text"]):
        continue

    # check if the caption contains the keywords
    # https://stackoverflow.com/a/3389611/6325767
    if any(x in caption["text"] for x in keywords):
        text = caption["text"]
        startTime = caption["start"]
        duration = caption["duration"]

        textClean = text.replace(' ', '_') # swap spaces for underscores
        textClean = re.sub(r'\W+', '', textClean) # todo: make this more inclusive
        outputFile = "%s/%s-%ssecs.mp4"%(outputFolder,textClean,duration)

        print("cutting segment that starts at %s, lasts %s seconds: '%s'"%(startTime, duration, text))
        cut_segment(videoFilePath, startTime, duration, outputFile)



# done with you now!!
subsFile.close()
print("!!SUPERCUTTER FINISHED!!")