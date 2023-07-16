import pygame
import time

pygame.init()

width, height = 600, 200
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Flip Clock")

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

digit_images = {
    '0': None,
    '1': None,
    '2': None,
    '3': None,
    '4': None,
    '5': None,
    '6': None,
    '7': None,
    '8': None,
    '9': None
}

for digit in digit_images:
    digit_images[digit] = pygame.transform.scale(pygame.image.load(f'clock/{digit}.png').convert(), (64, 64))

def display_time():
    current_time = time.strftime("%H:%M:%S")
    window.fill(BLACK)
    x = 50
    for digit in current_time:
        if digit == ':':
            x += 40
            continue
        window.blit(digit_images[digit], (x, 50))
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
