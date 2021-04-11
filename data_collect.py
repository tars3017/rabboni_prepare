# -*- coding: UTF-8 -*-
from rabboni import *
import timeit
import matplotlib.pyplot as plt
rabo = Rabboni(mode = "USB") #先宣告一個物件
rabo.connect()
cnt=0
#rabo.set_sensor_config(acc_scale=16,gry_scale=2000,rate=500,threshold=10000)
#rabo.set_sensor_config(acc_scale=16,gyr_scale=500,rate=500,threshold=10000)
rabo.read_data()
start=timeit.default_timer()

# 讀取資料 必跑
try:
    while True:#一直打印資料 直到結束程式
        cnt+=1
        rabo.print_data()#print資料

except KeyboardInterrupt:#結束程式
    print('Shut done!')
    print (rabo.Accx_list)#印出到結束程式時的所有Accx值

    rabo.stop()#停止dongle
    rabo.write_csv(data = rabo.Accx_list,file_name ="AccX")#將Accx寫出csv檔
    rabo.write_csv(data = rabo.Accy_list,file_name ="AccY")#將Accy寫出csv檔
    rabo.write_csv(data = rabo.Accz_list,file_name ="AccZ")#將Accz寫出csv檔
    rabo.write_csv(data = rabo.Accx_list,file_name ="AccX")#將Accx寫出csv檔
    rabo.write_csv(data = rabo.Gyrx_list,file_name ="GyrX")#將Gyrx寫出csv檔
    rabo.write_csv(data = rabo.Gyry_list,file_name ="GyrY")#將Gyrx寫出csv檔
    rabo.write_csv(data = rabo.Gyrz_list,file_name ="GyrZ")#將Gyrx寫出csv檔

finally:
    #rabo.stop()
    end=timeit.default_timer()
    print("total time : ",end-start,'\n')
    print("data size : ",cnt,'\n')
    print("data per sec : ",(end-start)/cnt)
    Rx = []
    Ry = []
    Rz = []
    Max = 0
    sepTime = (end-start) / cnt
    pos = 0
    for i in rabo.Accx_list:
        pos += sepTime * sepTime * abs(i)
        Rx.append(pos * 10)
        Max = max(Max, pos * 10)
    pos = 0
    for i in rabo.Accy_list:
        pos += sepTime * sepTime * i
        Ry.append(pos * 10)
        #Max = max(Max, pos * 10)
    pos = 0
    for i in rabo.Accz_list:
        pos += sepTime * sepTime * i
        Rz.append(pos * 10)
        Max = max(Max, pos * 10)
    plt.title('X-Z/X-Y trace figure')
    plt.xlabel('X displacement')
    plt.plot(Rx, Rz, label='Z displacement')
    plt.plot(Rx, Ry, label='Y displacement')
    plt.xlim(0, 0.5)
    plt.ylim(-0.5, 0.5)
    plt.legen()
    plt.show()
    # maybe try to use the opposite huge accleration as the timing to stop