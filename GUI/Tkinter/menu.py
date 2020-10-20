import tkinter as tk
from stop_watch  import stop_watch_main
from timer import timer_main
from block_break import block_break_main

class MainWindow():
    counter = 0
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("main munu")
        
        button_1 = tk.Button(self.root, text="stop watch app", 
                                command=self.create_stop_watch)
        button_2 = tk.Button(self.root, text="timer app", 
                                 command=self.create_timer)
        button_3 = tk.Button(self.root, text="block break app", 
                                 command=self.create_block_break)
        button_1.pack(side="top")
        button_2.pack()
        button_3.pack()
 
        self.root.mainloop()
        
    def create_stop_watch(self):
        stop_watch_main()
    
    def create_timer(self):
        timer_main()
    
    def create_block_break(self):
        block_break_main()
 
if __name__ == "__main__":
        MainWindow()
