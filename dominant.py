from PIL import Image
import argparse
parser = argparse.ArgumentParser()

parser.add_argument('-f', '--file',  dest='filename',  help='input file')
parser.add_argument('-c', '--colors', dest='colors', type=int, default=3, help='number of colors')
args = parser.parse_args()

filename = args.filename
colors = args.colors

im = Image.open(filename)
im.show()
out = im.convert("P", palette=Image.ADAPTIVE, colors=colors).convert('RGB')
out.show()

for count, rgb_tuple in out.getcolors():
    print "Count:{} rgb:#{:02x}{:02x}{:02x}".format(count, *rgb_tuple)
    color_image = Image.new("RGB", (200, 200), rgb_tuple)
    color_image.show()
