from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)

with canvas(device) as draw:
    draw.rectangle(device.bounding_box, outline="black", fill="black")