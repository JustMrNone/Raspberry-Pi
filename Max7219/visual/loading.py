from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from time import sleep


class Xlines:
    def __init__(self, device, period):
        self.device = device
        self.period = period
        
    def verline(self):
        for x in range(8):
            with canvas(self.device) as draw:
                for y in range(x+1):
                    for i in range(8):
                        draw.point((i, i+y), fill="white")
            sleep(self.period) 
            
            
    def verlineu(self):
        for x in range(8):
            with canvas(self.device) as draw:
                for y in range(x+1):
                    for i in range(8):
                        draw.point((i, i-y), fill="white")
            sleep(self.period)

def main():
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    xlines = Xlines(device, 0.2)
    try:
        while True: 
            xlines.verline()
            xlines.verlineu()
            
    except KeyboardInterrupt:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="black", fill="black")

if __name__ == "__main__":
    main()