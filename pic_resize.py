#-*- coding:utf-8 -*-
from PIL import Image
import glob
import cv2

FILE_DIR = './origin_data/dot_data/'
SAVE_DIR = './dataset/'
HEIGHT = 32
WIDTH = 32


def img_resize(dir_path,  h, w):
    path_list = glob.glob(dir_path+"*")
    for img_path in path_list:
        if img_path.find('png') > -1:
            img = Image.open(img_path)
            img_name = img_path.lstrip(dir_path)
            img_name = img_name.lstrip('\\')

            print(img_path, "->", img_name)
            img_resize_lanczos = img.resize((h, w), Image.LANCZOS)
            img_resize_lanczos.save(SAVE_DIR+img_name)

def img_cnvt_ext(dir_path, pre_ext, pst_ext):
    path_list = glob.glob(dir_path+"*")
    for img_path in path_list:
        img_name = img_path.lstrip(dir_path)
        img_name = img_name.lstrip(pre_ext)
        img_name = img_name + pst_ext
        
        print(img_name)
        img = Image.open(img_path)
        img.save(SAVE_DIR+img_name)
        
if __name__ == '__main__':
    img_resize(FILE_DIR, HEIGHT, WIDTH)
