from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from startup import XStart
from pi4 import PI4
from pi_logo import PI4Logo


def main():
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    
    start = XStart(device, 0.1)
    seq = [start.verlined, start.verlineu, start.verlined_reverse, start.verlined_reverseu]
    
    pi_logo = PI4Logo(device, 1) 
    pi_logo.draw_logo()
    count = 0
    while True:
        for func in seq:
            func()
            count += 1
        if count == 1:
            continue
        

        raspi = PI4(device, 2)
        raspi.pi4()

        break
    
if __name__ == "__main__":
    main()