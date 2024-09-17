from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep


class PI4:
    def __init__(self, device, period):
        self.device = device 
        self.period = period
        
    def pi4(self):

        P = [(0, 2), (0, 3), (0, 4), (0, 5), (1, 2), (2, 2), (2, 3), (2, 4), (1, 4)]
        i = [(3, 2) ,(3, 3) ,(3, 4), (3, 5)]
        four = [(5, 2), (5, 3), (5, 4), (6, 4), (7, 4), (7, 3), (7, 2), (7, 5)]
        with canvas(self.device) as draw:
            draw.point(P+i+four, fill="white")
        sleep(self.period)        
        
def main():
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    rasppi4 = PI4(device, 1)
    rasppi4.pi4()
    

    
if __name__ == "__main__":
    main()