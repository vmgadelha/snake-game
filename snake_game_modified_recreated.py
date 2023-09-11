
import pygame
import time
import random
import tkinter as tk
from tkinter import simpledialog

pygame.init()

# Function to set snake speed
def set_speed():
    global snake_speed
    ROOT = tk.Tk()
    ROOT.withdraw()
    snake_speed = simpledialog.askinteger(title="Snake Speed", prompt="Enter the speed of the snake (1 to 100):")
    if snake_speed is None:
        snake_speed = 30

# Screen dimensions
width, height = 800, 600
gameDisplay = pygame.display.set_mode((width, height))
pygame.display.set_caption('Snake Game')

# Initialize speed variable
snake_speed = 30

# Colors
black, white, red = (0, 0, 0), (255, 255, 255), (255, 0, 0)

clock = pygame.time.Clock()
snake_block = 10

font = pygame.font.SysFont(None, 50)

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(gameDisplay, white, [x[0], x[1], snake_block, snake_block])

def gameLoop():
    global snake_speed
    game_over = False
    game_close = False

    # Snake initial position
    x1, y1 = width / 2, height / 2
    dx, dy = 0, 0

    snake_list = []
    length_of_snake = 1

    # Food position
    foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            gameDisplay.fill(black)
            message = font.render("You Lost! Press Q-Quit or C-Continue", True, red)
            gameDisplay.blit(message, [width / 6, height / 3])
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
                game_close = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = -snake_block
                    dy = 0
                elif event.key == pygame.K_RIGHT:
                    dx = snake_block
                    dy = 0
                elif event.key == pygame.K_UP:
                    dy = -snake_block
                    dx = 0
                elif event.key == pygame.K_DOWN:
                    dy = snake_block
                    dx = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                set_speed()

        if x1 >= width or x1 < 0 or y1 >= height or y1 < 0:
            game_close = True
        x1 += dx
        y1 += dy
        gameDisplay.fill(black)
        pygame.draw.rect(gameDisplay, red, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx, foody = round(random.randrange(0, width - snake_block) / 10.0) * 10.0, round(random.randrange(0, height - snake_block) / 10.0) * 10.0
            length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

# Run the game
gameLoop()
