from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from time import sleep

class PI4Logo:
    def __init__(self, device, period):
        self.device = device
        self.period = period

    def rotate_90_clockwise(self, points):
        # Rotate each point (x, y) by 90 degrees clockwise
        return [(y, 7 - x) for x, y in points]

    def draw_logo(self):
        # Updated version of the Raspberry Pi logo on an 8x8 matrix
        berry = [
            # Main body of the raspberry (more rounded shape)
            (2, 3), (2, 4),  # Top middle
            (3, 2), (3, 3), (3, 4), (3, 5),  # Upper sides, filling in
            (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),  # Middle sides, filling in
            (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),  # Middle sides, filling in
            (6, 2), (6, 3), (6, 4), (6, 5),  # Lower sides, filling in
            (7, 3), (7, 4)   # Bottom middle
        ]

        leaves = [
            # Leaves on top of the raspberry
            (0, 3), (0, 4),  # Top middle
            (1, 2), (1, 3), (1, 4), (1, 5),  # Side leaves, slightly extended to fill more
        ]

        # Combine berry and leaves
        logo = berry + leaves

        # Rotate the logo 90 degrees clockwise three times to achieve a 270-degree rotation
        rotated_logo_once = self.rotate_90_clockwise(logo)
        rotated_logo_twice = self.rotate_90_clockwise(rotated_logo_once)
        rotated_logo_thrice = self.rotate_90_clockwise(rotated_logo_twice)

        # Draw the rotated logo on the matrix
        with canvas(self.device) as draw:
            draw.point(rotated_logo_thrice, fill="white")
        sleep(self.period)

def main():
    # Initialize the SPI interface and the LED matrix device
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)  # 1 matrix display
    pi_logo = PI4Logo(device, 20)  # Set period to 1 second
    pi_logo.draw_logo()

if __name__ == "__main__":
    main()
