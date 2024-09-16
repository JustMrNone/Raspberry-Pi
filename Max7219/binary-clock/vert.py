from luma.led_matrix.device import max7219 
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import time 

serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial)

def light_upvert(device, col, state):
    with canvas(device) as draw:
        for x in range(1):
            for y in range(8):
                if state:
                    draw.point((col, y), fill="red")
                else:
                    draw.point((col, y), fill="black")

light_upvert(device, 0, True)
time.sleep(3)