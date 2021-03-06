import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from resizeimage import resizeimage


# def image_sizing(im):
#     fd_img = open(im,'r')
#     img = Image.open(fd_img)
#     img = resizeimage.resize_thumbnail(img,[100,100])
#     img.save(im,img.format)
#     width, height = img.size
#     print(width,height)
#     print im
#     fd_img.close()
#     return im

# def image_sizing2(im):
#     basewidth = 300
#     img = Image.open(im)
#     wpercent = (basewidth/float(img.size[0]))
#     hsize = int((float(img.size[1]) * float(wpercent)))
#     img = img.resize((basewidth, hsize),PIL.Image.ANTIALIAS)
#     img.save(im)
def resize_and_crop(img_path, modified_path, size, crop_type='top'):
    """
    Resize and crop an image to fit the specified size.

    args:
    img_path: path for the image to resize.
    modified_path: path to store the modified image.
    size: `(width, height)` tuple.
    crop_type: can be 'top', 'middle' or 'bottom', depending on this
    value, the image will cropped getting the 'top/left', 'middle' or
    'bottom/right' of the image to fit the size.
    raises:
    Exception: if can not open the file in img_path of there is problems
    to save the image.
    ValueError: if an invalid `crop_type` is provided.
    """
    # If height is higher we resize vertically, if not we resize horizontally
    img = Image.open(img_path)
    # Get current and desired ratio for the images
    img_ratio = img.size[0] / float(img.size[1])
    ratio = size[0] / float(size[1])
    #The image is scaled/cropped vertically or horizontally depending on the ratio
    if ratio > img_ratio:
        img = img.resize((size[0], int(round(size[0] * img.size[1] / img.size[0]))),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, img.size[0], size[1])
        elif crop_type == 'middle':
            box = (0, int(round((img.size[1] - size[1]) / 2)), img.size[0],
                int(round((img.size[1] + size[1]) / 2)))
        elif crop_type == 'bottom':
            box = (0, img.size[1] - size[1], img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    elif ratio < img_ratio:
        img = img.resize((int(round(size[1] * img.size[0] / img.size[1])), size[1]),
            Image.ANTIALIAS)
        # Crop in the top, middle or bottom
        if crop_type == 'top':
            box = (0, 0, size[0], img.size[1])
        elif crop_type == 'middle':
            box = (int(round((img.size[0] - size[0]) / 2)), 0,
                int(round((img.size[0] + size[0]) / 2)), img.size[1])
        elif crop_type == 'bottom':
            box = (img.size[0] - size[0], 0, img.size[0], img.size[1])
        else :
            raise ValueError('ERROR: invalid value for crop_type')
        img = img.crop(box)
    else :
        img = img.resize((size[0], size[1]),
            Image.ANTIALIAS)

    # If the scale is the same, we do not need to crop
    img.save(modified_path)


resize_and_crop("spider_web.jpg","spider_web_resized.jpg",(300,150),"middle")
resize_and_crop("floral-fabric-background-pattern.jpg","floral-fabric-background-pattern_resized.jpg",(300,150),"middle")
resize_and_crop("paisley.jpg","paisley_resized.jpg",(300,150),"middle")
resize_and_crop("yellow_roses.png","yellow_roses_resized.png",(300,150),"middle")
resize_and_crop("cyclist.jpg","cyclist_resized.jpg",(300,150),"middle")
resize_and_crop("blues.jpg","blues_resized.jpg",(300,150),"middle")
resize_and_crop("bridge.jpeg","bridge_resized.jpeg",(300,150),"middle") 
resize_and_crop("dots.png","dots_resized.png",(300,150),"middle")
resize_and_crop("marble.jpg","marble_resized.jpg",(300,150),"middle")
resize_and_crop("old_world.jpg","old_world_resized.jpg",(300,150),"middle")
resize_and_crop("snow.jpg","snow_resized.jpg",(300,150),"middle")
resize_and_crop("thank_you.jpg","thank_you_resized.jpg",(300,150),"middle")
resize_and_crop("waves.jpg","waves_resized.jpg",(300,150),"middle")
resize_and_crop("clover.jpg","clover_resized.jpg",(300,150),"middle")
resize_and_crop("birthday.jpg","birthday_resized.jpg",(300,150),"middle")