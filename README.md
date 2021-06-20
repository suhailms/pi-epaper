# pi-epaper
my files for [waveshare epaper display 2.13in](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT)

The Raspberry Pi GPIO pinout guide: https://pinout.xyz/pinout/213_inch_e_paper_phat#


**"imagefont.truetype() - cannot open resource" error**


To fix the issue you can use the default fonts from the raspberry pi's Font folder i.e, /usr/share/fonts/
for example: /usr/share/fonts/truetype/freefont/FreeSans.ttf
If you want to use your own font copy the .ttf font file to '/usr/share/fonts/truetype'
