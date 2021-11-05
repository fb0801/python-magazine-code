#make a python digital clock

#imprt our modules
import time
import tkinter as tk


def tick(time1=""):
    #get the current time
    time2 = time.strftime('%H:%M:%S') #format for the time
    if time2 != time1:
        time1 = time2
        clock.config(text=time2)

    clock.config(text=time2)

root=tk.Tk()
#create a label for the clock
clock=tk.Label(root,font=('arial',20,'bold'), bg='green')


btn_1 = Button(root, text='Refresh', command=tick)



#placement of the clock
clock.pack(fill='both',expand=1)
#put btns on the screeen
btn_1.pack()

tick()#call the tick func
root.mainloop()
