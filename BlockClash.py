#
# Block Clash - A puzzle board game programmed by Dr. Eric O. Flores
# Copyright (C) 2024 Dr. Eric O. Flores
# E-mail: eoftoro@gmail.com
# GPL3

import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 700  # Adjust height to fit the bottom pane
ROWS, COLS = 5, 5  # 5x5 grid
BLOCK_SIZE = WIDTH // COLS  # Size of each block
RESET_DELAY = 8000  # 8 seconds delay before resetting (to give more time to see the winner message)
FLASH_INTERVAL = 500  # Flash interval for winner message in milliseconds
MAX_POINTS = 10  # Adjusted maximum points for the game

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREY = (200, 200, 200)

# Set up the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Block Clash")

# Initialize grid and hidden W, X positions
grid = [[None for _ in range(COLS)] for _ in range(ROWS)]
hidden_W = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
hidden_X = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))

# Font for displaying scores and messages
font = pygame.font.SysFont(None, 36)

# Sound loading (assumes you have these .wav files in the folder)
winning_sound = pygame.mixer.Sound("winning.wav")
badmove_sound = pygame.mixer.Sound("badmove.wav")

# Player and Computer Scores
player_score = 0
computer_score = 0

# Randomly select who starts
player_turn = random.choice([True, False])
if player_turn:
    turn_message = "Player, click your block!"
else:
    turn_message = "Computer plays first!"
    # Trigger the computer's first move
    pygame.time.set_timer(pygame.USEREVENT, 1000)

# Game state variables
game_over = False
winner_message = ""
reset_triggered = False  # Track if reset timer has been triggered
flash_timer = 0  # Track time for flashing the winner message
flash_on = True  # Toggle for the flashing effect


