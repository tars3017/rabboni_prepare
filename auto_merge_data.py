import csv
import os
import numpy
def mergeFile():
    cur = os.getcwd()
    final = [[]]
    def write_in_file(file):
        with open(file, 'r', newline='') as f:
            rows = csv.reader(f)
            for row in rows:
                final.append(row)
                break

    title = ["Packet number", "GyroscopeX", "GyroscopeY", "GyroscopeZ", "AcceleromotorX", "AcceleromotorY", "AcceleromotorZ"]
    with open('.\\merge.csv', 'w', newline='') as f:
        csvwriter = csv.writer(f)
        csvwriter.writerow(title)
    print("done")
    for filename in os.listdir(cur):        
        if(filename.startswith("GyrX")):
            with open(filename, 'r', newline='') as f:
                rows = csv.reader(f)
                packet = []
                final.append([])
                for row in rows:
                    for i in range(len(row)):
                        packet.append(i+1)
                        final[1].append(row[i])
                final[0] = packet
            break
    for filename in os.listdir(cur):
        if(filename.startswith("GyrY")):
            write_in_file(filename)
            break
    for filename in os.listdir(cur):
        if(filename.startswith("GyrZ")):
            write_in_file(filename)
            break
    for filename in os.listdir(cur):
        if(filename.startswith("AccX")):
            write_in_file(filename)
            break
    for filename in os.listdir(cur):
        if(filename.startswith("AccY")):
            write_in_file(filename)
            break
    for filename in os.listdir(cur):
        if(filename.startswith("AccZ")):
            write_in_file(filename)
            break
    # print(len(final))
    npArray = numpy.array(final)
    trans = npArray.T
    transL = trans.tolist()
    # print(transuL)
    # f = open('.\merge.csv', 'w')
    # f.close
    for i in transL:
        print(i)
        with open('.\merge.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(i)
mergeFile()