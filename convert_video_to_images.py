import sys
import cv2
import os
from datetime import datetime

# Get the video file from the command line argument
video_file = sys.argv[1]

# Create a datetime object containing the current date and time
now = datetime.now()

# Create a new directory with the date and time as the name
directory = now.strftime("%Y%m%d-%H%M%S")
os.mkdir(directory)

# Open the video file
video = cv2.VideoCapture(video_file)

# Read the first frame
success, frame = video.read()

# Enter a while loop to read the remaining frames
while success:
    # Save the frame as an image file in the new directory
    cv2.imwrite(os.path.join(directory, str(video.get(cv2.CAP_PROP_POS_FRAMES)) + ".jpg"), frame)
    
    # Print a message indicating whether or not a new frame was successfully read
    print("Frame #{} successfully read".format(video.get(cv2.CAP_PROP_POS_FRAMES)))
    
    # Read the next frame
    success, frame = video.read()
