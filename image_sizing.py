def image_sizing(im):
    fd_img = open(im,'r')
    img = Image.open(fd_img)
    img = resizeimage.resize_thumbnail(img,[500,500])
    img.save(im,img.format)
    width, height = img.size
    print(width,height)
    fd_img.close()
    return im
