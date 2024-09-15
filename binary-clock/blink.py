from luma.led_matrix.device import max7219 
from luma.core.interface.serial import spi
from luma.core.render import canvas
import time 

def main():
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    blink(device, 0, 0.5)


def light_up(device, row, state):
    with canvas(device) as draw:
        for x in range(8):
            if state:
                draw.point((x, row), fill="red")
            else:
                draw.point((x, row), fill="black")

def blink(device, row, interval=0.1):
    try:
        while True:
            light_up(device, row, True)

            time.sleep(interval)

            light_up(device, row, False)

            time.sleep(interval)
    except KeyboardInterrupt:
        with canvas(device) as draw:
            draw.rectangle(device.bounding_box, outline="black", fill="black")



if __name__ == "__main__":
    main()