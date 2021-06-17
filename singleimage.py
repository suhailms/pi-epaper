import os
#import time

from lib.waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

#data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'data')

try:
	print("Kitty incoming...")
	epaper = epd2in13_V2.EPD()
	epaper.init(epaper.FULL_UPDATE)
	epaper.Clear(255)
	#print("cleared")
	h = epaper.width
	w = epaper.height
	image = Image.new('1', (w, h), 255)

	#showing image
	#time.sleep(3)
	kitty = Image.open('data/kitty.png')
	kitty = kitty.transpose(Image.ROTATE_180) #use this only if you want to flip the screen upside down
	image.paste(kitty, (0,0))
	epaper.display(epaper.getbuffer(image))

except IOError as e:
	print(e)

except KeyboardInterrupt:
	print("ctrl+c")
	epd2in13_V2.epdconfig.module_exit()
	exit()
