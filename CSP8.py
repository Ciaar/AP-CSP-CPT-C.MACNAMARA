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
button0 = pygame.Rect (300, 350, 200, 200)
play_button = pygame.Rect(300, 350, 200, 200)
play_text = font.render("Play again", True, (0, 0, 0))

rxn_time = 0
run = True
completed = False
written = False

def start ():
    asking = True
    yes_button = pygame.Rect(200, 400, 150, 100)
    no_button = pygame.Rect(450, 400, 150, 100)
    yes_text = font.render("Yes", True, (0, 0, 0))
    no_text = font.render("No", True, (0, 0, 0))

    while asking:
        screen.fill((30, 30, 30))
        show_text("Would you like to play?", (255, 255, 255), 220, 200)

        pygame.draw.rect(screen, (0, 255, 0), yes_button)
        pygame.draw.rect(screen, (255, 0, 0), no_button)

        screen.blit(yes_text, (yes_button.x + 40, yes_button.y + 30))
        screen.blit(no_text, (no_button.x + 40, no_button.y + 30))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if yes_button.collidepoint(pygame.mouse.get_pos()):
                    asking = False
                elif no_button.collidepoint(pygame.mouse.get_pos()):
                    print("\nPlease comeback again later!")
                    pygame.quit()
                    exit()
        pygame.display.update()
    



def play ():  
    with open('leaderboard.txt', 'r') as file:
        numbers = [float(line.strip()) for line in file if line.strip()] 
    numbers.sort()       
    while len(numbers) < 5:
        numbers.append(float('inf'))
    p1, p2, p3, p4, p5 = numbers[:5]
    start_time = pygame.time.get_ticks()
    random_time = random.randint(3000,10000)
    button_color = (255, 255, 255)
    global run, completed, written, rxn_time, button_text 
    while run:   
        if completed:
            screen.fill((50,215,250))
            time_text = font.render("Your reaction time was: "+str(rxn_time/1000)+" seconds!", True, (255, 255, 255))
            screen.blit(time_text, (100, 250))
            pygame.draw.rect(screen, (255, 255, 255), play_button)
            screen.blit(play_text, (320, 460))
        else:         
            screen.fill((0, 0, 0))
            imp = pygame.image.load("/Users/ciaran/downloads/table/table3.png")
            imp_resized = pygame.transform.scale(imp, (350,350))
            screen.blit(imp_resized, (220,15))
            show_text(str(p1) + " s", (255, 255, 255), 355, 50)
            show_text(str(p2) + " s", (255, 255, 255), 355, 112)
            show_text(str(p3) + " s", (255, 255, 255), 355, 172)
            show_text(str(p4) + " s", (255, 255, 255), 355, 235)
            show_text(str(p5) + " s", (255, 255, 255), 355, 295)      
            elapsed_time = pygame.time.get_ticks() - start_time
            if elapsed_time > random_time:
                button_color = (0, 255, 0)
            pygame.draw.rect(screen, button_color, button)
            pygame.draw.rect(screen, button_color, button0)
            screen.blit(button_text, (340, 355))
            screen.blit(button_text, (340, 355))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position=pygame.mouse.get_pos()
                if not completed and (button.collidepoint(mouse_position) or button0.collidepoint(mouse_position)):
                    if elapsed_time - random_time < 0:
                         buttonyes_text = font.render("Not Yet", True, (255, 0, 0))
                         screen.blit(buttonyes_text,(340,320))
                    else:
                         rxn_time = elapsed_time - random_time
                         completed = True
                         if not written:
                             with open('leaderboard.txt', 'a') as file1:
                                 written = True
                elif completed and play_button.collidepoint(mouse_position):
                         completed = False
                         written = False
                         rxn_time = 0
                         pygame.display.update()
                         return False
        pygame.display.update()
start ()
while True:
    quit = play()
    if quit:
        break
pygame.quit()
exit()


