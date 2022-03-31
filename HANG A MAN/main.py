from math import degrees
from pydoc import text
import pygame
import math
import random

pygame.font.init()

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)

#fonts
LETTER_FONT = pygame.font.SysFont('comicsans', 20)
WORD_FONT = pygame.font.SysFont('comicsans', 40)
TITLE_FONT = pygame.font.SysFont('comicsans', 50)

#Screen Size
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("HANG-A-MAN")


#Alphabet buttons
RADIUS = 20
GAP = 15
letters = []
startx = round((WIDTH-(RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
  x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
  y = starty + ((i // 13) * (GAP + RADIUS * 2))
  letters.append([x,y, chr(A + i), True])


#Hangman images
images = []
for i in range(7):
  image = pygame.image.load("hangman"+str(i)+".png")
  images.append(image)

hangman_status  = 0

def getRandomWord():
  words = ['python', 'java', 'javascript', 'html', 'program', 'code', 'database', 'developer', 'dart', 'flutter', 'data', 'algorithm', 'css', 'pygame']
  word = random.choice(words)
  return word

word = getRandomWord().upper()
guessed = []

#FPS 
FPS = 60
clock = pygame.time.Clock()
run = True

#Draw Function
def draw():
  win.fill(WHITE)

  #draw the title
  text = TITLE_FONT.render("HANG-A-MAN",1,BLACK)
  win.blit(text,(WIDTH/2 - text.get_width()/2, 20))

  #draw the word
  display_word = ""
  for letter in word:
    if letter in guessed:
      display_word += letter + " "
    else:
      display_word += "_ "
  text = WORD_FONT.render(display_word, 1, BLACK)
  win.blit(text, (350, 200))


  #draw the alphabet buttons
  for letter in letters:
    x, y, ltr, visble = letter
    if visble:
      pygame.draw.circle(win, BLACK, (x,y), RADIUS, 3)
      text = LETTER_FONT.render(ltr,1,BLACK)
      win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))
  
  #draw the images
  win.blit(images[hangman_status],(80,100))
  pygame.display.update()

#show messages
def message(msg):
  pygame.time.delay(1000)
  win.fill(WHITE)
  text = WORD_FONT.render(msg, 1, BLACK)
  win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
  pygame.display.update()
  pygame.time.delay(4000)


#GAME_LOOP
while run:
  clock.tick(FPS)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        m_x , m_y = pygame.mouse.get_pos()
        for letter in letters:
          x, y, ltr, visible = letter
          dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
          if dis < RADIUS:
            letter[3] = False
            guessed.append(ltr)
            if ltr not in word:
              hangman_status += 1

  draw()

  won = True
  for letter in word:
    if letter not in guessed:
      won = False
      break

  if won:
    message("You WON! ")
    break

  if hangman_status == 6:
    message("You LOST! ")
    break

pygame.quit()