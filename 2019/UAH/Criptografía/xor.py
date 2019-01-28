import cv2
import numpy as np
import os

# set video file path of input video with name and extension
vid = cv2.VideoCapture('./result.mp4')


if not os.path.exists('frames'):
    os.makedirs('frames')

#for frame identity
index = 0
keyFrame = None
while(True):
    # Extract images
    ret, frame = vid.read()

    # end of frames
    if not ret:
        break

    if index == 0:
        keyFrame = frame
    else:
        frame = frame ^ keyFrame

    # Saves images
    name = './frames/frame' + str(index) + '.jpg'
    print ('Creating...' + name)
    cv2.imwrite(name, frame)

    # next frame
    index += 1


frames = sorted(os.listdir('./frames'))
frame_array = []

for i in range(len(frames)):
    filename = './frames/' + frames[i]
    #reading each files
    img = cv2.imread(filename)
    height, width, layers = img.shape
    size = (width,height)

    #inserting the frames into an image array
    frame_array.append(img)

    out = cv2.VideoWriter('./xoredResult.mp4',cv2.VideoWriter_fourcc(*'mp4v'), 25, size)

for i in range(len(frame_array)):
    # writing to a image array
    out.write(frame_array[i])
out.release()
