import pygame


pygame.init()
screen = pygame.display.set_mode((600, 500))
pygame.display.set_caption('Baseball!!!')
COLOR_INACTIVE = pygame.Color('white')
COLOR_ACTIVE = pygame.Color('black')
FONT = pygame.font.Font(None, 32)


class InputBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        # Resize the box if the text is too long.
        width = max(150, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)


class First_screen():
    
    def __init__(self,screen):
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("pic/penguin.jpg")
        self.background = pygame.transform.smoothscale(self.background,(600,500))
        screen.blit(self.background,(0,0))
        self.input_box_name = InputBox(60,140,50,32)
        self.input_box_height = InputBox(400,140,50,32)
        self.input_boxes = [self.input_box_name, self.input_box_height]
        pygame.display.update()
        self.done = False

    def routine(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                for box in self.input_boxes:
                    box.handle_event(event)

            for box in self.input_boxes:
                box.update()

            screen.blit(self.background,(0,0))

            for box in self.input_boxes:
                box.draw(screen)

            text = FONT.render("Enter your name",True,(0,0,0))
            screen.blit(text, (43,115))
            text = FONT.render("Enter your height", True, (0,0,0))
            screen.blit(text, (390,115))

            pygame.display.flip()
            self.clock.tick(30)



if __name__ == '__main__':
    f = First_screen(screen)
    f.routine()
    pygame.quit()