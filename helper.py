
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
        length = len(line)
        if length > max_length:
            max_length = length
    print("MAX LENGTH ",max_length,"NUm lines ",num_lines)
    length = max_length
    fontsize = 1
    font = ImageFont.truetype("Milkshake.ttf", fontsize)
    if num_lines == 1 and length <= 5:
        multiplier = 1
    elif num_lines == 1 and length > 5:
        multiplier = .90
    elif num_lines == 2:
        multiplier = 1.5
    elif num_lines >= 3 and length < 10:
        multiplier = .80
    elif num_lines >= 3 and length < 24:
        multiplier = 1.6
    else:
        multiplier = 1.8
    if num_lines == 1:
        coordinates = (0, 0)
    elif num_lines == 2:
        coordinates = (20, 1)
    elif num_lines == 3:
        coordinates = (20, 20)
    elif num_lines == 4:
        coordinates = (20, 15)
    else:
        coordinates = (35, 1)
    print("multiplier ",multiplier)

    while font.getsize(txt)[0] < im.size[0]*multiplier and font.getsize(txt)[1] < im.size[1]*multiplier:
        fontsize += 1
        print(font.getsize(txt),im.size[0]*multiplier,im.size[1]*multiplier,num_lines)
        font = ImageFont.truetype("Milkshake.ttf", fontsize)
    fontsize -= 1
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