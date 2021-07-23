import argparse

from PIL import Image

parser = argparse.ArgumentParser()
parser.add_argument('-file', help='Имя файла', type=str)
parser.add_argument('-size', help='Размер пикселей', default=10, type=int)
args = parser.parse_args()


with Image.open(args.file) as image:
    image = image.resize(
        (image.size[0] // args.size, image.size[1] // args.size),
        Image.NEAREST
    ).resize(
        (image.size[0] * args.size, image.size[1] * args.size),
        Image.NEAREST
    )

    image.save('Pixel' + args.file)