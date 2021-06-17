#!/usr/bin/python

import os

from lib.waveshare_epd import epd2in13_V2
from PIL import Image, ImageDraw, ImageFont

data_dir = 'data'

try:
	#Display init, clear
	epaper = epd2in13_V2.EPD()
	print("init and clear")
	epaper.init(epaper.FULL_UPDATE)
	epaper.Clear(255)
	print("cleared")
	h = epaper.width
	w = epaper.height
  body = ImageFont.truetype(os.path.join(data_dir, 'Font.ttc'), 22)
	txt = Image.new('1', (w, h), 255)
	draw = ImageDraw.Draw(txt)
	draw.text((10,0), 'HELLO FRIEND', font=body, fill=0) # x-y axis '10' and '0'
	txt1 = txt.rotate(180) # use this only if you want to flip the screen upside down
	epaper.display(epaper.getbuffer(txt1))

except IOError as e:
	print(e)

except KeyboardInterrupt:
	print("ctrl+c")
	epd2in13_V2.epdconfig.module_exit()
	exit()
