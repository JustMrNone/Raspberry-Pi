from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from PIL import ImageFont
from time import sleep
from datetime import datetime

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

def exchange(hour, minute):
    #how many minutes since midnight 
    minutes_passed = (hour * 60) + minute
    custom_time = (minutes_passed / 1440) * 64
    return round(custom_time)
    
    
def main():
    hours, minutes, seconds, ampm = get_current_time_12_hour()
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)
    now = exchange(hours, minutes)
    points = []
    
    for x in range(8):
        for i in range(8):
            points.append((i+0, 0+x))


    with canvas(device) as draw:
        for point in points[:now]:
            draw.point(point, fill="white")

    sleep(10)

    print(len(points), now)    
main()
"""

for x in range(8):
    for y in range(x+1):
        with canvas(device) as draw:
            draw.point((0+y, 0), fill = "white")
            sleep(0.1)

for x in range(8):
    for y in range(x):
        with canvas(device) as draw:
            draw.point((x+0, y), fill = "white")
            sleep(0.1)        

"""