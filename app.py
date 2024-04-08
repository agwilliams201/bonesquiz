import pygame
import os
import random
import sys

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

# Set up the fonts
font = pygame.font.SysFont(None, 48)

# Define button and image positions
image_rect = pygame.Rect(100, 50, 600, 300)  # Placeholder for the bone image
textbox = pygame.Rect(250, 400, 300, 100)
back_button_rect = pygame.Rect(0, 550, 80, 40)  # Placeholder for the back button
next_button_rect = pygame.Rect(700, 550, 80, 40)  # Placeholder for the next button
text = ''
color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
active = False
image_folder = 'bonespngs'  # Folder where images are stored
boneslist = ['atlas1.png', 'atlas2.png', 'atlas3.png', 'atlas4.png', 'atlas5.png',
    'axis1.png', 'axis2.png', 'axis3.png', 'axis4.png', 'axis5.png',
    'lumbar1.png', 'lumbar2.png', 'lumbar3.png', 'lumbar4.png', 'lumbar5.png',
    'sacrum1.png', 'sacrum2.png', 'sacrum3.png', 'sacrum4.png', 'sacrum5.png',
    'coccyx1.png', 'coccyx2.png', 'coccyx3.png', 'coccyx4.png', 'coccyx5.png',
    'scapula1.png', 'scapula2.png', 'scapula3.png', 'scapula4.png', 'scapula5.png',
    'humerus1.png', 'humerus2.png', 'humerus3.png', 'humerus4.png', 'humerus5.png',
    'ulna1.png', 'ulna2.png', 'ulna3.png', 'ulna4.png', 'ulna5.png',
    'radius1.png', 'radius2.png', 'radius3.png', 'radius4.png', 'radius5.png',
    'metacarpals1.png', 'metacarpals2.png', 'metacarpals3.png', 'metacarpals4.png', 'metacarpals5.png',
    'ilium1.png', 'ilium2.png', 'ilium3.png', 'ilium4.png', 'ilium5.png',
    'maxilla1.png', 'maxilla2.png', 'maxilla3.png', 'maxilla4.png', 'maxilla5.png',
    'mandible1.png', 'mandible2.png', 'mandible3.png', 'mandible4.png', 'mandible5.png',
    'temporal1.png', 'temporal2.png', 'temporal3.png', 'temporal4.png', 'temporal5.png',
    'parietal1.png', 'parietal2.png', 'parietal3.png', 'parietal4.png', 'parietal5.png',
    'occipital1.png', 'occipital2.png', 'occipital3.png', 'occipital4.png', 'occipital5.png',
    'vomer1.png', 'vomer2.png', 'vomer3.png', 'vomer4.png', 'vomer5.png',
    'hyoid1.png', 'hyoid2.png', 'hyoid3.png', 'hyoid4.png', 'hyoid5.png',
    'nasal1.png', 'nasal2.png', 'nasal3.png', 'nasal4.png', 'nasal5.png',
    'clavicle1.png', 'clavicle2.png', 'clavicle3.png', 'clavicle4.png', 'clavicle5.png',
    'ribs1.png', 'ribs2.png', 'ribs3.png', 'ribs4.png', 'ribs5.png',
    'sternum1.png', 'sternum2.png', 'sternum3.png', 'sternum4.png', 'sternum5.png',
    'xiphoid_process1.png', 'xiphoid_process2.png', 'xiphoid_process3.png', 'xiphoid_process4.png', 'xiphoid_process5.png',
    'pubis1.png', 'pubis2.png', 'pubis3.png', 'pubis4.png', 'pubis5.png',
    'ischium1.png', 'ischium2.png', 'ischium3.png', 'ischium4.png', 'ischium5.png',
    'acetabulum1.png', 'acetabulum2.png', 'acetabulum3.png', 'acetabulum4.png', 'acetabulum5.png',
    'femur1.png', 'femur2.png', 'femur3.png', 'femur4.png', 'femur5.png',
    'tibia1.png', 'tibia2.png', 'tibia3.png', 'tibia4.png', 'tibia5.png',
    'fibula1.png', 'fibula2.png', 'fibula3.png', 'fibula4.png', 'fibula5.png',
    'patella1.png', 'patella2.png', 'patella3.png', 'patella4.png', 'patella5.png',
    'metatarsals1.png', 'metatarsals2.png', 'metatarsals3.png', 'metatarsals4.png', 'metatarsals5.png',
    'frontal1.png', 'frontal2.png', 'frontal3.png', 'frontal4.png', 'frontal5.png',
    'ethmoid1.png', 'ethmoid2.png', 'ethmoid3.png', 'ethmoid4.png', 'ethmoid5.png',
    'lacrimal1.png', 'lacrimal2.png', 'lacrimal3.png', 'lacrimal4.png', 'lacrimal5.png',
    'zygomatic1.png', 'zygomatic2.png', 'zygomatic3.png', 'zygomatic4.png', 'zygomatic5.png',
    'sphenoid1.png', 'sphenoid2.png', 'sphenoid3.png', 'sphenoid4.png', 'sphenoid5.png']
