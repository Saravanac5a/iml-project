import cv2
import numpy as np
import os

data = []
target = []

for filename in os.listdir("C:/Python files/participants_data/AlgonautsVideos268_All_30fpsmax"):
    vidcap = cv2.VideoCapture('C:/Python files/participants_data/AlgonautsVideos268_All_30fpsmax/'+str(filename))
    success,image = vidcap.read()
    success = True
    frames = []
    while success:
        frames.append(image)
        success,image = vidcap.read()
    frames = np.array(frames)
    target.append(int(filename[:4]))
    data.append(frames)
data = np.array(data)
#https://gist.github.com/dsalaj/b9143289784fbd7f741518301e6037ce
#%%