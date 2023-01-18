import sys
import time
import cv2
import os
from datetime import datetime
def extract_frames(video_path):
    # Create folder name with current date and time
    folder_name = datetime.now().strftime('%Y-%m-%d_%H.%M.%S')
    os.makedirs(folder_name)

    # Open video file
    vidcap = cv2.VideoCapture(video_path)

    # Initialize frame count
    frame_count = 0

    # Get total frame count
    total_frame_count = vidcap.get(cv2.CAP_PROP_FRAME_COUNT)

    # Iterate over frames in video
    while True:
        success, image = vidcap.read()
        if not success:
            break
        # Save frame as image
        cv2.imwrite(f"{folder_name}/{frame_count}.jpg", image)
        
        # Print progress
        percentage = (frame_count / total_frame_count) * 100
        sys.stdout.write("[")
        for i in range(int(percentage)):
            sys.stdout.write("=")
        sys.stdout.write("]")
        sys.stdout.write(f" {int(round(percentage))}%")
        sys.stdout.flush()
        sys.stdout.write("\r")
        time.sleep(0.01)
        frame_count += 1

# Get video path from command line argument
video_path = sys.argv[1]

# Extract frames from video
extract_frames(video_path)
