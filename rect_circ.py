import pygame
import random
from PIL import ImageColor
import sys

color=input("Enter the color you want to change for the circle ")

color2=input("Enter the color you want to change for the rectangle ")



def greet(color):
    rgb_value=ImageColor.getrgb(color)
    return rgb_value



pygame.init()

screen=pygame.display.set_mode((400,400))



font_system=pygame.font.SysFont("Arial",20)
running=True

def count(count):
    print(count)
    count+=1
    return count


rect_count=0

circle_count=0

font_system2=pygame.font.SysFont("Arial",15)

instuction=font_system2.render(f"Press c for circle\nPress r for rectangle\n press q to quit",True, (0,255,255))
instuction_rect=instuction.get_rect(center=(65,300))

screen.blit(instuction,instuction_rect)


text_surface=font_system.render(f"circle_count: {circle_count}",True,(255,255,255))
text_rect=text_surface.get_rect(center=(65,15))
screen.blit(text_surface,text_rect)
text_surface2=font_system.render(f"rect_count: {rect_count}",True,(255,255,255))
text_rect2=text_surface2.get_rect(center=(65,40))
screen.blit(text_surface2,text_rect2)
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT or (event.type==pygame.KEYDOWN and event.key==pygame.K_q):
            running=False

        elif event.type==pygame.KEYDOWN:
            l=greet(color)
            if event.key==pygame.K_c:
                pygame.draw.rect(screen, (0,0,0), text_rect)
                circle_count=count(circle_count)
                text_surface=font_system.render(f"circle_count: {circle_count}",True,(255,255,255))
                text_rect=text_surface.get_rect(center=(65,15))
                screen.blit(text_surface,text_rect)
                pygame.draw.circle(screen, l, radius=20, center=(random.uniform(130,400),random.uniform(0,400)))
            elif event.key==pygame.K_r:
                p=greet(color2)
                pygame.draw.rect(screen, (0,0,0), text_rect2)
                rect_count=count(rect_count)
                text_surface2=font_system.render(f"rect_count: {rect_count}",True,(255,255,255))
                text_rect2=text_surface2.get_rect(center=(65,40))
                screen.blit(text_surface2,text_rect2)
                pygame.draw.rect(screen, p, (random.uniform(130,400),random.uniform(0,400),20,30))
    pygame.display.update()
    pygame.display.flip()


pygame.quit()
sys.exit()