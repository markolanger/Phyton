import subprocess

wortlaenge = "0:25"
Hoch = 75*4   #höhe in cm
Breit = 75*7  #breite in cm
fontcolor = "#F0FFFF"
StartupVolume = "mpc volume 53"
outpt = subprocess.check_output(StartupVolume, shell=True)
#volume = subprocess.check_output('mpc volume', shell=True)
titel = subprocess.check_output('mpc current', shell=True)


def callback1():
    print("volumeM")
    volumeM()
    Slider.set(volume[8:10])
    print(volume[8:10])

def callback2():
    print("volumeP")
    volumeP()
    Slider.set(volume[8:10])
    print(volume[8:10])

def volumeM():
    subprocess.check_output('mpc volume -5' , shell = True)
def volumeP():
    subprocess.check_output('mpc volume +5' , shell = True)


from tkinter import *
root = Tk()
root.wm_title("GUI")
root.config(background = "#FFFFFF")
topFrame = Frame(root, width = Breit, height = Hoch, background = "#FFFFFF") # Frame initialisieren
topFrame.grid(row=0, column=0, padx=0, pady=0)
middleFrame = Frame(root, width = Breit, height = Hoch, background = "#FFFFFF") # Frame initialisieren
middleFrame.grid(row=1, column=0, padx=0, pady=0) # Relative Position und Seitenabstand (padding) angeben
topLabel1 = Label(topFrame, text=titel[0:81], bg="#FFFFFF")
topLabel1.grid(row=0, column=0, padx=0, pady=0)
topLabel2 = Label(topFrame, text="...", bg="#FFFFFF")
topLabel2.grid(row=0, column=1, padx=0, pady=0)
topLabel3 = Label(topFrame, text=volume, bg="#FFFFFF")
topLabel3.grid(row=2, column=0, padx=0, pady=0)
buttonFrame = Frame(root, width=Breit, height = Hoch/2, bg = "#FFFFFF")
buttonFrame.grid(row=2, column=0, padx=3, pady=3)
B1 = Button(buttonFrame, text="Button1", width=5, command=callback1)
B1.grid(row=0, column=0, padx=10, pady=0)
B2 = Button(buttonFrame, text="Button2", width=5, command=callback2)
B2.grid(row=0, column=1, padx=10, pady=0)
Slider = Scale(buttonFrame, from_=0, to=100, resolution=0.1, orient=HORIZONTAL, length=300)
Slider.grid(row=0, column=2, padx=0, pady=0)
Slider.set(volume[8:10])
print(volume[8:10])

mainloop()
volume = subprocess.check_output('mpc volume', shell=True)