import cv2
import numpy as np
from PIL import Image
import os, sys
from colormath.color_objects import sRGBColor, LabColor
from colormath.color_conversions import convert_color
from colormath.color_diff import delta_e_cie2000
import math

def run_mosaic(input_img_folder, input_image, output_image, pixel_width, pixel_height, real_color_diff = False):
    downsize_all_images(input_img_folder, 'basic_mosaic_downsize\\', pixel_width, pixel_height)
    dict_lib = dictionary_of_quantified_lib_images('basic_mosaic_downsize\\')
    stitch_replacement(dict_lib, input_image, output_image, pixel_width, pixel_height, real_color_diff)

def stitch_replacement(dict_lib, target_image, output_image, pixel_width, pixel_height, real_color_diff):
    start_x = 0
    start_y = 0
    end_x = pixel_width
    end_y = pixel_height
    target_img = Image.open(target_image)
    target_width, target_height = target_img.size
    res_array = None
    cur_row = None
    count = 0
    target_data = cv2.imread(target_image)

    while start_x < target_width and start_y < target_height:
        #maybe switch
        target_section = target_data[start_y:end_y,start_x:end_x]
        closest = get_closest_lib_img(target_section, dict_lib, real_color_diff)
        if cur_row == None:
            cur_row = cv2.imread(closest)
        else:
            cur_row = np.concatenate([cur_row, cv2.imread(closest)], axis=1)

        print "Found match for #" + str(count)
        count +=1

        start_x += pixel_width
        if start_x >= target_width:
            start_x = 0
            start_y += pixel_height
            if res_array == None:
                res_array = cur_row
            else:
                res_array = np.concatenate([res_array, cur_row], axis=0)

            cur_row = None
        end_x = start_x + pixel_width
        end_y = start_y + pixel_height

    cv2.imwrite(output_image,res_array)

def simple_color_diff(color_1, color_2):
    r_diff = int(abs(color_1[0]-color_2[0]))
    g_diff = int(abs(color_1[1]-color_2[1]))
    b_diff = int(abs(color_1[2]-color_2[2]))

    return r_diff + g_diff + b_diff

#http://hanzratech.in/2015/01/16/color-difference-between-2-colors-using-python.html
def color_diff(color_1, color_2):
    # Red Color 6
    color1_rgb = sRGBColor(color_1[0], color_1[1], color_1[2])
    #  Blue Color 9
    color2_rgb = sRGBColor(color_2[0], color_2[1], color_2[2])
    # Convert from RGB to Lab Color Space 12
    color1_lab = convert_color(color1_rgb, LabColor)
    # Convert from RGB to Lab Color Space 15
    color2_lab = convert_color(color2_rgb, LabColor)
    # Find the color difference 18
    delta_e = delta_e_cie2000(color1_lab, color2_lab)
    return delta_e

def downsize_all_images(folder_in, folder_out, pixel_width, pixel_height):
    count = 0
    for item in os.listdir(folder_in):
        if os.path.isfile(folder_in+item) and item.endswith('.jpg'):
            im = Image.open(folder_in+item)
            f, e = os.path.splitext(folder_in+item)
            imResize = im.resize((pixel_width, pixel_height), Image.ANTIALIAS)
            imResize.save(folder_out + item[:-4] + '-resized.jpg', 'JPEG', quality=90)
            count+=1

def get_closest_lib_img(target_section, dict_lib, real_color_diff):

    winning_diff = 0
    winning_image = None
    for key, value in dict_lib.iteritems():
        cur_diff = 0
        for y in xrange(0,target_section.shape[0]):
            for x in xrange(0, target_section.shape[1]):
                if real_color_diff:
                    cur_diff += color_diff(target_section[y,x], value[y,x])
                else:
                    cur_diff += simple_color_diff(target_section[y,x], value[y,x])
                #cur_diff += abs(target_section[y,x,0]-value[y,x,0]) + abs(target_section[y,x,1]-value[y,x,1]) + abs(target_section[y,x,2]-value[y,x,2])
        if cur_diff < winning_diff or winning_image == None:
            winning_diff = cur_diff
            winning_image = key

    return winning_image

def dictionary_of_quantified_lib_images(img_folder):
    dict_to_return = {}
    for item in os.listdir(img_folder):
        if os.path.isfile(img_folder + item):
            im = cv2.imread(img_folder + item)
            dict_to_return[img_folder+item] = im
    return dict_to_return

