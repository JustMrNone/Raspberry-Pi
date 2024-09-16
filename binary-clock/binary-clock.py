from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep
from datetime import datetime


class Time:
    def __init__(self):
        pass
    
    def get_current_time_12_hour():
    # Get the current time
        now = datetime.now()
    
    # Extract hours, minutes, and seconds
        hour = now.hour
        minute = now.minute
        second = now.second
    
    # Convert to 12-hour format
        am_pm = 'AM' if hour < 12 else 'PM'
        hour_12 = hour % 12
        hour_12 = 12 if hour_12 == 0 else hour_12  # Handle midnight case

        return hour_12, minute, second, am_pm

class BinaryClock(Time):
    def __init__(self, device):
        self.device = device
        self.hour, self.minute, self.second, self.am_pm = Time.get_current_time_12_hour()
    def update(self):
        self.hour, self.minute, self.second, self.am_pm = Time.get_current_time_12_hour()
        
    def AMPM(self):
        with canvas(self.device) as draw:
            if self.am_pm == "AM":
                draw.point((3, 0), fill="white")
                draw.point((4, 0), fill="white")
            elif self.am_pm == "PM":
                draw.point((3, 7), fill="white")
                draw.point((4, 7), fill="white")
    
    def rowss(self, rownum, colnum, state):
   
        with canvas(self.device) as draw:
            if state:
                draw.point((colnum, rownum), fill="white")
            else:
                draw.point((colnum, rownum), fill="black")
 
                     
    def hours(self):
        with canvas(self.device) as draw:
        # Define the bit positions for each number from 1 to 12
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
                10: [(0, 3), (0, 4)],  # 1010
                11: [(0, 3), (0, 4), (1, 4)],  # 1011
                12: [(0, 3), (1, 3)]  # 1100
        }

        # Get the bit positions for the current hour
            positions = bit_positions.get(self.hour, [])

        # Light up the corresponding points on the LED matrix
            for pos in positions:
                draw.point(pos, fill="white")

    def minutes(self):
        with canvas(self.device) as draw:
            bit_positions_minutes = {
            1: [(4, 4)],  # 000001
            2: [(3, 4)],  # 000010
            3: [(4, 4), (3, 4)],  # 000011
            4: [(2, 4)],  # 000100
            5: [(4, 4), (2, 4)],  # 000101
            6: [(3, 4), (2, 4)],  # 000110
            7: [(4, 4), (3, 4), (2, 4)],  # 000111
            8: [(4, 3)],  # 001000
            9: [(4, 4), (4, 3)],  # 001001
            10: [(3, 4), (4, 3)],  # 001010
            11: [(4, 4), (3, 4), (4, 3)],  # 001011
            12: [(2, 4), (4, 3)],  # 001100
            13: [(4, 4), (2, 4), (4, 3)],  # 001101
            14: [(3, 4), (2, 4), (4, 3)],  # 001110
            15: [(4, 4), (3, 4), (2, 4), (4, 3)],  # 001111
            16: [(3, 3)],  # 010000
            17: [(4, 4), (3, 3)],  # 010001
            18: [(3, 4), (3, 3)],  # 010010
            19: [(4, 4), (3, 4), (3, 3)],  # 010011
            20: [(2, 4), (3, 3)],  # 010100
            21: [(4, 4), (2, 4), (3, 3)],  # 010101
            22: [(3, 4), (2, 4), (3, 3)],  # 010110
            23: [(4, 4), (3, 4), (2, 4), (3, 3)],  # 010111
            24: [(4, 3), (3, 3)],  # 011000
            25: [(4, 4), (4, 3), (3, 3)],  # 011001
            26: [(3, 4), (4, 3), (3, 3)],  # 011010
            27: [(4, 4), (3, 4), (4, 3), (3, 3)],  # 011011
            28: [(2, 4), (4, 3), (3, 3)],  # 011100
            29: [(4, 4), (2, 4), (4, 3), (3, 3)],  # 011101
            30: [(3, 4), (2, 4), (4, 3), (3, 3)],  # 011110
            31: [(4, 4), (3, 4), (2, 4), (4, 3), (3, 3)],  # 011111
            32: [(2, 3)],  # 100000
            33: [(4, 4), (2, 3)],  # 100001
            34: [(3, 4), (2, 3)],  # 100010
            35: [(4, 4), (3, 4), (2, 3)],  # 100011
            36: [(2, 4), (2, 3)],  # 100100
            37: [(4, 4), (2, 4), (2, 3)],  # 100101
            38: [(3, 4), (2, 4), (2, 3)],  # 100110
            39: [(4, 4), (3, 4), (2, 4), (2, 3)],  # 100111
            40: [(4, 3), (2, 3)],  # 101000
            41: [(4, 4), (4, 3), (2, 3)],  # 101001
            42: [(3, 4), (4, 3), (2, 3)],  # 101010
            43: [(4, 4), (3, 4), (4, 3), (2, 3)],  # 101011
            44: [(2, 4), (4, 3), (2, 3)],  # 101100
            45: [(4, 4), (2, 4), (4, 3), (2, 3)],  # 101101
            46: [(3, 4), (2, 4), (4, 3), (2, 3)],  # 101110
            47: [(4, 4), (3, 4), (2, 4), (4, 3), (2, 3)],  # 101111
            48: [(3, 3), (2, 3)],  # 110000
            49: [(4, 4), (3, 3), (2, 3)],  # 110001
            50: [(3, 4), (3, 3), (2, 3)],  # 110010
            51: [(4, 4), (3, 4), (3, 3), (2, 3)],  # 110011
            52: [(2, 4), (3, 3), (2, 3)],  # 110100
            53: [(4, 4), (2, 4), (3, 3), (2, 3)],  # 110101
            54: [(3, 4), (2, 4), (3, 3), (2, 3)],  # 110110
            55: [(4, 4), (3, 4), (2, 4), (3, 3), (2, 3)],  # 110111
            56: [(4, 3), (3, 3), (2, 3)],  # 111000
            57: [(4, 4), (4, 3), (3, 3), (2, 3)],  # 111001
            58: [(3, 4), (4, 3), (3, 3), (2, 3)],  # 111010
            59: [(4, 4), (3, 4), (4, 3), (3, 3), (2, 3)],  # 111011
            60: [(2, 4), (4, 3), (3, 3), (2, 3)]  # 111100
        }

        # Get the bit positions for the current hour
            positions = bit_positions_minutes.get(self.minute, [])

        # Light up the corresponding points on the LED matrix
            for pos in positions:
                    draw.point(pos, fill="white")

    def seconds(self):
        with canvas(self.device) as draw:
            bit_positions_seconds = {
                1: [(7, 4)],  # 000001
                2: [(6, 4)],  # 000010
                3: [(7, 4), (6, 4)],  # 000011
                4: [(5, 4)],  # 000100
                5: [(7, 4), (5, 4)],  # 000101
                6: [(6, 4), (5, 4)],  # 000110
                7: [(7, 4), (6, 4), (5, 4)],  # 000111
                8: [(7, 3)],  # 001000
                9: [(7, 4), (7, 3)],  # 001001
                10: [(6, 4), (7, 3)],  # 001010
                11: [(7, 4), (6, 4), (7, 3)],  # 001011
                12: [(5, 4), (7, 3)],  # 001100
                13: [(7, 4), (5, 4), (7, 3)],  # 001101
                14: [(6, 4), (5, 4), (7, 3)],  # 001110
                15: [(7, 4), (6, 4), (5, 4), (7, 3)],  # 001111
                16: [(6, 3)],  # 010000
                17: [(7, 4), (6, 3)],  # 010001
                18: [(6, 4), (6, 3)],  # 010010
                19: [(7, 4), (6, 4), (6, 3)],  # 010011
                20: [(5, 4), (6, 3)],  # 010100
                21: [(7, 4), (5, 4), (6, 3)],  # 010101
                22: [(6, 4), (5, 4), (6, 3)],  # 010110
                23: [(7, 4), (6, 4), (5, 4), (6, 3)],  # 010111
                24: [(5, 3)],  # 011000
                25: [(7, 4), (5, 3)],  # 011001
                26: [(6, 4), (5, 3)],  # 011010
                27: [(7, 4), (6, 4), (5, 3)],  # 011011
                28: [(5, 4), (5, 3)],  # 011100
                29: [(7, 4), (5, 4), (5, 3)],  # 011101
                30: [(6, 4), (5, 4), (5, 3)],  # 011110
                31: [(7, 4), (6, 4), (5, 4), (5, 3)],  # 011111
                32: [(7, 3)],  # 100000
                33: [(7, 4), (7, 3)],  # 100001
                34: [(6, 4), (7, 3)],  # 100010
                35: [(7, 4), (6, 4), (7, 3)],  # 100011
                36: [(5, 4), (7, 3)],  # 100100
                37: [(7, 4), (5, 4), (7, 3)],  # 100101
                38: [(6, 4), (5, 4), (7, 3)],  # 100110
                39: [(7, 4), (6, 4), (5, 4), (7, 3)],  # 100111
                40: [(5, 3)],  # 101000
                41: [(7, 4), (5, 3)],  # 101001
                42: [(6, 4), (5, 3)],  # 101010
                43: [(7, 4), (6, 4), (5, 3)],  # 101011
                44: [(5, 4), (5, 3)],  # 101100
                45: [(7, 4), (5, 4), (5, 3)],  # 101101
                46: [(6, 4), (5, 4), (5, 3)],  # 101110
                47: [(7, 4), (6, 4), (5, 4), (5, 3)],  # 101111
                48: [(6, 3), (5, 3)],  # 110000
                49: [(7, 4), (6, 3), (5, 3)],  # 110001
                50: [(6, 4), (6, 3), (5, 3)],  # 110010
                51: [(7, 4), (6, 4), (6, 3), (5, 3)],  # 110011
                52: [(5, 4), (6, 3), (5, 3)],  # 110100
                53: [(7, 4), (5, 4), (6, 3), (5, 3)],  # 110101
                54: [(6, 4), (5, 4), (6, 3), (5, 3)],  # 110110
                55: [(7, 4), (6, 4), (5, 4), (6, 3), (5, 3)],  # 110111
                56: [(7, 3), (6, 3), (5, 3)],  # 111000
                57: [(7, 4), (7, 3), (6, 3), (5, 3)],  # 111001
                58: [(6, 4), (7, 3), (6, 3), (5, 3)],  # 111010
                59: [(7, 4), (6, 4), (7, 3), (6, 3), (5, 3)],  # 111011
                60: [(5, 4), (7, 3), (6, 3), (5, 3)]  # 111100
        }

            
            positions = bit_positions_seconds.get(self.second, [])

            for pos in positions:
                draw.point(pos, fill="white")
                
                
    def clear_display(self):
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="black", fill="black")
        
        
def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial)
    bitclock = BinaryClock(device)
    time = Time()
    try:
        while True:
            bitclock.clear_display()
            bitclock.update()
            bitclock.hours()
            sleep(0.2)
            bitclock.minutes()
            sleep(0.2)
            bitclock.seconds()
            sleep(0.3)
            bitclock.AMPM()  # Display AM/PM
            sleep(0.2)
                 # Adjust sleep duration as needed
            
        
    except KeyboardInterrupt:
        bitclock.clear_display()
        return 0

if __name__ == "__main__":
    main()
