import pygame
import random
import sys

def maja(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y- ((3/4.0) * kõrgus)), (x,y), (x+laius,y), (x+laius,y-(3/4.0) * kõrgus), (x,y- ((3/4.0) * kõrgus)), (x + laius/2.0,y-kõrgus), (x+laius,y-(3/4.0)*kõrgus)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)

def Uks(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,(y-1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)

def Aken(x,y,laius,kõrgus,pind,värv):
    punktid=[(x,y),(x,y-(1/2)*kõrgus),(x+(1/3)*laius,(y-1/2)*kõrgus),(x+(1/3)*laius,y),(x,y)]
    suurus=random.randint(1,10)
    pygame.draw.lines(pind,värv,False,punktid,suurus)


r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
fon=[r,g,b]


r=random.randint(0,255)
g=random.randint(0,255)
b=random.randint(0,255)
majavarv=[r,g,b]

pind=pygame.display.set_mode([640,480])
pygame.display.set_caption("Juhuslikud objektid + majake")
pind.fill(fon)

maja(100,400,300,400,pind,majavarv)
Uks(100,400,300,400,pind,majavarv)
Aken(250,300,100,100,pind,majavarv)
pygame.display.flip()

for i in range(10):



    kaka4=pygame.Rect(298,197,100,200)
    pygame.draw.rect(pind,(205,133,63),kaka4)

    kaka3=pygame.Rect(370,280,20,20)
    pygame.draw.ellipse(pind,(28,50,0),kaka3)

    kaka3=pygame.Rect(130,210,90,90)
    pygame.draw.rect(pind,(255,255,255),kaka3)

    kaka4=pygame.Rect(170,210,10,90)
    pygame.draw.rect(pind,(2,0,80),kaka4)

    kaka5=pygame.Rect(130,250,90,10)
    pygame.draw.rect(pind,(2,0,80),kaka5)

    kaka3=pygame.Rect(220,20,60,60)
    pygame.draw.ellipse(pind,(255,255,255),kaka3)

    

    pygame.display.flip()
while True:
    event=pygame.event.poll()
    if event.type==pygame.QUIT:
        sys.exit()
pygame.quit()
