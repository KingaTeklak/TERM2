#!/usr/bin/env python
import sys
from PIL import Image


big_image = sys.argv[1]
small_image = sys.argv[3]
image_parameter = sys.argv[2]

#image_path = "C:/Users/kinga/Desktop/studia/SEM2/PROGRAMOWANIE/PICTURE.jpg"
#image_save_path = "C:/Users/kinga/Desktop/studia/SEM2/PROGRAMOWANIE/SMALL_PICTURE.JPG"
#image_parameter = 20


img = Image.open(big_image)
img.show()
new_width = int(float(img.size[0])/float(image_parameter))
new_high = int(float(img.size[1])/float(image_parameter))
new_img = img.resize((new_width, new_high), Image.ANTIALIAS)
new_img.show()
new_img.save(small_image)
