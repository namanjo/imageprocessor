from PIL import Image
from PIL import ImageFilter


#IMAGE TRANSFORMATIONS
def crop(pic):
    print("The size of pic is: " + str(pic.size))
    print("You have to give 4 coordinates to crop, i.e X coor & Y coor")
    area = []
    for i in range(1, 5):
        coordinate = int(input('Enter Point ' + str(i) + ": "))
        area.append(coordinate)
    cropped_image = pic.crop(area)
    return cropped_image


def rotations(pic):
    action = input("Rotate left, right, down, or u want to get the mirror effect?: ").lower()

    if action.startswith('l'):
        left = pic.transpose(Image.ROTATE_90)
        return left

    if action.startswith('r'):
        right = pic.transpose(Image.ROTATE_270)
        return right

    if action.startswith('d'):
        down = pic.transpose(Image.ROTATE_180)
        return down

    if action.startswith('m'):
        mirror_image = pic.transpose(Image.FLIP_LEFT_RIGHT)
        return mirror_image


def resize(pic):
    length, breadth = pic.size
    print("\nCurrently The Dimensions Of your Photo are, " + "Length: " + str(length) + ", Breadth: " + str(breadth))
    print('Now give the dimensions you want to resize the photo to')
    new_length = int(input("Enter the new length: "))
    new_breadth = int(input('Enter the new breadth: '))
    resize_image = pic.resize((new_length, new_breadth))
    return resize_image


#IMAGE EDITING
def cool_filters(pic, cool_inp):

    r, g, b = pic.split()

    if cool_inp == 'bw1':
        black_white_1 = pic.convert('L')
        return black_white_1

    if cool_inp == 'bw2':
        return r

    if cool_inp == 'bw3':
        return g

    if cool_inp == 'bw4':
        return b

    if cool_inp == 'blur':
        blur = pic.filter(ImageFilter.BLUR)
        return blur

    if cool_inp == 'sharpen':
        sharpen = pic.filter(ImageFilter.DETAIL)
        return sharpen

    if cool_inp == 'outlines':
        outline = pic.filter(ImageFilter.FIND_EDGES)
        return outline


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
        return background_pic

    if length < breadth:
        measure = breadth
        background_resize = pic.resize((measure, measure))
        background_pic = background_resize.filter(ImageFilter.BLUR)
        var1 = measure - length
        coorX1 = var1//2
        coorX2 = coorX1 + length
        area = (coorX1, 0, coorX2, measure)
        background_pic.paste(pic, area)
        return background_pic


def choice():
    choice = input("Want to do it again..? ").lower()
    if choice.startswith('y'):
        return True
    else:
        return False


photo = Image.open('sanfran.png')  #pre loaded images (one of these images will be passed as a parameter in the above functions)

print('\nWelcome to Image Editor and processor.\n')


while True:

    op = int(input('Press 1 to crop, 2 to rotate, 3 to resize,\n4 to Add Effects & 5 to Square Fit: '))

    if op == 1:
        while True:
            photo = crop(photo)
            photo.show()
            if not choice():
                break

    if op == 2:
        while True:
            photo = rotations(photo)
            photo.show()
            if not choice():
                break

    if op == 3:
        while True:
            photo = resize(photo)
            photo.show()
            if not choice():
                break

    if op == 4:
        while True:
            try:
                cool_inp = input("Available filters: bw1, bw2, bw3, bw4, blur, sharpen & outlines, Choose 1: ")
                pic = cool_filters(photo, cool_inp)
                pic.show()
                if not choice():
                    break
            except AttributeError:
                print("Enter a valid filter name")
                continue
        photo = pic

    if op == 5:
        photo = square_fit(photo)
        photo.show()

    user_choice = input("Done all your edits?: ").lower()
    if user_choice.startswith('y'):
        photo.save('edited_pic.jpg')
        print("The Edited photo has been saved.")
        break
    else:
        continue
