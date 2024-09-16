from alphabet import Alphabat
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
import sys
from time import sleep


def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial, cascaded=1)
    alpha = Alphabat(device)
    
    if len(sys.argv) > 1:
        text = sys.argv[1]
        alpha.scroll_text(text.upper(), delay=0.1, char_spacing=1) 
    else:
        text = input("Enter any text: ")
        alpha.scroll_text(text.upper(), delay=0.1, char_spacing=1) 
    
if __name__ == "__main__":
    main()