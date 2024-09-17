from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from time import sleep

class XStart:
    def __init__(self, device, period=0.5):
        self.device = device
        self.period = period
        
        
    def verlined(self):
        for x in range(8):
            with canvas(self.device) as draw:
                for i in range(8):
                    draw.point((i, i+x), fill="white")
            sleep(self.period) 
            
    def verlineu(self):
        for x in range(8):
            with canvas(self.device) as draw:
                for i in range(8):
                    draw.point((i, i-x), fill="white")
            sleep(self.period)
            
            
    def verlined_reverse(self):

        for x in range(8):
            with canvas(self.device) as draw:
                for i in range(8):
                    draw.point((i, 7 - (i - x)), fill="white")
            sleep(self.period)  
            
    def verlined_reverseu(self):
        for x in range(8):
            with canvas(self.device) as draw:
                for i in range(8):
                    draw.point((i, 7 - (i + x)), fill="white")
            sleep(self.period)  
        
def main():
        # Initialize the device
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    start = XStart(device, 0.2)
    seq = [start.verlined(), start.verlineu(), start.verlined_reverse(), start.verlined_reverseu()]

    while True:
        for func in seq:
            func()
        

if __name__ == "__main__":
    main()



"""
def verlined():
    # Create a separate drawing context for the whole process
    for x in range(8):
        with canvas(device) as draw:
            for i in range(8):
                draw.point((x, i+x), fill="white")
        sleep(0.5)  # Wait for 0.5 seconds before drawing the next line
        
"""