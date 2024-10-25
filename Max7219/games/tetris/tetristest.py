import time
import random
import sys
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas
import keyboard  # Make sure to install this library

# Constants
WIDTH = 8
HEIGHT = 8
BLOCK_SIZE = 1  # Each block size on the LED matrix
SPEED = 0.5  # Game speed
WINNING_SCORE = 10

# Tetromino shapes (L, J, T, I, O, S, Z)
TETROMINOS = [
    [[1, 1, 1], [0, 1, 0]],  # T
    [[1, 1, 1], [1, 0, 0]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[1, 1], [1, 1]],        # O
    [[0, 1, 1], [1, 1, 0]],  # S
    [[1, 1, 0], [0, 1, 1]],  # Z
    [[1, 1, 1, 1]],          # I
]

# Initialize MAX7219
serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1, block_orientation=90)

class Tetris:
    def __init__(self):
        self.board = [[0 for _ in range(WIDTH)] for _ in range(HEIGHT)]
        self.current_tetromino = None
        self.current_x = 0
        self.current_y = 0
        self.score = 0
        self.spawn_tetromino()

    def spawn_tetromino(self):
        """Spawn a new tetromino at the top of the board."""
        self.current_tetromino = random.choice(TETROMINOS)
        self.current_x = WIDTH // 2 - len(self.current_tetromino[0]) // 2
        self.current_y = 0

        if self.collides():
            print("Game Over!")
            sys.exit()

    def collides(self):
        """Check if the current tetromino collides with the board."""
        for y, row in enumerate(self.current_tetromino):
            for x, value in enumerate(row):
                if value:
                    if (self.current_y + y >= HEIGHT or
                            self.current_x + x < 0 or
                            self.current_x + x >= WIDTH or
                            self.board[self.current_y + y][self.current_x + x]):
                        return True
        return False

    def merge(self):
        """Merge the current tetromino into the board."""
        for y, row in enumerate(self.current_tetromino):
            for x, value in enumerate(row):
                if value:
                    self.board[self.current_y + y][self.current_x + x] = 1

    def clear_lines(self):
        """Clear filled lines and update the score."""
        lines_to_clear = [i for i, row in enumerate(self.board) if all(row)]
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0 for _ in range(WIDTH)])
            self.score += 1

    def rotate(self):
        """Rotate the current tetromino 90 degrees clockwise."""
        self.current_tetromino = [list(row) for row in zip(*self.current_tetromino[::-1])]
        if self.collides():
            # Undo rotation if it collides
            self.current_tetromino = [list(row) for row in zip(*self.current_tetromino)][::-1]

    def move(self, dx):
        """Move the current tetromino left or right."""
        self.current_x += dx
        if self.collides():
            self.current_x -= dx

    def drop(self):
        """Drop the current tetromino one row down."""
        self.current_y += 1
        if self.collides():
            self.current_y -= 1
            self.merge()
            self.clear_lines()
            self.spawn_tetromino()

    def draw_board(self):
        """Draw the current game board on the LED matrix."""
        with canvas(device) as draw:
            # Draw the board
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    if self.board[y][x]:
                        draw.point((x, y), fill="white")

            # Draw the current tetromino
            for y, row in enumerate(self.current_tetromino):
                for x, value in enumerate(row):
                    if value:
                        draw.point((self.current_x + x, self.current_y + y), fill="white")

def main():
    game = Tetris()
    
    try:
        while True:
            game.drop()  # Drop the tetromino
            game.draw_board()  # Draw the game state
            time.sleep(SPEED)  # Control game speed
            
            # Control tetromino movement
            if keyboard.is_pressed('a'):  # Move left
                game.move(-1)
            if keyboard.is_pressed('d'):  # Move right
                game.move(1)
            if keyboard.is_pressed('s'):  # Move down faster
                game.drop()
            if keyboard.is_pressed('w'):  # Rotate
                game.rotate()

            # Check for winning score
            if game.score >= WINNING_SCORE:
                print(f"You Win! Score: {game.score}")
                break

    except KeyboardInterrupt:
        print("Game interrupted!")

if __name__ == "__main__":
    main()
