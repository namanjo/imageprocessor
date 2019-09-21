from PIL import Image
from PIL import ImageFilter

sanfran = Image.open('sanfran.png')
ryan = Image.open('ryan.png')


def crop(pic):
    print("The size of pic is: " + str(pic.size))
    print("You have to give 4 coordinates to crop, i.e X coor & Y coor")
    area = []
    for i in range(1, 5):
        coordinate = int(input('Enter Point ' + str(i) + ": "))
        area.append(coordinate)
    cropped_image = pic.crop(area)
    cropped_image.show()


def rotations(pic, action):
    if action is 'left':
        left = pic.transpose(Image.ROTATE_90)
        left.show()

    if action is 'right':
        right = pic.transpose(Image.ROTATE_270)
        right.show()

    if action is 'down':
        down = pic.transpose(Image.ROTATE_180)
        down.show()

    if action is 'mirror':
        mirror_image = pic.transpose(Image.FLIP_LEFT_RIGHT)
        mirror_image.show()


def resize(pic):
    length, breadth = pic.size
    print("Currently The Dimensions Of your Photo are, " + "Length: " + str(length) + ", Breadth: " + str(breadth))
    print('Now give the dimensions you want to resize the photo')
    new_length = int(input("Enter the new length: "))
    new_breadth = int(input('Enter the new breadth: '))
    resize_image = pic.resize((new_length, new_breadth))
    resize_image.show()


def cool_filters(pic, type):
    r, g, b = pic.split()

    if type is 'bw1':
        black_white_1 = pic.convert('L')
        black_white_1.show()

    if type is 'bw2':
        r.show()

    if type is 'bw3':
        g.show()

    if type is 'bw4':
        b.show()

    if type is 'blur':
        blur = pic.filter(ImageFilter.BLUR)
        blur.show()

    if type is 'sharpen':
        sharpen = pic.filter(ImageFilter.DETAIL)
        sharpen.show()

    if type is 'outlines':
        outline = pic.filter(ImageFilter.FIND_EDGES)
        outline.show()


def square_fit(pic):
    length, breadth = pic.size

    if length > breadth:
        measure = length
        background_resize = pic.resize((measure, measure))
        background_pic = background_resize.filter(ImageFilter.BLUR)
        var1 = measure - breadth
        coorX1 = var1 // 2
        coorX2 = coorX1 + breadth
        area = (0, coorX1, measure, coorX2)
        background_pic.paste(pic, area)
        background_pic.show()

    if length < breadth:
        measure = breadth
        background_resize = pic.resize((measure, measure))
        background_pic = background_resize.filter(ImageFilter.BLUR)
        var1 = measure - length
        coorX1 = var1//2
        coorX2 = coorX1 + length
        area = (coorX1, 0, coorX2, measure)
        background_pic.paste(pic, area)
        background_pic.show()