# Function to draw grid
def draw_grid():
    for row in range(ROWS):
        for col in range(COLS):
            color = GREY  # Unclicked blocks
            if grid[row][col] == "player":
                color = BLACK  # Player blocks
            elif grid[row][col] == "computer":
                color = BLUE  # Computer blocks
            pygame.draw.rect(
                screen,
                color,
                (col * BLOCK_SIZE, 100 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
            )  # Offset the grid to start below the top pane
            pygame.draw.rect(
                screen,
                WHITE,
                (col * BLOCK_SIZE, 100 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
                2,
            )


# Draw the score panel at the top
def draw_score_panel():
    player_text = font.render(f"Player: {player_score}", True, BLACK)
    computer_text = font.render(f"Computer: {computer_score}", True, BLUE)
    screen.blit(player_text, (20, 20))  # Top left
    screen.blit(
        computer_text, (WIDTH - computer_text.get_width() - 20, 20)
    )  # Top right


# Draw the information panel **just below the score panel**
def draw_info_panel():
    global winner_message, flash_on
    if game_over:
        if flash_on:  # Flash the winner message
            message_text = font.render(winner_message, True, BLACK)
            screen.blit(
                message_text, (WIDTH // 2 - message_text.get_width() // 2, 60)
            )  # Display the message below the scoreboard
    else:
        message_text = font.render(turn_message, True, BLACK)
        screen.blit(
            message_text, (WIDTH // 2 - message_text.get_width() // 2, 60)
        )  # Display normal turn message


# Check if a block is empty
def is_empty(row, col):
    return grid[row][col] is None


# Flash the "X" block in red
def flash_X_block(row, col):
    for _ in range(3):  # Flash 3 times
        pygame.draw.rect(
            screen,
            RED,
            (col * BLOCK_SIZE, 100 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
        )
        pygame.display.update()
        pygame.time.delay(200)
        pygame.draw.rect(
            screen,
            GREY,
            (col * BLOCK_SIZE, 100 + row * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE),
        )
        pygame.display.update()
        pygame.time.delay(200)


# Computer's move (random)
def computer_move():
    global computer_score, turn_message
    empty_blocks = [(r, c) for r in range(ROWS) for c in range(COLS) if is_empty(r, c)]
    if empty_blocks:
        row, col = random.choice(empty_blocks)
        check_hidden(row, col, "computer")
        grid[row][col] = "computer"
        computer_score += 1
        turn_message = "Player, click your block!"


# Check for hidden W or X block
def check_hidden(row, col, player_type):
    global player_score, computer_score

    # If the player/computer clicked on the hidden "W" (winning block)
    if (row, col) == hidden_W:
        winning_sound.play()
        if player_type == "player":
            player_score += 1
            print("Player found a W block! Bonus point!")
        else:
            computer_score += 1
            print("Computer found a W block! Bonus point!")
        reset_hidden()  # Move hidden blocks to new random positions

    # If the player/computer clicked on the hidden "X" (bad block)
    elif (row, col) == hidden_X:
        flash_X_block(row, col)  # Flash the block in red
        badmove_sound.play()
        if player_type == "player":
            player_score -= 1
            print("Player clicked on X block! Penalty!")
        else:
            computer_score -= 1
            print("Computer clicked on X block! Penalty!")
        reset_hidden()  # Move hidden blocks


# Move hidden blocks to new random positions
def reset_hidden():
    global hidden_W, hidden_X
    hidden_W = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))
    hidden_X = (random.randint(0, ROWS - 1), random.randint(0, COLS - 1))


# Check if the grid is full (game end condition)
def is_grid_full():
    for row in range(ROWS):
        for col in range(COLS):
            if grid[row][col] is None:
                return False  # There's still an empty block, so game is not yet over
    return True  # All blocks are filled


# Function to play sound
def play_click_sound():
    click_sound = pygame.mixer.Sound("click.wav")
    click_sound.play()


# Function to reset the game
def reset_game():
    global grid, player_score, computer_score, player_turn, game_over, winner_message, turn_message, reset_triggered, flash_on
    grid = [[None for _ in range(COLS)] for _ in range(ROWS)]  # Reset the grid
    player_score, computer_score = 0, 0  # Reset scores
    player_turn = random.choice([True, False])  # Randomly pick who goes first
    game_over = False
    reset_triggered = False  # Reset the reset trigger
    flash_on = True  # Reset flashing state
    winner_message = ""
    pygame.time.set_timer(
        pygame.USEREVENT, 0
    )  # Ensure the timer is stopped before resetting
    if player_turn:
        turn_message = "Player, click your block!"
    else:
        turn_message = "Computer plays first!"
        pygame.time.set_timer(
            pygame.USEREVENT, 1000
        )  # Trigger the computer's first move


# Function to handle game end based on score or grid being full
def handle_game_end():
    global game_over, winner_message, reset_triggered
    if is_grid_full() or player_score >= MAX_POINTS or computer_score >= MAX_POINTS:
        # Determine the winner based on the score
        if player_score > computer_score:
            winner_message = "Player Wins!"
        elif computer_score > player_score:
            winner_message = "Computer Wins!"
        else:
            winner_message = "It's a Tie!"
        game_over = True
        pygame.display.update()  # Display the winner message immediately

        # Trigger a reset after 8 seconds (if it hasn't already been triggered)
        if not reset_triggered:
            pygame.time.set_timer(
                pygame.USEREVENT + 1, RESET_DELAY
            )  # Trigger reset after 8 seconds
            reset_triggered = True


# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Computer makes the first move if selected
        if event.type == pygame.USEREVENT and not player_turn:
            computer_move()
            player_turn = True
            pygame.time.set_timer(
                pygame.USEREVENT, 0
            )  # Stop the timer after the first move

        # Handle the reset timer
        if event.type == pygame.USEREVENT + 1:  # Custom timer event for reset
            reset_game()

        # Handle player click
        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if (
                player_turn and 100 <= mouse_y < 100 + ROWS * BLOCK_SIZE
            ):  # Ensure clicks are within the grid area
                row = (mouse_y - 100) // BLOCK_SIZE
                col = mouse_x // BLOCK_SIZE

                # If clicked block is empty
                if is_empty(row, col):
                    check_hidden(row, col, "player")
                    grid[row][col] = "player"
                    play_click_sound()  # Play sound when block is clicked
                    player_turn = False  # Switch to computer's turn
                    player_score += 1

                    # Check for game end conditions (either score or full grid)
                    handle_game_end()
                    if not game_over:
                        # Computer's turn
                        computer_move()
                        player_turn = True

    # Flash the winner message every 500 milliseconds during the game over state
    if game_over:
        flash_timer += clock.get_time()
        if flash_timer >= FLASH_INTERVAL:
            flash_on = not flash_on  # Toggle the flashing state
            flash_timer = 0  # Reset the timer for the next flash

    # Draw everything
    screen.fill(WHITE)
    draw_score_panel()  # Top pane (scoreboard)
    draw_info_panel()  # Message just below the scoreboard
    draw_grid()  # Center pane (game area)
    pygame.display.update()

    clock.tick(60)  # Limit the frame rate to 60 FPS

pygame.quit()
