# Samsung-Motionphoto-Deletion

## Description
This is a script I wrote long time ago, I uploaded it here for other people's use.

Samsung motionphoto is similar to apple's live photo.
But it stores all the motion part inside the jpg file.
JPG file ends with hex FFD9, so this program finds such HEX and delete the rest of the file contents.

Samsung's own Gallery app can extract the motion photo as gif, and this is the feature to be added.

## Feature
Though Samsung's own Gallery app can delete the motion photo part of the jpg file, but it can only be executed one at a time with multiple taps.

This python script is a batch process.

## Warning
**The most important warnings are listed below**

**1. The script will read all the files in the fold denoted by the path that user entered, but it
does not detect whether the input file is a valid jpg file. Unexpected behavior can happen to such file**

**2. The panorama motion photo is different from the regular still image in Samsung's camera system, so 
please do not include any panorama motion photo in the path folder**

**3. Please backup all the files before using this script!!**
