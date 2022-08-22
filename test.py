import threading
import time
import tkinter as tk
from tkinter import ttk

class A(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        i = 0
        while True:
            print("hello world")
            i += 1
            if i > 10:
                break
            time.sleep(1)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Thread Test')
        self.geometry('400x200')
        self.grid_columnconfigure(0,weight=1)
        self.grid_rowconfigure(0,weight=1)

        self.button = ttk.Button(text='Run', command=self.run)
        self.button.grid(padx=10,pady=10,column=0, row=0, sticky=tk.NSEW)

    def run(self):
        a = A()
        a.start()
        self.monitor(a)

    def monitor(self, thread):
        if thread.is_alive():
            print("alive")
            self.after(100, lambda: self.monitor(thread))
        else:
            print("done")

if __name__ == '__main__':
    app = App()
    app.mainloop()