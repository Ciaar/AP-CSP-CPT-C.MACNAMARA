#imports the module, pygame, so that I can have more fuctions and create a screen that can display images if needed
import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Reaction Time Tester')

font = pygame.font.SysFont(None, 50)

def show_text(msg, color, x=SCREEN_WIDTH//2, y=SCREEN_HEIGHT//2):
    text = font.render(msg, True, color)
    screen.blit(text, (x, y))

button = pygame.Rect((300, 350, 200, 200))
button_text = font.render("Button", True, (0, 0, 0))

rxn_time = 0

with open('leaderboard.txt', 'r') as file:
    numbers = file.readlines()

numbers.sort()
p1= numbers [0]
p2= numbers [1] 
p3= numbers [2]
p4= numbers [3] 
p5= numbers [4] 


run = True
completed = False
written = False

def play ():
    
    start_time = pygame.time.get_ticks()
    random_time = random.randint(3000,10000)
    button_color = (255, 255, 255)

    global run, completed, written, rxn_time, button_text
    
    while run:
       
        if completed:
            screen.fill((50,215,250))
            time_text = font.render("Your reaction time was: "+str(rxn_time/1000)+" seconds!", True, (255, 255, 255))
            screen.blit(time_text, (100, 250))
        else:
               
            screen.fill((0, 0, 0))
            imp = pygame.image.load("/Users/ciaran/downloads/table/table3.png")
            imp_resized = pygame.transform.scale(imp, (350,350))
            screen.blit(imp_resized, (220,15))
            show_text(str(p1[0:len(p1)-1]), (255, 255, 255), 355, 50)
            show_text(str(p2[0:len(p2)-1]), (255, 255, 255), 355, 112)
            show_text(str(p3[0:len(p3)-1]), (255, 255, 255), 355, 172)
            show_text(str(p4[0:len(p4)-1]), (255, 255, 255), 355, 235)
            show_text(str(p5[0:len(p5)-1]), (255, 255, 255), 355, 295)
            

           
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time > random_time:
                button_color = (0, 255, 0)
           

            pygame.draw.rect(screen, button_color, button)
            screen.blit(button_text, (340, 355))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                 mouse_position=pygame.mouse.get_pos()
                 if button.collidepoint(mouse_position):
                    if elapsed_time - random_time < 0:
                         buttonyes_text = font.render("Not Yet", True, (255, 0, 0))
                    else:
                         rxn_time = elapsed_time - random_time
                         completed = True
                         if not written:
                             with open('leaderboard.txt', 'a') as file1:
                                 file1.write('\n' + str(rxn_time / 1000))
                                 written = True

                         

        pygame.display.update()
        
print("\nWelcome to Reaction Time Tester!")
print("Current leaderboard:\n\nfirst place: "+str(p1)+"\nsecond place: "+p2+"_\nthird place: "+str(p3)+"\nfourth place: "+str(p4)+"\nfifth place: "+str(p5))

question=input("Would you like to play? (yes/no)").lower()
if question == "yes":
    play()
