# pi-epaper
my files for [waveshare epaper display 2.13in](https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT)

The Raspberry Pi GPIO pinout guide: https://pinout.xyz/pinout/213_inch_e_paper_phat#


**"imagefont.truetype() - cannot open resource" error**


To fix the issue you can use the default fonts from the raspberry pi's Font folder i.e, /usr/share/fonts/
for example: if you want to use FreeSans.ttf(/usr/share/fonts/truetype/freefont/FreeSans.ttf)
    
    font = ImageFont.truetype('FreeSans.ttf', 24)

If you want to use your own font copy the .ttf font file to '/usr/share/fonts/truetype'

body = ImageFont.truetype(os.path.join(pic_dir, 'AvenirNext.ttc'), 18, index=5)

Index of Avenir Next font:
    0 Medium  
    1 Regular  
    2 Ultra Light  
    3 Italic  
    4 Medium Italic  
    5 Ultra Light Italic  
    6 Bold  
    7 Demi Bold  
    8 Heavy  
    9 Bold Italic  
    10 Demi Bold Italic  
    11 Heavy Italic  
