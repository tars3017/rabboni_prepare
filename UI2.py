import pygame, os, time, random
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
                if event.key == pygame.K_BACKSPACE:
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
    
    def return_str(self):
        return self.text

class First_screen():
    
    def __init__(self,screen):
        self.clock = pygame.time.Clock()
        self.background = pygame.image.load("pic/penguin.jpg")
        self.background = pygame.transform.smoothscale(self.background,(600,500))
        self.button = pygame.image.load("pic/next.png")
        self.button = pygame.transform.smoothscale(self.button,(200,170)).convert_alpha()
        self.input_box_name = InputBox(60,140,50,32)
        self.input_box_height = InputBox(400,140,50,32)
        self.input_boxes = [self.input_box_name, self.input_box_height]
        self.done = False
        self.remove_screen = False

    def routine(self):
        while not self.done:

            screen.blit(self.background,(0,0))
            screen.blit(self.button,(200,300))
            text = FONT.render("Enter your name",True,(0,0,0))
            screen.blit(text, (43,115))
            text = FONT.render("Enter your height", True, (0,0,0))
            screen.blit(text, (390,115))

            for box in self.input_boxes:
                box.update()
                box.draw(screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                for box in self.input_boxes:
                    box.handle_event(event)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    if (267 < pos[0] < 322) and (316 < pos[1] < 360) :
                        name,height = self.input_boxes[0].return_str(), self.input_boxes[1].return_str()
                        #go to next screen
                        self.background.fill((255,255,255))
                        screen.blit(self.background,(0,0))
                        print(name,height)
                        self.done = True

            pygame.display.flip()
            self.clock.tick(30)


class Menu():
    
    def __init__(self,screen):
        self.background = pygame.image.load("pic/menu.JPG")
        self.background = pygame.transform.smoothscale(self.background.convert_alpha(),(600,500))
        self.start_button = pygame.image.load("pic/white_menu_button.JPG")
        self.start_button = pygame.transform.smoothscale(self.start_button.convert_alpha(),(200,100))
        self.quit_button = pygame.image.load("pic/quit.JPG")
        self.quit_button = pygame.transform.smoothscale(self.quit_button.convert_alpha(),(200,100))
        
        self.done = False

    def routine(self):
        while not self.done:
            screen.blit(self.background,(0,0))
            screen.blit(self.start_button,(349,67))
            screen.blit(self.quit_button,(349, 350))
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if (349 < pygame.mouse.get_pos()[0] < 550) and (69 < pygame.mouse.get_pos()[1] < 169):
                        self.done = True
                        screen.fill((255,255,255))        
                        # next screen
                    if (349 < pygame.mouse.get_pos()[0] < 550) and (350 < pygame.mouse.get_pos()[1]<450):
                        pygame.quit()
            pygame.display.flip()

from Gait_Tracking import script
# import Collect
from rabboni import Rabboni
from auto_merge_data import mergeFile
import timeit
def collect():
    
    rabo = Rabboni(mode = "USB") #先宣告一個物件
    rabo.connect()
    cnt=0
    go = 1
    # rabo.set_sensor_config(acc_scale=16,gry_scale=2000,rate=500,threshold=10000)
    # rabo.set_sensor_config(acc_scale=16,gyr_scale=500,rate=500,threshold=10000)
    start=timeit.default_timer()

    rabo.read_data()
    while go:
        #一直打印資料 直到按按鈕
        cnt+=1
        rabo.print_data()#print資料
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                go = 0
                break

    print('Shut done!')
    end=timeit.default_timer()
    # print (rabo.Accx_list)#印出到結束程式時的所有Accx值
    rabo.stop()
    
    print("total time : ",end-start,'\n')
    print("data size : ",cnt,'\n')
    print("data per sec : ",(end-start)/cnt)
    rabo.stop()#停止dongle
    rabo.write_csv(data = rabo.Accx_list,file_name ="AccX")#將Accx寫出csv檔
    rabo.write_csv(data = rabo.Accy_list,file_name ="AccY")#將Accy寫出csv檔
    rabo.write_csv(data = rabo.Accz_list,file_name ="AccZ")#將Accz寫出csv檔
    rabo.write_csv(data = rabo.Accx_list,file_name ="AccX")#將Accx寫出csv檔
    rabo.write_csv(data = rabo.Gyrx_list,file_name ="GyrX")#將Gyrx寫出csv檔
    rabo.write_csv(data = rabo.Gyry_list,file_name ="GyrY")#將Gyrx寫出csv檔
    rabo.write_csv(data = rabo.Gyrz_list,file_name ="GyrZ")#將Gyrx寫出csv檔
    mergeFile()
    script.run()


class Ball_screen():

    def __init__(self,screen):
        self.background = pygame.image.load("pic/strike.jpg")
        self.background = pygame.transform.smoothscale(self.background,(600,500))
        self.baseball_pic = pygame.image.load("pic/baseball.png")
        self.baseball_pic = pygame.transform.smoothscale(self.baseball_pic.convert_alpha(),(30,30))
        self.stop_button = pygame.image.load("pic/stop.jpg")
        self.stop_button = pygame.transform.smoothscale(self.stop_button.convert_alpha(),(200,100))

    def routine(self):
        screen.blit(self.background,(0,0))
        screen.blit(self.baseball_pic,(random.randint(280,500),random.randint(191,400)))
        screen.blit(self.stop_button,(300,20))
        pygame.display.flip()
        collect()
        
        

if __name__ == '__main__':
    f = First_screen(screen)
    a = Menu(screen)
    b = Ball_screen(screen)

    f.routine()
    while 1:
        a.done = False
        a.routine()
        b.routine()

    pygame.quit()