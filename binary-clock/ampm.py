from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)


class AMPM:
    def __init__(self):
        pass
    
    def am(self):
        while True:
            with canvas(device) as draw:
                draw.point((3, 0), fill="white")
                draw.point((4, 0), fill="white")
    
    def pm(self):
        while True:
            with canvas(device) as draw:
                draw.point((3, 7), fill="white")
                draw.point((4, 7), fill="white")
    
            
            



sleep(10)