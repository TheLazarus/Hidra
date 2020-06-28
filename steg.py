from PIL import Image
from PIL import ImageColor
import binascii
import optparse

def rgb2hex(r, g, b):
	return '#{:02x}{:02x}{:02x}'.format(r, g, b)

def hex2rgb(hexcode):
	return ImageColor.getcolor(hexcode, "RGB")

def str2bin(message):
	binary = bin(int(binascii.hexlify(message.encode()), 16))
	return binary[2:]	

def bin2str(binary):
	binary = -len(binary) % 8 * '0' + binary
	bytes = (binary[i:i+8] for i in range(0, len(binary), 8))
	message = ''.join(chr(int(char, 2)) for char in bytes)
	return message
	
def encode(hexcode, digit):
	if hexcode[-1] in ('0', '1', '2', '3', '4' , '5'):
		 hexcode = hexcode[:-1] + digit
		 return hexcode
	else:
		return None

def decode(hexcode):
	if hexcode[-1] in ('0', '1'):
		return hexcode[-1]
	else:
		return None

def hide(filename, message):
	imageFile = Image.open(filename)
	binary = str2bin(message) + '1111111111111110'
	imageFile = imageFile.convert('RGBA')
	if imageFile.mode in ('RGBA'):
		data = imageFile.getdata()
		newData = []
		digit = 0
		temp = ''
		for item in data:
			if (digit < len(binary)):
				newpix = encode(rgb2hex(item[0], item[1], item[2]), binary[digit])
				if newpix == None:
					newData.append(item)
				else:
					r, g, b = hex2rgb(newpix)
					newData.append((r,g,b, 255))
					digit += 1
			else:
				newData.append(item)
		imageFile.putdata(newData)
		imageFile.save(filename, "PNG")
		return "Completed!"
def retr(filename):
	imageFile = Image.open(filename)
	binary = ''
	
	if img.mode in ('RGBA'):
		img = img.convert('RGBA')
		data = img.getdata()
		
		for item in data:
			digit = decode(rgb2hex(item[0], item[1], item[2]))
			if digit == None:
				pass
			else:
				binary = binary + digit
				if(binary[-16:] == '1111111111111110'):
					print("Success")
					return bin2str(binary[:-16])
		return bin2str(binary)
	return "Incorrect Image Mode, couldn't retrieve"

def Main():
	parser = optparse.OptionParser('usage %prog '+\
		'-e/-d <target file>')
	parser.add_option('-e', dest='hide', type='string', \
		help='target picture path to hide')
	parser.add_option('-d', dest='retr', type='string', \
		help='target picture path to retrieve text')
	(options, args) = parser.parse_args()
	if(options.hide != None):
		text = input('Enter a message to hide: ')
		print hide(options.hide, text)
	elif(options.retr != None):
		print retr(options.retr)
	else:
		print parser.usage
		exit(0)
if __name__ == '__main__':
	 Main()	
print(rgb2hex(13, 13, 13))
print(hex2rgb('#0c0c0c'))
print(str2bin('hello'))
print(bin2str('110100001100101011011000110110001101111'))



