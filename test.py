from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)

#font = ImageFont.load_default()

try:
    while True:
        for j in range(100):
            with canvas(device) as draw:
                for i in range(8):
                    draw.point((i, 0), fill="red")
            sleep(0.1)
        sleep(0.5)

except KeyboardInterrupt:
    with canvas(device) as draw:
        draw.rectangle(device.bounding_box, outline="black", fill="black")


print("test complete")