from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep

serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1)

with canvas(device) as draw:
    draw.point((0, 4), fill="white")
    
sleep(2)



'''
            bit_positions = {
                1: [(1, 4)],  # 0001
                2: [(0, 4)],  # 0010
                3: [(1, 4), (0, 4)],  # 0011
                4: [(1, 3)],  # 0100
                5: [(1, 3), (0, 4)],  # 0101
                6: [(1, 3), (1, 4)],  # 0110
                7: [(1, 3), (1, 4), (0, 4)],  # 0111
                8: [(0, 3)],  # 1000
                9: [(0, 3), (1, 4)],  # 1001
                10: [(0, 3), (1, 3)],  # 1010
                11: [(0, 3), (1, 3), (1, 4)],  # 1011
                12: [(0, 3), (0, 4)]  # 1100
        }
        
'''