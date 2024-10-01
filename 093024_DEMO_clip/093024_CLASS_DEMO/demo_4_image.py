from CLIP_helper import *
import numpy as np
import os
from PIL import Image

#give aceess to the files
THIS_FOLDER = os.path.dirname(__file__)
IMAGE_FOLDER = os.path.join(THIS_FOLDER, 'data/images')
IMAGE_FILES = os.listdir(IMAGE_FOLDER)
IMAGE_FILES = [f for f in IMAGE_FILES if f.endswith(".jpg")]
IMAGE_FILES = [os.path.join(IMAGE_FOLDER, f) for f in IMAGE_FILES]

axis1 = 'baroque'
axis2 = 'modernism'

axis1_vec = encode_text(axis1)
axis2_vec = encode_text(axis2)

img_file = IMAGE_FILES[0]
img = Image.open()

image_vec = encode_image(img)

print("image vector:", image_vec)