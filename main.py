from PIL import Image
import os, sys


## print image format, mode , size






f, e = os.path.splitext("jazz.jpeg")
im = Image.open("jazz.jpeg")

outfile = f + ".png"
if im != outfile:
    try:

        im.save(outfile)
    except OSError:
        print("cannot convert", im)

#im.show()

print("image format{}, image mode {}, image size {}".format(im.format, im.mode, im.size))

out = im.resize((128, 128))
out = im.rotate(45) # degrees counter-clockwise
#out.show()
crop_box = (0, 100, 100, 200)
region = im.crop(crop_box)
#region.show()

region = region.transpose(Image.ROTATE_90)
im.paste(region, crop_box)
im.show()