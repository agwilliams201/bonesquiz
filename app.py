import pygame
import os
import random
import sys
from pygame.locals import *

# Initialize Pygame
pygame.init()

# Set up the display
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Bone Quiz")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PERI = (204, 204, 255)
BLACK = (0,0,0)
STUPID_COLOR = (250, 225, 223)
GOOD_GREEN = (189, 228, 167)

# Set up the fonts
font = pygame.font.SysFont(None, 48)

# Define button and image positions
image_rect = pygame.Rect(100, 50, 600, 300)  # Placeholder for the bone image
textbox = pygame.Rect(250, 400, 300, 100)
button = pygame.Rect(350, 525, 100, 50)
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
image_folder = 'muscles'  # Folder where images are stored
boneslist = [
    "Biceps brachii long head1.png",
    "Biceps brachii long head2.png",
    "Biceps brachii short head1.png",
    "Biceps brachii short head2.png",
    "Biceps brachii1.png",
    "Biceps brachii2.png",
    "Biceps brachii3.png",
    "Biceps femoris long head1.png",
    "Biceps femoris long head2.png",
    "Biceps femoris long head3.png",
    "Deltoid anterior1.png",
    "Deltoid anterior2.png",
    "Deltoid middle1.png",
    "Deltoid posterior1.png",
    "Deltoid posterior2.png",
    "Deltoid1.png",
    "Deltoid2.png",
    "Deltoid3.png",
    "Deltoid4.png",
    "Extensor digitorum longus1.png",
    "Extensor digitorum longus2.png",
    "Extensor digitorum longus3.png",
    "External oblique1.png",
    "External oblique2.png",
    "External oblique3.png",
    "Flexor digitorum superficialis1.png",
    "Flexor digitorum superficialis2.png",
    "Gastrocnemius1.png",
    "Gastrocnemius2.png",
    "Gastrocnemius3.png",
    "Gluteus maximus1.png",
    "Gluteus maximus2.png",
    "Gluteus medius1.png",
    "Gluteus medius2.png",
    "Gluteus medius3.png",
    "Latissimus dorsi1.png",
    "Latissimus dorsi2.png",
    "Latissimus dorsi3.png",
    "Masseter1.png",
    "Masseter2.png",
    "Orbicularis oculi1.png",
    "Orbicularis oculi2.png",
    "Orbicularis oculi3.png",
    "Orbicularis oris1.png",
    "Orbicularis oris2.png",
    "Pectoralis major1.png",
    "Pectoralis major2.png",
    "Pectoralis major3.png",
    "Platysma1.png",
    "Platysma2.png",
    "Platysma3.png",
    "Rectus Femoris1.png",
    "Rectus Femoris2.png",
    "Rectus Femoris3.png",
    "Semitendinosus1.png",
    "Semitendinosus2.png",
    "Semitendinosus3.png",
    "Sternocleidomastoid1.png",
    "Sternocleidomastoid2.png",
    "Sternocleidomastoid3.png",
    "Temporalis1.png",
    "Temporalis2.png",
    "Tibialis anterior1.png",
    "Tibialis anterior2.png",
    "Tibialis anterior3.png",
    "Trapezius1.png",
    "Trapezius2.png",
    "Vastus Medialis1.png",
    "Vastus Medialis2.png",
    "Vastus Medialis3.png",
    "Vastus lateralis1.png",
    "Vastus lateralis2.png",
    "Vastus lateralis3.png",
    "delta middle2.png"
]
show_result_screen = False
correct_dict = {
    "Biceps brachii long head1.png": "biceps brachii long head",
    "Biceps brachii long head2.png": "biceps brachii long head",
    "Biceps brachii short head1.png": "biceps brachii short head",
    "Biceps brachii short head2.png": "biceps brachii short head",
    "Biceps brachii1.png": "biceps brachii",
    "Biceps brachii2.png": "biceps brachii",
    "Biceps brachii3.png": "biceps brachii",
    "Biceps femoris long head1.png": "biceps femoris long head",
    "Biceps femoris long head2.png": "biceps femoris long head",
    "Biceps femoris long head3.png": "biceps femoris long head",
    "Deltoid anterior1.png": "deltoid anterior",
    "Deltoid anterior2.png": "deltoid anterior",
    "Deltoid middle1.png": "deltoid middle",
    "Deltoid posterior1.png": "deltoid posterior",
    "Deltoid posterior2.png": "deltoid posterior",
    "Deltoid1.png": "deltoid",
    "Deltoid2.png": "deltoid",
    "Deltoid3.png": "deltoid",
    "Deltoid4.png": "deltoid",
    "Extensor digitorum longus1.png": "extensor digitorum longus",
    "Extensor digitorum longus2.png": "extensor digitorum longus",
    "Extensor digitorum longus3.png": "extensor digitorum longus",
    "External oblique1.png": "external oblique",
    "External oblique2.png": "external oblique",
    "External oblique3.png": "external oblique",
    "Flexor digitorum superficialis1.png": "flexor digitorum superficialis",
    "Flexor digitorum superficialis2.png": "flexor digitorum superficialis",
    "Gastrocnemius1.png": "gastrocnemius",
    "Gastrocnemius2.png": "gastrocnemius",
    "Gastrocnemius3.png": "gastrocnemius",
    "Gluteus maximus1.png": "gluteus maximus",
    "Gluteus maximus2.png": "gluteus maximus",
    "Gluteus medius1.png": "gluteus medius",
    "Gluteus medius2.png": "gluteus medius",
    "Gluteus medius3.png": "gluteus medius",
    "Latissimus dorsi1.png": "latissimus dorsi",
    "Latissimus dorsi2.png": "latissimus dorsi",
    "Latissimus dorsi3.png": "latissimus dorsi",
    "Masseter1.png": "masseter",
    "Masseter2.png": "masseter",
    "Orbicularis oculi1.png": "orbicularis oculi",
    "Orbicularis oculi2.png": "orbicularis oculi",
    "Orbicularis oculi3.png": "orbicularis oculi",
    "Orbicularis oris1.png": "orbicularis oris",
    "Orbicularis oris2.png": "orbicularis oris",
    "Pectoralis major1.png": "pectoralis major",
    "Pectoralis major2.png": "pectoralis major",
    "Pectoralis major3.png": "pectoralis major",
    "Platysma1.png": "platysma",
    "Platysma2.png": "platysma",
    "Platysma3.png": "platysma",
    "Rectus Femoris1.png": "rectus femoris",
    "Rectus Femoris2.png": "rectus femoris",
    "Rectus Femoris3.png": "rectus femoris",
    "Semitendinosus1.png": "semitendinosus",
    "Semitendinosus2.png": "semitendinosus",
    "Semitendinosus3.png": "semitendinosus",
    "Sternocleidomastoid1.png": "sternocleidomastoid",
    "Sternocleidomastoid2.png": "sternocleidomastoid",
    "Sternocleidomastoid3.png": "sternocleidomastoid",
    "Temporalis1.png": "temporalis",
    "Temporalis2.png": "temporalis",
    "Tibialis anterior1.png": "tibialis anterior",
    "Tibialis anterior2.png": "tibialis anterior",
    "Tibialis anterior3.png": "tibialis anterior",
    "Trapezius1.png": "trapezius",
    "Trapezius2.png": "trapezius",
    "Vastus Medialis1.png": "vastus medialis",
    "Vastus Medialis2.png": "vastus medialis",
    "Vastus Medialis3.png": "vastus medialis",
    "Vastus lateralis1.png": "vastus lateralis",
    "Vastus lateralis2.png": "vastus lateralis",
    "Vastus lateralis3.png": "vastus lateralis",
    "delta middle2.png": "deltoid middle"
}

