import tkinter as tk
from stop_watch  import stop_watch_main
from timer import stop_timer_main

class MainWindow():
    counter = 0
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Test")
        
        button_1 = tk.Button(self.root, text="stop watch app", 
                                command=self.create_stop_watch)
        button_2 = tk.Button(self.root, text="timer app", 
                                 command=self.create_timer)
        button_1.pack(side="top")
        button_2.pack(side="bottom")
 
        self.root.mainloop()
        
    def create_stop_watch(self):
        stop_watch_main()
    
    def create_timer(self):
        stop_timer_main()
 
if __name__ == "__main__":
        MainWindow()
