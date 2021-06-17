#!/usr/bin/python

import logging
from lib.waveshare_epd import epd2in13_V2

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("TASK: CLEAR DISPLAY")
    
    epd = epd2in13_V2.EPD()
    logging.info("CLEARING DISPLAY")
    epd.init(epd.FULL_UPDATE)
    epd.Clear(0xFF)
    
    logging.info("Going to Sleep, See Yaa..")
    epd.sleep()
    
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl+c: FIRED")
    epd2in13_V2.epdconfig.module_exit()
    exit()
