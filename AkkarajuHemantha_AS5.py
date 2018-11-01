# Author: Hemantha Akkaraju
# Assignment: Image Processing with Vectors
#
import math
from math import sin
import sys
sys.path.append('./Lib')

from image_mat_util import file2image
from image_mat_util import image2display
from image_mat_util import image2file

imgA = file2image("SourceImages/s1-256.png")
imgB = file2image("SourceImages/s2-256.png")
#   image[row][column]
#   len(image) says how many rows [y-size, or height]
#   len(image[0]) says how many column [x-size, or width]
# image2display(m)

# (A) Demonstrate the results of convex sum between the two images by varying
# alpha between 0 and 1.
# Convex sum = alpha * s1 + (1 - alpha) * s2 where 0 <= alpha <= 1
def convex_sum(imgOne, imgTwo):
    alpha = 0.0
    new_image = []
    for r in range(len[imgTwo]):
        for c in range(len(imgTwo[0])):
            new_image = tuple(apha * i + (1 - apha) * j for i, j in zip(imgOne, imgTwo))
            alpha = alpha + 0.1
    return new_image

convex = convex_sum(imgA, imgB)
image2display(convex)

# (B) Demonstrate the results of affine sum between the two images by varying alpha
# between 1 and 2. Note, when alpha is 2, beta must be -1, in a very real sense, we are
# removing image-s2 from image-s1.
# Affine sum = aplha * s1 + beta * s2


