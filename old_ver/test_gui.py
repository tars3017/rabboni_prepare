from tkinter import *
def gui():
    # tmp value
    tmpOut = 10
    win = Tk()
    win.title('ball path tracking system')
    win.geometry('700x432')
    win.wm_minsize(width = 700, height = 432)
    win.attributes('-topmost', True)

    startBtn = Button(text = "start", font = "微軟正黑體 12")
    startBtn.pack()

    curV = Label(text = "x軸的速度是: ", height = 1, textvariable = tmpOut, font = "微軟正黑體 12", bg = "#00a8a3", pady = 5)
    curV.pack()

    win.mainloop()

gui()