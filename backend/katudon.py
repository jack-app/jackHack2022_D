import cv2
import numpy as np
from PIL import Image
def make_gif(timestamp,float_filename):  
    pictures = []
    fps = 30
    img1 = cv2.imread(float_filename)
    bg_img = cv2.imread(timestamp+'.jpeg')
    height,width = img1.shape[:2]
    fg_img = cv2.resize(img1,(2*width,2*height),interpolation=cv2.INTER_CUBIC)
    hsv = cv2.cvtColor(fg_img, cv2.COLOR_BGR2HSV)
    bin_img = cv2.inRange(hsv, (0, 10, 0), (255, 255, 255))
    contours, _ = cv2.findContours(bin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=lambda x: cv2.contourArea(x))
    mask = np.zeros_like(bin_img)
    cv2.drawContours(mask, [contour], -1, color=255, thickness=-1)
    for i in range(fps):
        if i%fps <= fps//2:
            bg_img = cv2.imread(timestamp+'.jpeg')
            loc = timestamp + str(i)+'.png'
            x, y = 1750, 800-7*i
            w = min(fg_img.shape[1], bg_img.shape[1] - x)
            h = min(fg_img.shape[0], bg_img.shape[0] - y)
            fg_roi = fg_img[:h, :w]
            bg_roi = bg_img[y : y + h, x : x + w]
            bg_roi[:] = np.where(mask[:h, :w, np.newaxis] == 0, bg_roi, fg_roi)
            cv2.imwrite(loc,bg_img)
            pic = Image.open(loc)
            pictures.append(pic)
            pictures[0].save(timestamp+'.gif',save_all=True, append_images=pictures[1:], optimize=False, duration=100, loop=0)

        else:
            bg_img = cv2.imread(timestamp+'.jpeg')
            loc = timestamp + str(i)+'.png'
            x, y = 1750, 800-7*(fps-i)
            w = min(fg_img.shape[1], bg_img.shape[1] - x)
            h = min(fg_img.shape[0], bg_img.shape[0] - y)
            fg_roi = fg_img[:h, :w]
            bg_roi = bg_img[y : y + h, x : x + w]
            bg_roi[:] = np.where(mask[:h, :w, np.newaxis] == 0, bg_roi, fg_roi)
            cv2.imwrite(loc,bg_img)
            pic = Image.open(loc)
            pictures.append(pic)
            pictures[0].save(timestamp+'.gif',save_all=True, append_images=pictures[1:], optimize=False, duration=100, loop=0)


