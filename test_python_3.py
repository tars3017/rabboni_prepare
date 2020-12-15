from vpython import *
from rabboni import *
import timeit
import numpy

rabo = Rabboni(mode = "USB") #先宣告一個物件(這邊宣告它叫rabo)
rabo.connect() #透過USB連接裝置,若抓不到會報錯 (void)
print ("Status(0->unconnected,1->connected):",rabo.Status)
rabo.read_data() 
start=timeit.default_timer()

try:
    while True:
        rabo.print_data()

except KeyboardInterrupt:
    rabo.disconnect()
    Xa=rabo.Accx_list
    Ya=rabo.Accy_list
    Za=rabo.Accz_list
    end=timeit.default_timer()
    datasize=len(Xa)
    Vx = 0
    Vy = 0
    Vz = 0
    dt = 800 #畫面更新時間(sec)
    t = 0
    tim = 0
    i=1
    
    constant = 4
    scene = canvas(title='1', width=800, height=800, x=0, y=0, center=vector(1,0.8,0), background=vector(0.5,0.6,0.5))
    # floor = box(pos=vector(0,-(0.005)/2,0), length=0.3, height=0.005, width=0.1)
    ball = sphere(pos=vector(0,0,0), radius=0.5)
    pointer1 = arrow(pos=vector(-10,0,0),axis=vector(20,0,0),shaftwidth=0.05,color=color.red)
    pointer2 = arrow(pos=vector(0,-10,0),axis=vector(0,20,0),shaftwidth=0.05,color=color.blue)
    pointer3 = arrow(pos=vector(0,0,-10),axis=vector(0,0,20),shaftwidth=0.05,color=color.green)
    for i in range(datasize-1):
        sleep(20/1000)
        #if(abs(Xa[i])<abs(Za[i])and abs(Ya[i])<abs(Za[i])):
        #    pt = points(color=color.black,pos=vector(0,0,0),shape="quare")
        
        # Vx += (Xa[i+1]-Xa[i]) * dt 
        # Vy += (Ya[i+1]-Ya[i]) * dt 
        # Vz += (Za[i+1]-Za[i]) * dt 
                   
        ball.pos.x += (Xa[i+1]-Xa[i]) * constant
        ball.pos.y += (Ya[i+1]-Ya[i]) * constant
        ball.pos.z += (Za[i+1]-Za[i]) * constant
        print(ball.pos.x,' ',ball.pos.y,' ',ball.pos.z) 
        tim += dt
        i+=1
    ball.pos.x=0
    ball.pos.y=0
    ball.pos.z=0
    print('finish')
    # rabo.disconnect()
    # rabo.stop()