import tkinter as tk
import time

class StopWatch(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        # GUI設定
        master.geometry("300x150")
        master.title("ストップウォッチ")
        master.config(bg="black")

        self.startTime = time.time()
        self.stopTime = 0.0
        self.elapsedTime = 0.0
        self.playTime = False

        # キャンバスエリア
        self.canvas = tk.Canvas(master, width=290,height=80,bg="skyblue")
        #キャンバスバインド
        self.canvas.place(x=3,y=10)

        tk.Button(master,text="リセット",command=self.resetButtonClick,width=10).place(x=10, y=110)
        tk.Button(master,text="スタート/ストップ",command=self.startStopButtonClick,width=20).place(x=110, y=110)
        # tk.Button(master,text="ストップ",command=self.stopButtonClick,width=10).place(x=210, y=110)

        master.after(50,self.update)
    
    def startStopButtonClick(self):
        if not self.playTime:
            self.watchStart()
        else:
            self.watchStop()

    def watchStart(self):
        self.startTime = time.time()-self.elapsedTime
        self.playTime = True
    
    def watchStop(self):
        self.stopTime = time.time()-self.startTime
        self.playTime=False
    
    def resetButtonClick(self):
        self.startTime = time.time()
        self.stopTime = 0.0
        self.elapsedTime=0.0
        self.playTime=False
    
    def update(self):
        self.canvas.delete("Time")
        if self.playTime:
            self.elapsedTime = time.time()-self.startTime
            self.canvas.create_text(280,40,text=round(self.elapsedTime,1),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")
        else:
            self.canvas.create_text(280,40,text=round(self.stopTime,1),font=("Helvetica",40,"bold"),fill="black",tag="Time",anchor="e")
        self.master.after(50,self.update)

    
def stop_watch_main():
    win = tk.Tk()
    app = StopWatch(master = win)
    app.mainloop()
    
if __name__ == "__main__":
    stop_watch_main()


