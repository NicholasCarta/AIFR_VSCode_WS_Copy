import cv2
import os
import numpy as np

video_folder_path = '/workspaces/AIFR_VSCode_WS_Copy/src/image_processing/split'

background = cv2.imread('/workspaces/AIFR_VSCode_WS_Copy/src/image_processing/split/out1.png')
bkg_gray = cv2.cvtColor(background, cv2.COLOR_BGR2GRAY)

#for loop to iterate over the images
    #read the image
    #convert to gray scale

#create an image of size(background) with white pixels in it


for i in range (1, 87):
    frame_name = f"out{i:01d}.png"
    frame_path = os.path.join(video_folder_path, frame_name)

    current_frame = cv2.imread(frame_path)
    current_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2GRAY)

    diff = current_frame - bkg_gray

    clipped_diff = np.clip(diff, -15, 15)
    # keep adding the diff to the white image
    #keep saving each white image + diff -> outi.png

    bkg_gray = bkg_gray + clipped_diff

#save bkg_image
cv2.imwrite('/workspaces/AIFR_VSCode_WS_Copy/src/image_processing/test/background.png', bkg_gray)

#save the white image

#ffmpeg to concat the images to a video