show_result_screen = False
correct_dict = {
    **{f'atlas{i}.png': 'Atlas' for i in range(1, 6)},
    **{f'axis{i}.png': 'Axis' for i in range(1, 6)},
    **{f'lumbar{i}.png': 'Lumbar' for i in range(1, 6)},
    **{f'sacrum{i}.png': 'Sacrum' for i in range(1, 6)},
    **{f'coccyx{i}.png': 'Coccyx' for i in range(1, 6)},
    **{f'scapula{i}.png': 'Scapula' for i in range(1, 6)},
    **{f'humerus{i}.png': 'Humerus' for i in range(1, 6)},
    **{f'ulna{i}.png': 'Ulna' for i in range(1, 6)},
    **{f'radius{i}.png': 'Radius' for i in range(1, 6)},
    **{f'metacarpals{i}.png': 'Metacarpals' for i in range(1, 6)},
    **{f'ilium{i}.png': 'Ilium' for i in range(1, 6)},
    **{f'maxilla{i}.png': 'Maxilla' for i in range(1, 6)},
    **{f'mandible{i}.png': 'Mandible' for i in range(1, 6)},
    **{f'temporal{i}.png': 'Temporal' for i in range(1, 6)},
    **{f'parietal{i}.png': 'Parietal' for i in range(1, 6)},
    **{f'occipital{i}.png': 'Occipital' for i in range(1, 6)},
    **{f'vomer{i}.png': 'Vomer' for i in range(1, 6)},
    **{f'hyoid{i}.png': 'Hyoid' for i in range(1, 6)},
    **{f'nasal{i}.png': 'Nasal' for i in range(1, 6)},
    **{f'clavicle{i}.png': 'Clavicle' for i in range(1, 6)},
    **{f'ribs{i}.png': 'Ribs' for i in range(1, 6)},
    **{f'sternum{i}.png': 'Sternum' for i in range(1, 6)},
    **{f'xiphoid_process{i}.png': 'Xiphoid Process' for i in range(1, 6)},
    **{f'pubis{i}.png': 'Pubis' for i in range(1, 6)},
    **{f'ischium{i}.png': 'Ischium' for i in range(1, 6)},
    **{f'acetabulum{i}.png': 'Acetabulum' for i in range(1, 6)},
    **{f'femur{i}.png': 'Femur' for i in range(1, 6)},
    **{f'tibia{i}.png': 'Tibia' for i in range(1, 6)},
    **{f'fibula{i}.png': 'Fibula' for i in range(1, 6)},
    **{f'patella{i}.png': 'Patella' for i in range(1, 6)},
    **{f'metatarsals{i}.png': 'Metatarsals' for i in range(1, 6)},
    **{f'frontal{i}.png': 'Frontal' for i in range(1, 6)},
    **{f'ethmoid{i}.png': 'Ethmoid' for i in range(1, 6)},
    **{f'lacrimal{i}.png': 'Lacrimal' for i in range(1, 6)},
    **{f'zygomatic{i}.png': 'Zygomatic' for i in range(1, 6)},
    **{f'sphenoid{i}.png': 'Sphenoid' for i in range(1, 6)},
}

def load_random_image():
    global bone_image, bone_image_rect
    image_name = random.choice(boneslist)  # Select a random image
    image_path = os.path.join(image_folder, image_name)  # Construct the full path
    bone_image = pygame.image.load(image_path)  # Load the image
    bone_image_rect = bone_image.get_rect(center=(window_width // 2, window_height // 2 - 100))
    return image_name

img = load_random_image()  # Load the initial image

# Function to draw the main quiz screen
def draw_quiz_screen(correct=None):
    screen.fill(PERI)

    # Draw the bone image placeholder
    pygame.draw.rect(screen, (200, 200, 200), image_rect)
    screen.blit(bone_image, bone_image_rect)
    
    # Draw the answer button
    pygame.draw.rect(screen, (220, 220, 220), textbox)
    txt_surface = font.render(text, True, BLACK)
    screen.blit(txt_surface, (textbox.x+5, textbox.y+5))

    
    pygame.display.flip()

def draw_result_screen(is_correct):
    # Choose the color and text based on whether the answer is correct
    result_color = GREEN if is_correct else RED
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

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                draw_result_screen(True)
                show_result_screen = True
            elif event.key == pygame.K_BACKSPACE:
                text = text[:-1]
            else:
                text += event.unicode
    if show_result_screen:
        if is_correct(text, img) == True:
            draw_result_screen(True)
            img = load_random_image()
        else:
            draw_result_screen(False)
        # Wait for a bit before moving on
        pygame.time.wait(2000)
        show_result_screen = False  # Reset the flag
        text = ''
    else:
        draw_quiz_screen()

pygame.quit()
