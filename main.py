from tkinter import Button, Tk, Label, Menu, Frame, mainloop
from time import strftime, strptime
from tkinter.constants import BOTTOM, X, SUNKEN, BOTH


class Clock(Tk):
    def __init__(self):
        super().__init__()

        self.font = ("Terminal", 40)
        self.title("Clock")
        self.minsize(300, 80)

        self.second = 0
        self.minute = 0

        self.draw()

    def draw(self):
        self.frame_btn = Frame(self)
        
        self.toggle_btn = Button(
            self.frame_btn,
            text = "Open the Clock",
            font = ("Digital", 14),
            relief = SUNKEN,
            bd = 3,
            bg = "#02122c",
            activebackground = "#02104a",
            activeforeground = "#c7dbfb",
            fg = "#c7dbfb",
            command = self.toggle_clock
        )

        self.toggle_btn.pack(fill = BOTH, expand = True)
        self.frame_btn.pack(side = BOTTOM, fill = BOTH, expand=True)

    def toggle_clock(self):
        self.frame_cl = Frame(self)

        try :
            self.frame1_sw.destroy()
        except:
            pass

        self.clock_lbl = Label(
            self.frame_cl,
            text = self.return_time(),
            font = self.font,
            bg = "#02122c",
            fg = "#c7dbfb"
        )

        self.clock_lbl.pack(fill = BOTH, expand = True)
        self.frame_cl.pack(fill = BOTH, expand = True)
        self.toggle_btn.config(text = "Switch to Stopwatch", command = self.toggle_stopwatch)

        self.update_time()

    def toggle_stopwatch(self):
        self.frame1_sw = Frame(self)

        try:
            self.frame_cl.destroy()
        except:
            pass

        self.sw_lbl = Label(
            self.frame1_sw,
            text = "00:00",
            font = self.font,
            bg = "#02122c",
            fg = "#c7dbfb"
        )

        self.sw_lbl.pack(fill = BOTH, expand=True)
        self.frame1_sw.pack(fill = BOTH, expand = True)
        
        self.update_stopwatch()
        self.toggle_btn.config(text = "Switch to Clock", command = self.toggle_clock)

    def return_time(self):
        return strftime("%H:%M:%S")

    def update_stopwatch(self):
        self.second += 1
        
        if self.second % 60 == 0:
            self.second = 0
            self.minute += 1

        try:
            self.sw_lbl.config(text = f"{self.minute}:{self.second}")
        except:
            pass
        self.after(1000, self.update_stopwatch)

    def update_time(self):
        try :
            self.clock_lbl.configure(text = self.return_time())
            self.after(200, self.update_time)
        except:
            pass

if __name__ == "__main__":
    root = Clock()
    root.mainloop()
