from PIL import Image
from PIL import ImageColor
import binascii
import optparse

def rgb2hex(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
	return ImageColor.getcolor(hexcode, "RGB")
print(rgb2hex(12,12,12))
print(hex2rgb('#0c0c0c'))
