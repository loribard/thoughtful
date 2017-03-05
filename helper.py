
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from resizeimage import resizeimage
import pyimgur


def make_jpg(im, color, message):
    im = Image.open(im)
    draw = ImageDraw.Draw(im)
    txt = message
    lines = message.splitlines()
    num_lines = len(lines)
    max_length = 0
    for line in lines:
        length = len(line.strip())
        if length > max_length:
            max_length = length
    print("MAX LENGTH ",max_length,"NUm lines ",num_lines)
    length = max_length
    fontsize = 1
    font = ImageFont.truetype("Milkshake.ttf", fontsize)
    if num_lines == 1:
        if length <= 5:
            fontsize = 100
            coordinates = (20, 0)
        elif length > 5 and length <= 10:
            fontsize = 65
            coordinates = (2, 25)
        elif length > 10 and length < 15:
            fontsize = 50
            coordinates = (3, 50)
        else:
            fontsize = 20
            coordinates = (3,50)
    elif num_lines == 2:
        if length <= 5:
            fontsize = 50
            coordinates = (20, 0)
        elif length > 5 and length <= 10:
            fontsize = 65
            coordinates = (3, 0)
        elif length > 10 and length < 15:
            fontsize = 50
            coordinates = (3, 35)
        else:
            fontsize = 25
            coordinates = (3,25)
    elif num_lines == 3:
        if length <= 5:
            fontsize = 50
            coordinates = (5, 0)
        elif length <= 10:
            fontsize = 35
            coordinates = (5,0)
        else:
            fontsize = 30
            coordinates = (7, 15)
    elif num_lines == 4:
        if length <= 10:
            fontsize = 30
            coordinates = (20, 0)
        else:
            fontsize = 25
            coordinates = (5, 0)
    else:
        fontsize = 20
        coordinates = (5, 0)

   
    font = ImageFont.truetype("Milkshake.ttf", fontsize)
    draw.text(coordinates, txt, color, font=font)
    im.save('testing.jpg') 
    return im


def make_url(image): 
    CLIENT_ID = "ffa486c0af07526"
    PATH = "testing.jpg"
    im = pyimgur.Imgur(CLIENT_ID)
    uploaded_image = im.upload_image(PATH)
    return uploaded_image.link


def image_sizing(im):
    fd_img = open(im, 'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_thumbnail(img, [500, 500])
    img.save(im, img.format)
    width, height = img.size
    print(width, height)
    fd_img.close()
    return im


def background_process(background,):

    if background == "floral":
        background = "/static/floral-fabric-background-pattern_resized.jpg"
        color = (0, 102, 0)
    elif background == "paisley":
        background = "/static/paisley_resized.jpg"
        color = (102, 0, 102)
    elif background == "sorry":
        background = "/static/yellow_roses_resized.png"
        color = (0, 102, 0)
    elif background == "spider":
        background = "/static/spider_web_resized.jpg"
        color = (242, 242, 242)      
    elif background == "snow":
        background = "/static/snow_resized.jpg"
        color = (51, 60, 73)       
    elif background == "blues":
        background = "/static/blues_resized.jpg"
        color = (66, 209, 244)       
    elif background == "marble":
        background = "/static/marble_resized.jpg"
        color = (242, 242, 242)       
    elif background == "oldworld":
        background = "/static/old_world_resized.jpg"
        color = (99, 77, 20)        
    elif background == "dots":
        background = "/static/dots_resized.png"
        color = (0, 153, 255)       
    elif background == "waves":
        background = "/static/waves_resized.jpg"
        color = (230, 230, 255)
    elif background == "clover":
        background = "/static/clover_resized.jpg"
        color = (204, 255, 179)       
    elif background == "birthday":
        print("BIRTHDAY")
        background = "/static/birthday_resized.jpg"
        color = (255, 255, 255)
    im = background.replace('/static/', '')
    return (background, im, color)
''