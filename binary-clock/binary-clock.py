from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial)
    light(device, 0, 4)

def rowss(device, rownum, colnum, state):
   
    with canvas(device) as draw:
        if state:
            draw.point((colnum, rownum), fill="white")
        else:
            draw.point((colnum, rownum), fill="black")

def light(device, col, row):
    try:
        # Turn on LEDs without using an infinite loop
        with canvas(device) as draw:
            for i in range(8):
                draw.point((i, row), fill="white")      # Turn on the LED at (col, i)
                draw.point((i, row-1), fill="white")    # Turn on the LED at (col-1, i)

        # Keep the display static by adding a sleep loop
        while True:
            sleep(1)  # Keep the LEDs on by sleeping in the loop

    except KeyboardInterrupt:
        # Clear the display when interrupted
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="black", fill="black")
               
if __name__ == "__main__":
    main()