def addText():
    font = pygame.font.SysFont(None, 20)
    text_surface = font.render('I am an idiot', True, (0, 0, 0))

    # Get the size of the text surface
    text_width, text_height = text_surface.get_size()

    # Calculate the position to center the text within the button
    text_x = button.centerx - text_width // 2
    text_y = button.centery - text_height // 2

    # Blit the text surface at the calculated position
    screen.blit(text_surface, (text_x, text_y))

    # Update the display
    pygame.display.update()

def load_random_image():
    global bone_image, bone_image_rect
    image_name = random.choice(boneslist)  # Select a random image
    image_path = os.path.join(image_folder, image_name)  # Construct the full path
    bone_image = pygame.image.load(image_path)  # Load the image
    new_width = 350  # example width
    new_height = 350  # example height
    bone_image = pygame.transform.scale(bone_image, (new_width, new_height))
    bone_image_rect = bone_image.get_rect(center=(window_width // 2, window_height // 2 - 100))
    return image_name

img = load_random_image()  # Load the initial image

# Function to draw the main quiz screen
def draw_quiz_screen(correct=None):
    screen.fill(STUPID_COLOR)

    # Draw the bone image placeholder
    pygame.draw.rect(screen, STUPID_COLOR, image_rect)
    screen.blit(bone_image, bone_image_rect)
    
    # Draw the answer button
    pygame.draw.rect(screen, (228, 195, 173), textbox, 0,4)
    pygame.draw.rect(screen, BLACK, textbox, 2,4)
    font = pygame.font.SysFont(None, 30)
    txt_surface = font.render(text, True, BLACK)
    text_width, text_height = txt_surface.get_size()
    text_x = textbox.centerx - text_width // 2
    text_y = textbox.centery - text_height // 2
    screen.blit(txt_surface, (text_x, text_y))

    #Draw the give up button
    pygame.draw.rect(screen, (84, 106, 123), button, 0,4)
    pygame.draw.rect(screen, BLACK, button, 2,4)
    addText()
    pygame.display.flip()

def draw_result_screen(is_correct):
    # Choose the color and text based on whether the answer is correct
    result_color = GOOD_GREEN if is_correct else RED
    result_text = "Correct!" if is_correct else "Incorrect!"
    
    # Draw the result screen
    screen.fill(result_color)
    text_surface = font.render(result_text, True, WHITE)
    text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

def is_correct(text, image_name):
    if correct_dict[image_name] == text:
        return True
    else:
        return False

def draw_answer_screen():
    # Choose the color and text based on whether the answer is correct
    result_color = GOOD_GREEN
    result_text = correct_dict[img][0].upper() + correct_dict[img][1:] 
    # Draw the result screen
    screen.fill(result_color)
    text_surface = font.render(result_text, True, WHITE)
    text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))
    screen.blit(text_surface, text_rect)
    pygame.display.flip()

# Main loop
running = True
while running:
    if show_result_screen:
        if is_correct(text, img) == True:
            draw_result_screen(True)
            pygame.time.wait(2000)
            img = load_random_image()
        else:
            draw_result_screen(False)
            pygame.time.wait(1000)
        # Wait for a bit before moving on
        show_result_screen = False  # Reset the flag
        text = ''
    else:
        draw_quiz_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                text = text.lower()
                draw_result_screen(True)
                show_result_screen = True
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
        mouse_pos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN and button.collidepoint(mouse_pos):
            draw_answer_screen()
            pygame.time.wait(2000)
pygame.quit()


