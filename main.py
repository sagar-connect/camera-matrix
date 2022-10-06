from cv2 import VideoCapture, flip
import os
from RgbToBrightness import RgbToBrightnessObj
import numpy as np

TERM_ROWS, TERM_COLS = 50, 160
CAM_HEIGHT, CAM_WIDTH = 180, 320

os.system(f'mode con: cols={TERM_COLS} lines={TERM_ROWS}')
os.system('cls')
os.system('color 0a')

vc = VideoCapture(0)
vc.set(4, CAM_HEIGHT)
vc.set(3, CAM_WIDTH)

while True:
    rval, frame = vc.read()
    frame = flip(frame, flipCode=1)
    for row in np.arange(0, CAM_HEIGHT, CAM_HEIGHT / TERM_ROWS):
        for col in np.arange(0, CAM_WIDTH, CAM_WIDTH / TERM_COLS):
            r, g, b = frame[int(row)][int(col)]
            print(RgbToBrightnessObj.rgb_to_brightness_map[r, g, b], end='')
    print('\b' * (TERM_ROWS * TERM_COLS), end='')
