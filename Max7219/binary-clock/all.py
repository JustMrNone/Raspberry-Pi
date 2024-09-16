from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)

try:
    while True:
        with canvas(device) as draw:
            for i in range(8):
                for j in range(8):
                        draw.point((i, j), fill="white")
except KeyboardInterrupt:
        with canvas(device) as draw:
            for i in range(8):
                for j in range(8):
                        draw.point((i, j), fill="black")