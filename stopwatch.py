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

    def __init__(self, master=none, cnf=())




    def __click__(self):
        if self.__button('text') == "start":
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
