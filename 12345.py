from PIL import Image, ImageFilter

print('Здравствуйте. Перед Вами Минифотошоп.')
print(' Если вы хотите по взаомодействовать с ним напишите "да".')
print('А если нет, то "стоп".')
print('Ниже будут приведены фильтры, которыми Вы можете воспользоваться.')
b = ['размытие', 'негатив', 'высветление', 'чёрно-белое фото', 'изменение размера фото',
     'вырезание кусочка фото', 'сокращение или увеличение цветов в фото', 'поворачивание фото']
print(b)
a = input()
c = 0
while a.lower() != 'стоп' or a != '':
    print('Введите один фильтр, который вы хотите.')
    print('Если Вы забыли какие фильтры может выполнять программа напишите забыл/a')
    a = input()
    if a.lower() != 'стоп' and a != '':
        if 'забыл' in a:
            print(*b)
    else:
        break
    if c == 0:
        im = Image.open('image.jfif')
        c += 1
    else:
        im = Image.open('res.jfif')
    pixels = im.load()
    x, y = im.size
    if a.lower() == 'размытие':
        print('Введите глубину размытия')
        im2 = im.filter(ImageFilter.GaussianBlur(radius=int(input())))
        im2.save('res.jfif')
    if a.lower() == 'негатив':
        def image_filter(pixels, x, y):
            for i in range(x):
                for j in range(y):
                    r, g, b = pixels[i, j]
                    pixels[i, j] = 255 - r, 255 - g, 255 - b
            im.save('res.jfif')


        image_filter(pixels, x, y)
    if a.lower() == 'высветление':
        def curve(pixel):
            r, g, b = pixel
            brightness = r + g + b if r + g + b > 0 else 1
            if brightness < 60:
                k = 60 / brightness
                return min(255, int(r * k ** 2)), \
                       min(255, int(g * k ** 2)), \
                       min(255, int(b * k ** 2))
            else:
                return r, g, b


        for i in range(x):
            for j in range(y):
                pixels[i, j] = curve(pixels[i, j])
        im.save('res.jfif')
    if a.lower() == 'чёрно-белое фото':
        for i in range(x):
            for j in range(y):
                r, g, b = pixels[i, j]
                bw = (r + g + b) // 3
                pixels[i, j] = bw, bw, bw
        im.save('res.jfif')
    if a.lower() == 'изменение размера фото':
        print('Введите длину и ширину картинки')
        d = int(input())
        e = int(input())
        im2 = im.resize((d, e))
        im2.save('res.jfif')
    if a.lower() == 'вырезание кусочка фото':
        print('Введите координаты левого верхнего пикселя и правого нижнего.'
              'Каждую координаты отдельно.')
        im2 = im.crop((int(input()), int(input()), int(input()), int(input())))
        im2.save('res.jfif')
    if a.lower() == 'сокращение или увеличение цветов в фото':
        print('Напишите кол-во цветов')
        im2 = im.quantize(int(input()))
        im2.save('res.jfif')
    if a.lower() == 'поворачивание фото':
        print('Введите число градусов, на которое Вы хотите повернуть фото.')
        r = int(input())
        if r == 90:
            im2 = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_90)
            im2.save('res.jfif')
        if r == 180:
            im2 = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_180)
            im2.save('res.jfif')
        if r == 270:
            im2 = im.transpose(Image.FLIP_LEFT_RIGHT).transpose(Image.ROTATE_270)
            im2.save('res.jfif')
