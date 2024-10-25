import time
import random
from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi
from luma.core.render import canvas

# Constants for the game
WIDTH = 8
HEIGHT = 8
PADDLE_HEIGHT = 3
BALL_SIZE = 1

# Paddle positions
player1_pos = 3
player2_pos = 3

# Ball position and velocity
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_vel_x = random.choice([-1, 1])
ball_vel_y = random.choice([-1, 1])

# Initialize MAX7219 LED matrix
serial = spi(port=0, device=0)
device = max7219(serial, cascaded=1, block_orientation=90)

def draw_game():
    """Draw the current state of the game."""
    with canvas(device) as draw:
        # Draw paddles
        for i in range(PADDLE_HEIGHT):
            draw.point((0, player1_pos + i), fill="white")  # Player 1
            draw.point((WIDTH - 1, player2_pos + i), fill="white")  # Player 2
        
        # Draw ball
        draw.point((ball_x, ball_y), fill="white")

def update_ball():
    """Update ball position and check for collisions."""
    global ball_x, ball_y, ball_vel_x, ball_vel_y, player1_pos, player2_pos
    
    # Move the ball
    ball_x += ball_vel_x
    ball_y += ball_vel_y
    
    # Check for collision with top and bottom walls
    if ball_y <= 0 or ball_y >= HEIGHT - 1:
        ball_vel_y *= -1  # Reverse vertical direction

    # Check for collision with paddles
    if ball_x == 0 and player1_pos <= ball_y < player1_pos + PADDLE_HEIGHT:
        ball_vel_x *= -1  # Reverse horizontal direction for player 1
    elif ball_x == WIDTH - 1 and player2_pos <= ball_y < player2_pos + PADDLE_HEIGHT:
        ball_vel_x *= -1  # Reverse horizontal direction for player 2

    # Check for scoring
    if ball_x < 0 or ball_x >= WIDTH:
        reset_ball()

def reset_ball():
    """Reset the ball to the center of the playfield."""
    global ball_x, ball_y, ball_vel_x, ball_vel_y
    ball_x = WIDTH // 2
    ball_y = HEIGHT // 2
    ball_vel_x = random.choice([-1, 1])
    ball_vel_y = random.choice([-1, 1])

def update_paddle(paddle, direction):
    """Update paddle position based on input."""
    global player1_pos, player2_pos
    if paddle == 1:
        if direction == 'up' and player1_pos > 0:
            player1_pos -= 1
        elif direction == 'down' and player1_pos < HEIGHT - PADDLE_HEIGHT:
            player1_pos += 1
    elif paddle == 2:
        if direction == 'up' and player2_pos > 0:
            player2_pos -= 1
        elif direction == 'down' and player2_pos < HEIGHT - PADDLE_HEIGHT:
            player2_pos += 1

# Main game loop
try:
    while True:
        draw_game()
        update_ball()
        
        # Simple controls for player paddles (replace with your input handling)
        command = input("Enter '1 up', '1 down', '2 up', '2 down' to move paddles or 'q' to quit: ")
        if command == 'q':
            break
        elif command.startswith('1'):
            direction = command.split()[1]
            update_paddle(1, direction)
        elif command.startswith('2'):
            direction = command.split()[1]
            update_paddle(2, direction)

        time.sleep(0.1)  # Control the game speed

except KeyboardInterrupt:
    print("Game over!")
