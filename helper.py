
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from resizeimage import resizeimage
from pathlib import Path
import pyimgur
import shutil
import os


def get_size(display_message_list):
    max_length = 0
    for item in display_message_list:
        item = item.strip()
        if len(item) > max_length:
            max_length = len(item)
    if max_length <= 5:
        size = "900"
    elif max_length <= 10 and len(display_message_list) < 5:
        size = "300"
    else:
        size = "225"

    print("Size: ",size,"Maximum length: ",max_length)
    return size


def make_jpg(im,color,size):
   
    with open("message.txt") as message:
        message = message.read() 
    print('Size',size,type(message),message)
    im = Image.open(im)
    draw = ImageDraw.Draw(im)
    size = int(int(size)/8.8)
    print(size,type(size))
    font = ImageFont.truetype("Milkshake.ttf",size)
    draw.text((35,1),message,color,spacing=0,font=font)
    im.save('testing.jpg') 
    
    os.chdir('/Users/loribard/src/sendacard/static')
    im.save('testing.jpg')
    os.chdir('/Users/loribard/src/sendacard')
    return im



def make_url(image): 
    CLIENT_ID = "ffa486c0af07526"
    PATH = "testing.jpg"
    uploaded_images = Path("uploaded_images.txt")
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH)
    return uploaded_image.link



def image_sizing(im):
    fd_img = open(im,'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_thumbnail(img,[500,500])
    img.save(im,img.format)
    width, height = img.size
    print(width,height)
    fd_img.close()
    return im

def process_display_message_list(display_message_list):
    for j in range(len(display_message_list)):
        if display_message_list[j] == "":
            display_message_list[j] == "&nbsp;"                    
        else:
            new_item = ''         
            for i in range(len(display_message_list[j]) - 1):
                if display_message_list[j][i] == ' ' and display_message_list[j][i+1] == ' ':
                    new_item += "&nbsp;"
                else:
                    new_item += display_message_list[j][i]   
            new_item += display_message_list[j][-1]
            display_message_list[j] = new_item
    return display_message_list

def background_process(background,size):

    if background == "floral":
        background = "/static/floral-fabric-background-pattern_resized.jpg"
        color = (255,102,0)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "paisley":
        background = "/static/paisley_resized.jpg"
        color = (102,0,102)
        style = "color:rgb" + str(color)+";font-size:"+ size + "px;margin-left:0.3em;"
    elif background == "sorry":
        background = "/static/yellow_roses_resized.png"
        color = (0,102,0)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "spider":
        background = "/static/spider_web_resized.jpg"
        color = (242,242,242)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "snow":
        background = "/static/snow_resized.jpg"
        print("BACKGROUND",background)
        color = (51,60,73)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "blues":
        background = "/static/blues_resized.jpg"
        color = (66,209,244)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;"
    elif background == "marble":
        background = "/static/marble_resized.jpg"
        color = (242,242,242)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "oldworld":
        background = "/static/old_world_resized.jpg"
        color = (99,77,20)
        style = "color:rgb" + str(color)+";font-size:"+ size + "px;margin-left:0.3em;"
    elif background == "dots":
        background = "/static/dots_resized.png"
        color = (66,243,255)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "waves":
        background = "/static/waves_resized.jpg"
        color = (230,230,255)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "clover":
        background = "/static/clover_resized.jpg"
        color = (204,255,179)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;margin-left:0.3em;"
    elif background == "thanks":
        background = "/static/thank_you_resized.jpg"
        color = (255,0,0)
        style = "color:rgb" + str(color) + ";font-size:" + size + "px;"
    print("BACKGROUND BEFORE STRIP",background)
    im = background.replace('/static/','')
    print("IM IN HELPER", im)

    return (background, style, im, color)
''