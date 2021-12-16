from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, font, scrolledtext
from tkinter import *
import sys
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("900x500")
window.configure(bg = "#FFFFFF")
window.title("")

font1 = font.Font(family="Baskerville Old Face", size=14)

mõisted = {}

fail3 = open("mõistete_fail.txt", "r", encoding = "UTF-8")
fail4 = open("küsida.txt", "w", encoding = "UTF-8")
for rida in fail3:
    rida = rida.strip().split("\t")
    mõisted[rida[0]] = rida[1]
    kirjutada = rida[0] + '\n'
    fail4.write(kirjutada)
fail3.close()
fail4.close()

def tagasi():
    window.destroy()
    if 'lisa_kaart' in sys.modules.keys():
        sys.modules.pop('lisa_kaart')
    import lisa_kaart
    
def edasi():
    window.destroy()
    start = time.time()
    start = str(start)
    f1 = open("time.txt", "w")
    f1.write(start)
    f1.close()
    f2 = open("õigete_vastuste_hulk.txt", "w")
    f2.close()
    if "õpi_kaart" in sys.modules.keys():
        sys.modules.pop('õpi_kaart')
    import õpi_kaart


def kustuta():
    mõisted = {}
    fail = open("mõistete_fail.txt", "w")
    fail2 = open("küsida.txt", "w")
    fail.close()
    fail2.close()

    window.destroy()
    if "lisa_kaart" in sys.modules.keys():
        sys.modules.pop('lisa_kaart')
    import lisa_kaart

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 800,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

class ScrollBar:
    def __init__(self):
        h = Scrollbar(window, orient = 'horizontal')
        h.pack(side = BOTTOM, fill = X)
        v = Scrollbar(window)
        v.pack(side = RIGHT, fill = Y)
        
        t = Text(window, width = 58, height = 10, font=font1, wrap = NONE,
                xscrollcommand = h.set,
                yscrollcommand = v.set)

        for i in mõisted.keys():
            lisa = mõisted[i]+"\n"
            if len(i) > 25:
                i = i[:22] + "..."
            
            i = i + "\t" + "\t" + "\t"
                
            t.insert(END,i)
            
            t.insert(END,lisa)

        t.place(x=30, y=70)

        h.config(command=t.xview)
        v.config(command=t.yview)
                

s = ScrollBar()
        
      
canvas_image = PhotoImage(file=relative_to_assets("vaata_äär.png"))
canvas.create_image(0,0, anchor="nw", image=canvas_image)


button_image_15 = PhotoImage(file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=edasi,
    relief="flat"
)

button_image_16 = PhotoImage(file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=tagasi,
    relief="flat"
)

button_image_17 = PhotoImage(file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=kustuta,
    relief="flat"
)

button_15.place(x=340, y=400)
button_16.place(x=600, y=400)
button_17.place(x=40, y=400)



window.resizable(False, False)
window.mainloop()
