from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
from time import sleep


class Alphabat:
    def __init__(self, device):
        self.characters = {
        'A': [(1,1), (2,0), (3,0), (4,0), (5,1), (1,2), (5,2), (1,3), (2,3), (3,3), (4,3), (5,3), (1,4), (5,4)],
        'B': [(1,0), (2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (2,2), (3,2), (4,2), (5,3), (1,3), (2,4), (3,4), (4,4), (1,5)],
        'C': [(2,0), (3,0), (4,0), (1,1), (1,2), (1,3), (1,4), (2,5), (3,5), (4,5)],
        'D': [(1,0), (2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (5,2), (1,3), (5,3), (1,4), (5,4), (2,5), (3,5), (4,5)],
        'E': [(1,0), (2,0), (3,0), (4,0), (1,1), (1,2), (2,2), (3,2), (1,3), (1,4), (2,5), (3,5), (4,5)],
        'F': [(1,0), (2,0), (3,0), (4,0), (1,1), (1,2), (2,2), (3,2), (1,3), (1,4), (1,5)],
        'G': [(2,0), (3,0), (4,0), (1,1), (1,2), (1,3), (1,4), (3,4), (4,4), (5,4), (4,5)],
        'H': [(1,0), (5,0), (1,1), (5,1), (1,2), (2,2), (3,2), (4,2), (5,2), (1,3), (5,3), (1,4), (5,4)],
        'I': [(2,0), (3,0), (4,0), (3,1), (3,2), (3,3), (3,4), (2,5), (3,5), (4,5)],
        'J': [(3,0), (4,0), (5,0), (4,1), (4,2), (4,3), (1,4), (2,4), (3,5)],
        'K': [(1,0), (5,0), (1,1), (4,1), (1,2), (3,2), (1,3), (4,3), (1,4), (5,4)],
        'L': [(1,0), (1,1), (1,2), (1,3), (1,4), (2,5), (3,5), (4,5)],
        'M': [(1,0), (2,0), (5,0), (1,1), (3,1), (5,1), (1,2), (2,2), (4,2), (5,2), (1,3), (5,3), (1,4), (5,4)],
        'N': [(1,0), (2,0), (5,0), (1,1), (3,1), (5,1), (1,2), (4,2), (5,2), (1,3), (5,3), (1,4), (5,4)],
        'O': [(2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (5,2), (1,3), (5,3), (2,5), (3,5), (4,5)],
        'P': [(1,0), (2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (2,2), (3,2), (4,2), (1,3), (1,4), (1,5)],
        'Q': [(2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (5,2), (1,3), (5,3), (2,5), (3,5), (4,5), (4,4), (5,5)],
        'R': [(1,0), (2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (2,2), (3,2), (4,2), (1,3), (3,3), (1,4), (4,4), (5,4)],
        'S': [(2,0), (3,0), (4,0), (1,1), (2,2), (3,2), (4,2), (5,3), (2,4), (3,5), (4,5)],
        'T': [(1,0), (2,0), (3,0), (4,0), (5,0), (3,1), (3,2), (3,3), (3,4), (3,5)],
        'U': [(1,0), (5,0), (1,1), (5,1), (1,2), (5,2), (1,3), (5,3), (2,5), (3,5), (4,5)],
        'V': [(1,0), (5,0), (1,1), (5,1), (1,2), (5,2), (2,3), (4,3), (3,5)],
        'W': [(1,0), (5,0), (1,1), (5,1), (1,2), (3,2), (5,2), (2,3), (4,3), (1,4), (5,4)],
        'X': [(1,0), (5,0), (2,1), (4,1), (3,2), (3,3), (2,4), (4,4), (1,5), (5,5)],
        'Y': [(1,0), (5,0), (2,1), (4,1), (3,2), (3,3), (3,4), (3,5)],
        'Z': [(1,0), (2,0), (3,0), (4,0), (5,0), (4,1), (3,2), (2,3), (1,4), (1,5), (2,5), (3,5), (4,5), (5,5)],
    
        '0': [(2,0), (3,0), (4,0), (1,1), (5,1), (1,2), (5,2), (1,3), (5,3), (1,4), (5,4), (2,5), (3,5), (4,5)],
        '1': [(3,0), (2,1), (3,1), (3,2), (3,3), (3,4), (3,5)],
        '2': [(2,0), (3,0), (4,0), (5,1), (5,2), (2,3), (3,3), (4,3), (1,4), (1,5), (2,5), (3,5), (4,5)],
        '3': [(2,0), (3,0), (4,0), (5,1), (3,2), (4,2), (5,3), (2,4), (3,5), (4,5)],
        '4': [(4,0), (3,1), (3,2), (2,2), (1,3), (2,3), (3,3), (3,4), (3,5)],
        '5': [(2,0), (3,0), (4,0), (1,1), (2,2), (3,2), (4,2), (5,3), (2,4), (3,5), (4,5)],
        '6': [(2,0), (3,0), (4,0), (1,1), (1,2), (2,3), (3,3), (4,3), (1,4), (5,4), (2,5), (3,5), (4,5)],
        '7': [(1,0), (2,0), (3,0), (4,0), (5,0), (4,1), (3,2), (3,3), (2,4), (2,5)],
        '8': [(2,0), (3,0), (4,0), (1,1), (5,1), (2,3), (3,3), (4,3), (1,4), (5,4), (2,5), (3,5), (4,5)],
        '9': [(2,0), (3,0), (4,0), (1,1), (5,1), (2,2), (3,2), (4,2), (5,3), (2,4), (3,5), (4,5)]
    }
        self.device = device  # Save the device for use in drawing

    def display_character(self, char):
        if char in self.characters:
            with canvas(self.device) as draw:
                for point in self.characters[char]:
                    draw.point(point, fill="white")

    def render_character(self, char):
        pixels = self.characters.get(char, [])  # Get pixel coordinates for the character
        bitmap = [[0 for _ in range(8)] for _ in range(8)]  # 8x8 grid for character
        for x, y in pixels:
            bitmap[y][x] = 1
        return bitmap

    def scroll_text(self, message, delay=0.1, char_spacing=4):
        # Create the full bitmap for the message by concatenating character bitmaps
        full_message_bitmap = []
        for char in message:
            char_bitmap = self.render_character(char)
            # Extract columns from character and append to full message bitmap
            for col in range(8):
                full_message_bitmap.append([char_bitmap[row][col] for row in range(8)])

            # Add some spacing between characters
            for _ in range(char_spacing):  # Use char_spacing to adjust spacing between characters
                full_message_bitmap.append([0 for _ in range(8)])

        # Scroll the message
        for start_col in range(len(full_message_bitmap) - 8):
            with canvas(self.device) as draw:
                for x in range(8):  # 8 columns wide
                    for y in range(8):  # 8 rows tall
                        if full_message_bitmap[start_col + x][y]:
                            draw.point((x, y), fill="white")
            sleep(delay)
            
def main():
    # Setup SPI for the MAX7219
    serial = spi(port=0, device=0)
    device = max7219(serial, cascaded=1)

    alpha = Alphabat(device)
    alpha.scroll_text("HELLO", delay=0.1, char_spacing=1) 

# Manually define each letter's pixel coordinates in a 6x8 grid (6 height, 8 width)
# Each character is represented as a set of (x, y) points to be lit on the matrix





"""while True:
    for char in char_sequence:
        display_character(char)
        sleep(1)  # Display each character for 1 second
        
# Loop through all characters and display each for 1 second
char_sequence = "ASSHOLE"


"""

if __name__ == "__main__":
    main()