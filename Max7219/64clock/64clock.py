from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep
from datetime import datetime


class Clock64:
    def __init__(self, device):
        self.device = device
            
    def get_current_time_12_hour(self):
        # Get the current time
        now = datetime.now()
        
        # Extract hours, minutes, and seconds
        hour = now.hour
        minute = now.minute
        second = now.second
        
        return hour, minute, second

    def exchange(self, hour, minute):
        #how many minutes since midnight 
        minutes_passed = (hour * 60) + minute
        custom_time = (minutes_passed / 1440) * 64
        return round(custom_time)

    def show(self):
        points = []
        hours, minutes, seconds = self.get_current_time_12_hour()
        now = self.exchange(hours, minutes)
        try:
            while True:
                for x in range(8):
                    for i in range(8):
                        points.append((i+0, 0+x))

                if now > 0 and now < len(points):
                    with canvas(self.device) as draw:
                        for _ in points:
                            last = points[27 - 1]
                            draw.point(last, fill="white")
                else:
                    print("something is wrong")
        except KeyboardInterrupt: 
            with canvas(self.device) as draw:
                draw.rectangle(self.device.bounding_box, outline="black", fill="black")

def main():
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    clock = Clock64(device)
    clock.show()


main()