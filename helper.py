
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from resizeimage import resizeimage
import pyimgur


def make_jpg(im, color, message):
    lines = message.splitlines()
    max_length = 0
    for line in lines:
        if len(line.strip()) > max_length:
            max_length = len(line.strip())
    im = Image.open(im)
    fontsize = 40
    font = ImageFont.truetype("Milkshake.ttf", fontsize)
    img = Image.new("RGBA", (1, 1))
    draw = ImageDraw.Draw(img)
    textsize = draw.textsize(message, font)
    A = textsize[0] + 30
    B = textsize[1] + 30
    textsize = (A, B)
    im = im.resize(textsize, PIL.Image.ANTIALIAS)    
    draw = ImageDraw.Draw(im)
    if max_length <= 5:
        coordinates = (6, 1)
    elif max_length <= 10:
        coordinates = (10, 5)
    else:
        coordinates = (20, 20)

    draw.text(coordinates, message, color, font)
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