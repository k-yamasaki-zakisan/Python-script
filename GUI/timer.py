import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()
    
    

def stop_timer_main():
    win = tk.Tk()
    app = Application(master = win)
    app.mainloop()
    
if __name__ == "__main__":
    stop_timer_main()