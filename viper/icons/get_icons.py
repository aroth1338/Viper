import os
from PIL import Image
from color_wheel.conversion import hex_to_rgb, blend_colors
import importlib.resources as pkg_resources
from . import images

images_path = pkg_resources.files(images)


def healthy(color = "#000000"):
    fileName = "Young"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[3] < 0.1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def elderly(color = "#000000"):
    fileName = "Elderly"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[3] < 0.1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def foot(color = "#000000", filled = False):
    if not filled: fileName = "Barefoot_2"
    else: fileName = "Barefoot_Solid"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 230 and item[1] >= 230 and item[2] >= 230:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def walking(color = "#000000"):
    fileName = "Man_Walking"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def open_hand(color = "#000000"):
    fileName = "Open_Hand"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245 or item[3] < 1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def hand(color = "#000000", filled = False):
    if not filled: fileName = "Hand_icon"
    else: fileName = "Hand_icon_filled"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245 or item[3] < 1:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def sight(color = "#000000"):
    """
    Returns a Sight icon image in the given color.
    Color must be in Hex Code
    """
    
    fileName = "Sight"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        else:
            newData.append((new_color[0], new_color[1], new_color[2], 255))

    img.putdata(newData)
    return img

def reward(color = "#000000"):
    """
    Returns a Reward Sound Icon in the given color.
    Color must be in hex code.
    """
    
    fileName = "Reward_Sound"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        elif item[0] < 132:
            newData.append((new_color[0], new_color[1], new_color[2], 255))
        else:
            newData.append(blend_colors(new_color, (255, 255, 255)))

    img.putdata(newData)
    return img

def punishment(color = "#000000"):
    """
    Returns a Punishment Sound Icon in the given color.
    Color must be in hex code.
    """
    
    fileName = "Punishment_Sound"
    pic_format = "png"
    new_color = color #change this to desired color

    filepath = os.path.join(images_path, fileName)
    img = Image.open(filepath + '.' + pic_format)
    img = img.convert("RGBA")
    datas = img.getdata()

    new_color = hex_to_rgb(new_color)

    newData = []

    for i, item in enumerate(datas):
        if item[0] >= 245 and item[1] >= 245 and item[2] >= 245:
            newData.append((255, 255, 255, 0))
        elif item[0] < 132:
            newData.append((new_color[0], new_color[1], new_color[2], 255))
        else:
            newData.append(blend_colors(new_color, (255, 255, 255)))

    img.putdata(newData)
    return img

if __name__=='__main__':
    print(images_path)