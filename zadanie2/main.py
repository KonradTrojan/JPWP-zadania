import pygame

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(" :-) ")
bg = pygame.image.load("background.png")
bg = pygame.transform.scale(bg, (800, 600))

run = True

positionX = 200
positionY = 300

pos = pygame.Vector2(200, 300)

window.blit(bg, (0, 0))
pygame.draw.circle(window, (255, 0, 0), (positionX,positionY), 15)
pygame.display.update()

clock = pygame.time.Clock()

pygame.draw.circle(window, (255, 0, 0), (300, 300), 15)
pygame.display.update()

positionX_stoj = 500
positionY_stoj = 500

speed = 2

move_map = {pygame.K_LEFT: pygame.Vector2(-1, 0),
            pygame.K_RIGHT: pygame.Vector2(1, 0),
            pygame.K_UP: pygame.Vector2(0, -1),
            pygame.K_DOWN: pygame.Vector2(0, 1)}



while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT: run = False

    window.blit(bg, (0, 0))
    
    #stojąca kulka
    if (pos[0] > positionX_stoj - 30 and pos[0] < positionX_stoj + 30) and (pos[1] > positionY_stoj - 30 and pos[1] < positionY_stoj + 30):
        pygame.draw.circle(window, (255, 0, 0), (positionX_stoj, positionY_stoj), 15)
    else:
        pygame.draw.circle(window, (255, 255,255), (positionX_stoj, positionY_stoj), 15)
    #ruszająca się kulka
    pygame.draw.circle(window, (255, 0, 0), [int(x) for x in pos], 15)

    pygame.display.flip()


    pressed = pygame.key.get_pressed()
    move_vector = pygame.Vector2(0, 0)
    for m in (move_map[key] for key in move_map if pressed[key]):
        move_vector += m


    if move_vector.length() > 0:
        move_vector.normalize_ip()


    move_vector *= speed


    pos += move_vector

    clock.tick(60)
