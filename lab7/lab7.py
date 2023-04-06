

from PIL import  Image, ImageFilter

def zadach1():

    filename = "3.jpg"
    with Image.open(filename)as  img:
        img.load()

    img.show()
    widht,height = img.size

    format = img.format


    mode = img.mode

    print('Ширина: ', widht)
    print('Высота: ',height)
    print('Формат: ',format)
    print('цветовая модель: ',mode)


def zadach2():
    filename = "2.jpg"
    with Image.open(filename)as img:
        img.load()

    new_img = img.resize((img.width // 3, img.height // 3))

    new_img.save('resized_2.jpg')

    converted_img = img.transpose(Image.FLIP_TOP_BOTTOM)
    converted_img .save('image_flip_top.jpg')
    converted_img = img.transpose(Image.FLIP_LEFT_RIGHT)
    converted_img.save('image_flip.jpg')

def zadach3():

    spisok = ["1.jpg","2.jpg","3.jpg","4.jpg"]

    for file in spisok:
         with Image.open(file) as img:
             img.load()
             new_img = img.filter(ImageFilter.EMBOSS)
             new_img.show()
             new_img.save("New_"+ file)
def zadach4():
    filename = Image.open("4.jpg")
    watMark  =Image.open("watermark.png")

    watMark = watMark.resize([200,200])
    filename.paste(watMark,[200,200],mask=watMark)
    filename.show()
zadach4()












