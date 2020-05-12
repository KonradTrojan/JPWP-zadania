import pygame

'''
    Uzupełnij klasę TextButton
    Napis powinien być pozycjonowany na ekranie względem środkowych współrzędnych napisu
    Przydatne funkcje:
        mpx, mpy = pygame.mouse.get_post() # zwraca współrzędne kursora myszy
        text.get_rect() # zwraca prostokąt otaczający wyrenderowany text
'''

class TextButton:
    def __init__(self, center_x, center_y, font_name, font_size, text, color):
        self.centerX = center_x
        self.centerY = center_y

        self.font = pygame.font.SysFont(font_name, font_size)
        self.text = self.font.render(text, True, color)
        self.textRect = self.text.get_rect()

    def cursor_hover(self):
        # Zwraca True lub False w zależności od tego czy kursor znajduje się nad tekstem
        mpx, mpy = pygame.mouse.get_pos()
        if ((self.textRect.right > mpx > self.textRect.left) and (self.textRect.bottom > mpy > self.textRect.top)) :
            return True
        else:
            return False

    def update(self, text, color):
        self.text = self.font.render(text,True,color)
    def draw(self,win):
        self.textRect.center = (self.centerX, self.centerY)
        win.blit(self.text, self.textRect)
