import tkinter as tk
from tkinter import messagebox
import winsound

class Metronome:
    def __init__(self, root):
        self.bpm=0
        self.root=root
        self.beat=0
        self.playflag=False
        self.var = tk.StringVar()
        self.var.set(self.bpm)
        self.gui()
        
    def gui(self):
        frame=tk.Frame()
        frame.pack()

        label_bpm=tk.Label(frame, text='BPM : ', width=30, height=10)
        entry_bpm=tk.Entry(frame)
        button_bpm=tk.Button(frame, text='Enter', width=30, height=10, command=lambda:self.bpm_input('insert', entry_bpm, label_bpm))

        light_1=tk.Label(frame, width=10, height=5, background='red')
        light_2=tk.Label(frame, width=10, height=5, background='black')
        light_3=tk.Label(frame, width=10, height=5, background='black')
        light_4=tk.Label(frame, width=10, height=5, background='black')


        label_bpm=tk.Label(frame, textvariable=self.var, width=30, height=10)

        button_up=tk.Button(frame, text='▲', width=30, height=10, command=lambda:self.bpm_input('up', entry_bpm, label_bpm))
        button_play=tk.Button(frame, text='▶', width=30, height=10, command=lambda:self.play(light_1, light_2, light_3, light_4))
        button_stop=tk.Button(frame, text='■', width=30, height=10, command=lambda:self.stop())
        button_down=tk.Button(frame, text='▼', width=30, height=10, command=lambda:self.bpm_input('down', entry_bpm, label_bpm))

        label_bpm.grid(row=0, column=1)
        entry_bpm.grid(row=0, column=2, columnspan=2)
        button_bpm.grid(row=0, column=4)
        light_1.grid(row=1, column=1)
        light_2.grid(row=1, column=2)
        light_3.grid(row=1, column=3)
        light_4.grid(row=1, column=4)
        label_bpm.grid(row=2, column=0, columnspan=5)
        button_up.grid(row=3, column=1)
        button_play.grid(row=3, column=2)
        button_stop.grid(row=3, column=3)
        button_down.grid(row=3, column=4)
    
    
    def play(self, light_1, light_2, light_3, light_4):
        if self.playflag!=True:
            self.playflag=True
            self.player(light_1, light_2, light_3, light_4)

    def stop(self):
        self.beat=0
        self.playflag=False

    def bpm_input(self, v, entry_bpm, label_bpm):
        if v=='insert':
            tmp=entry_bpm.get()
            if tmp=='' or int(tmp)<1 or int(tmp)>300:
                self.bpm_alert()
                return
            else:
                self.bpm=int(entry_bpm.get())
                self.var.set(self.bpm)
        else:
            if v=='up':
                if self.bpm==300:
                    self.bpm_alert()
                    return
                self.bpm=self.bpm+1
                self.var.set(self.bpm)
            else:
                if self.bpm==1:
                    self.bpm_alert()
                    return
                self.bpm=self.bpm-1
                self.var.set(self.bpm)
    
    def player(self, light_1, light_2, light_3, light_4):
        if self.playflag:
            self.beat=self.beat+1
            if self.beat==1:
                winsound.Beep(1000,120)
                light_1.configure(background='red')
                light_2.configure(background='black')
                light_3.configure(background='black')
                light_4.configure(background='black')
            else:
                winsound.Beep(500,120)
                if self.beat==2:
                    light_1.configure(background='black')
                    light_2.configure(background='red')
                elif self.beat==3:
                    light_2.configure(background='black')
                    light_3.configure(background='red')
                else:
                    light_3.configure(background='black')
                    light_4.configure(background='red')
                    self.beat=0
            self.root.after(int((60 / self.bpm - 0.1) * 1000), lambda:self.player(light_1, light_2, light_3, light_4))
    
    def bpm_alert(self):
        messagebox.showwarning('bpm warning', '0<bpm<300')

def main():
    window=tk.Tk()
    window.title("Metronome")
    
    Metronome(window)

    window.mainloop()

if __name__ == "__main__":
    main()