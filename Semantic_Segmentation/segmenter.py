import cv2
import argparse
import numpy as np 
from collections import Counter
import matplotlib.pyplot as plt

def display_image(image):
    cv2.imshow("Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def read_image(image_path):
    # image = cv2.imread(image_path, cv2.IMREAD_COLOR)
    image = cv2.imread(image_path, 1)
    
    return image

def get_pixel_color(image, height_start, height_end, width_start, width_end):
    pixel_list = []
    for x in range (height_start, height_end+1):
        for y in range (width_start, width_end+1):
            pixel = image[x,y]
            if len(pixel) == 1:
                pixel_list.append(pixel)
            else:
                pixel_string = ""
                for p in pixel:
                    pixel_string = pixel_string + str(p) + ":"
                pixel_string = pixel_string[:-1]
                pixel_list.append(pixel_string)
    
    return pixel_list

def get_pixel_count(pixel_list):
    print("Pixel List Length : {}".format(len(pixel_list)))
    print("Unique Pixel Count : {}".format(len(Counter(pixel_list).keys())))
    pixel_count = {}
    for p in pixel_list:
        if p in pixel_count.keys():
            pixel_count[p] = pixel_count[p] + 1
        else:
            pixel_count[p] = 1

    return pixel_count

def get_bit(highest_count):
    bit = ""
    for p in range(0, len(highest_count)-1):
        if highest_count[p] < highest_count[p+1]:
            bit = bit + "1"
        else :
            bit = bit + "0"

    return bit

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help = "Name of the target file")
    args = parser.parse_args()

    image = read_image(args.filename)
    
    dimenssion = image.shape    
    height = dimenssion[0]
    width = dimenssion[1]
    print("Image Height : {} px".format(str(height)))
    print("Image Width : {} px".format(str(width)))
    height_new = height - (height%3)
    width_new = width - (width%3)
    print("{}: {}".format(height_new, width_new))
    image_new = cv2.resize(image, (width_new, height_new))
    
    h_start = 1
    seg_pos = []
    highest_count = []
    for i in range(1,4):
        h_range = int(height_new/3) - 1
        h_end = h_start + h_range
        w_start = 1
        for j in range(1,4):
            w_range = int(width_new/3) - 1
            w_end = w_start + w_range
            print("Reading from Height : {},{} and Width : {},{}".format(h_start, h_end, w_start, w_end))
            pixel_list = get_pixel_color(image, h_start, h_end, w_start, w_end)
            pixel_count = get_pixel_count(pixel_list)

            pixel_count_sorted = dict(sorted(pixel_count.items(), key = lambda x: x[1], reverse = True))
            first_pair = next(iter((pixel_count_sorted.items())))

            seg_pos.append("({}, {})".format(i, j))
            highest_count.append(first_pair[1])

            print("Segment ({}, {}) :: Pixel_color : [{}] and Count : {}".format(i, j, first_pair[0], first_pair[1]))

            w_start = w_start + w_range + 1
        h_start = h_start + h_range + 1
    
    bit = get_bit(highest_count)

    plt.bar(seg_pos, highest_count)

    plt.title("8-Bit word: {}".format(bit))
    plt.xlabel("Segment_Position")
    plt.ylabel("Count")
    
    plt.show()

   