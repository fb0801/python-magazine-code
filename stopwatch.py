#make a python stop watch

#imprt our modules
import time
import tkinter


class StopWatch(tkinter.Frame):
    @classmethod
    def main(cls):
        tkinter.nodefaultroot()
        root=tkinter.Tk()
        root.title('stopwatch')#title of the tkinter widget
        root.resizeable(true, false) #change window size
        root.grid
