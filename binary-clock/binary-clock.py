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

    def minutes(self, col, row):

        # Turn on LEDs without using an infinite loop
        with canvas(self.device) as draw:
            for i in range(2, 5):
                draw.point((i, row), fill="white")      # Turn on the LED at (col, i)
                draw.point((i, row-1), fill="white")    # Turn on the LED at (col-1, i)



    def seconds(self, col, row):
        with canvas(self.device) as draw:
            for i in range(5, 8):
                draw.point((i, row), fill="white")
                draw.point((i, row-1), fill="white")    


            
    def clear_display(self):
        with canvas(self.device) as draw:
            draw.rectangle(self.device.bounding_box, outline="black", fill="black")
        
        
def main():
    serial = spi(port=0, device=0, gpio=noop())
    device = max7219(serial)
    bitclock = BinaryClock(device)
    try:
        while True:
            bitclock.hours()
            sleep(1)
            bitclock.clear_display()
            bitclock.minutes(2, 4)
            sleep(1)
            bitclock.clear_display()
            bitclock.seconds(5, 4)
            sleep(1)
            
    except KeyboardInterrupt:
        bitclock.clear_display()
        return 0

if __name__ == "__main__":
    main()
