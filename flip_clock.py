import pygame
import time
pygame.init()

width, height = 600, 200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flip Clock")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

digit_images = [
    pygame.transform.scale(pygame.image.load('clock/0.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/1.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/2.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/3.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/4.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/5.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/6.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/7.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/8.png'), (64, 64)),
    pygame.transform.scale(pygame.image.load('clock/9.png'), (64, 64))
]


def display_time():
    current_time = time.strftime("%H:%M:%S")
    window.fill(BLACK)
    x = 50
    for digit in current_time:
        if digit == ':':
            x += 40
            continue
        digit_value = int(digit)
        window.blit(digit_images[digit_value], (x, 50))
        x += 70 
    pygame.display.flip()

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the time
    display_time()

    # Set the game's FPS
    clock.tick(30)  # Update the clock every second

# Quit the game
pygame.quit()
