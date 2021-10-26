from tkinter import Tk, Label, mainloop, BOTH
from time import strftime


class Clock(Tk):
    def __init__(self):
        super().__init__()

        self.font = ("Digital", 40)
        self.title("Clock")
        self.draw()

    def draw(self):
        self.lbl = Label(
            self,
            text = self.return_time(),
            font = self.font,
            bg = "#02122c",
            fg = "#c7dbfb"
        )

        self.lbl.pack(fill = BOTH, expand = True)
        self.update_time()

    def return_time(self):
        return strftime("%H:%M:%S")

    def update_time(self):
        self.lbl.configure(text = self.return_time())
        self.after(100, self.update_time)

if __name__ == "__main__":
    root = Clock()
    root.mainloop()
