import os
import random

FOLDERPATH = "D:\\Tutorials\\Algoexpert\\Become an Algorithms Expert Updated\\"
RANDOM_VIDEO = random.choice(os.listdir(FOLDERPATH))
EXTENSION = os.path.splitext(RANDOM_VIDEO)[1]
VIDEOEXTENSION = ".mp4"
if EXTENSION == VIDEOEXTENSION:	pass
else: RANDOM_VIDEO = random.choice(os.listdir(FOLDERPATH))
FULLPATH = FOLDERPATH  + RANDOM_VIDEO
FULLPATH = str(FULLPATH)

print("Video name :" , RANDOM_VIDEO)

print("final : ", FULLPATH)

