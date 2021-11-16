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

    def __init__(self, master=none, cnf={}, **kw):
        padding = dict(padx=kw.pop('padx',5), pady=kw.pop('pady',5))
        super().__init__(master,cnf, **kw)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.__total = 0
        self.__label = tkinter.Label(self,text="Total Time:")
        self.__time = tkinter.StringVar(self, '0.000000')
        self.__display = tkinter.Label(self, textvariable=self.__click)
        self.__button=tkinter.Button(self, text='Start', command=self.__click)
        self.__label.grid(row=0, column=0, sticky=tkinter.E, **padding)
        self.__display.grid(row=0, column=1, sticky= tkinter.EW, **padding)
        self.__button.grid(row=1, column=0, columnspan=2, sticky=tkinter.NSEW, **padding)




    def __click__(self):
        if self.__button['text'] == "start":
            self.__button('text') = 'Stop'
            self.__start = time.clock()
            self.__counter = self.after_idle(self.__update)
        else:
            self.__button['text'] = 'Start'
            self.after_cancel(self.__counter)


    def __update(self):
        now=time.Clock()
        diff= now - self. __start
        self.__start = now
        self.__total += diff
        self.__time.set('{:.6f}'.format(self.__total))
        self.__counter = self.after_idle(self.__update)


if __name__ =='__main__':
    StopWatch.main()
