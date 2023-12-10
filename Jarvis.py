import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
import os
from Main import Main

class ImageLabel(tk.Label):
    
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []
 
        try:
            for i in count(1):
                frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)
 
        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100
 
        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()
 
    def unload(self):
        self.config(image=None)
        self.frames = None
 
    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

def run():
    os.system('python Main.py')
 
#demo :
root = tk.Tk()

lbl = ImageLabel(root)
lbl.pack()
lbl.load('Aqua.gif')
exit_button = tk.Button(
    root,
    text='Exit',
    command=lambda: root.quit()
)
exit_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)



Jarvis_button = tk.Button(
    root,
    text='Jarvis',
    command=Main
)
Jarvis_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
    
)
root.mainloop()