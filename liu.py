from vpython import *
from rabboni import *
import numpy
import time
# import timeit
def sigmoid(x):
    return 1.0 / (1 + numpy.exp(-x)) * 10
rabo = Rabboni(mode = "USB") #先宣告一個物件(這邊宣告它叫rabo)
rabo.connect() #透過USB連接裝置,若抓不到會報錯 (void)
print ("Status(0->unconnected,1->connected):",rabo.Status)
rabo.read_data() 
# start=timeit.default_timer()
adjustX = 0
adjustY = 0
adjustZ = 0
counter = 0
print("adjusting...")
sleep(5)
rabo.disconnect()
print(rabo.Accz_list)
print("===========================")
adjustX = numpy.mean(rabo.Accx_list)
adjustY = numpy.mean(rabo.Accy_list)
adjustZ = numpy.mean(rabo.Accz_list)
print(adjustX, adjustY, adjustZ)

rabo.connect()
rabo.read_data()
print("start recording")
start = time.time()
Xa = []
Ya = []
Za = []
dt = 0.01
while(time.time() - start <= 10):
    sleep(dt)
    Xa.append(rabo.Accx)
    Ya.append(rabo.Accy)
    Za.append(rabo.Accz)
rabo.disconnect()
print("end...")
# end=timeit.default_timer()
datasize=len(Xa)
Vx = 0
Vy = 0
Vz = 0
# dt = (end-start)/datasize #畫面更新時間(sec)
# t = 0
# tim = 0
# i=0
g = 10
multiple = 1
scene = canvas(title='1', width=800, height=800, x=0, y=0, center=vector(1,0.8,0), background=vector(0.5,0.6,0.5))
# floor = box(pos=vector(0,-(0.005)/2,0), length=0.3, height=0.005, width=0.1)
ball = sphere(pos=vector(0,0,0), radius=0.5)
pointer1 = arrow(pos=vector(-10,0,0),axis=vector(20,0,0),shaftwidth=0.05,color=color.red)
pointer2 = arrow(pos=vector(0,-10,0),axis=vector(0,20,0),shaftwidth=0.05,color=color.blue)
pointer3 = arrow(pos=vector(0,0,-10),axis=vector(0,0,20),shaftwidth=0.05,color=color.green)
V0x = 0 
V0y = 0 
V0z = 0
preAx = adjustX
preAy = adjustY
preAz = adjustZ
Sx = 0
Sy = 0
Sz = 0
for i in range(len(Xa)):
    # rate(20)
    sleep(dt)
    Vx += (Xa[i]-adjustX)* dt * g
    Vy += (Ya[i]-adjustY) * dt * g  
    Vz += (Za[i]-adjustZ) * dt * g 
    Sx = (V0x * dt + 0.5 * (Xa[i]-preAx) * dt * dt) * multiple
    Sy = (V0y * dt + 0.5 * (Ya[i]-preAy) * dt * dt) * multiple
    Sz = (V0z * dt + 0.5 * (Za[i]-preAz) * dt * dt) * multiple
    print(Sx,' ',Sy,' ',Sz)            
    ball.pos.x += Sx
    ball.pos.y += Sy 
    ball.pos.z += Sz
    V0x = Vx
    V0y = Vy 
    V0z = Vz
    preAx = Xa[i]
    preAy = Ya[i]
    preAz = Za[i]

# ball.pos.x=0
# ball.pos.y=0
# ball.pos.z=0
print('finish')