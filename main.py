from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import sys
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def lisa():
    window.destroy() 
    if 'lisa_kaart' in sys.modules.keys():
        sys.modules.pop('lisa_kaart')
    import lisa_kaart

def õpi():
    mõisted = {}
    fail3 = open("mõistete_fail.txt", "r", encoding = "UTF-8")
    fail4 = open("küsida.txt", "w", encoding = "UTF-8")
    start = time.time()
    start = str(start)
    fail5 = open("time.txt", "w")
    fail5.write(start)
    fail5.close()
    fail6 = open("õigete_vastuste_hulk.txt", "w")
    fail6.close()
    for rida in fail3:
        rida = rida.strip().split("\t")
        mõisted[rida[0]] = rida[1]
        kirjutada = rida[0] + '\n'
        fail4.write(kirjutada)
    fail3.close()
    fail4.close()
    window.destroy()
    if "õpi_kaart" in sys.modules.keys():
        sys.modules.pop('õpi_kaart')
    import õpi_kaart

def edetabel():
    window.destroy()
    if "edetabel" in sys.modules.keys():
        sys.modules.pop('edetabel')
    import edetabel

window = Tk()

window.geometry("900x500")
window.configure(bg = "#FFFFFF")
window.title("")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=window.destroy,
    relief="flat"
)
button_1.place(
    x=734.0,
    y=427.0,
    width=140.0,
    height=55.0
)

button_image_2 = PhotoImage(file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=edetabel,
    relief="flat"
)
button_2.place(
    x=490.0,
    y=302.0,
    width=260.0,
    height=70.0
)

button_image_3 = PhotoImage(file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lisa,
    relief="flat"
)
button_3.place(
    x=490.0,
    y=206.0,
    width=260.0,
    height=70.0
)

button_image_4 = PhotoImage(file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=õpi,
    relief="flat"
)
button_4.place(
    x=490.0,
    y=111.0,
    width=260.0,
    height=70.0
)

canvas.create_rectangle(
    373,
    0,
    373,
    515,
    fill = "black",
    outline = "")

canvas_image = PhotoImage(file=relative_to_assets("main.png"))
canvas.create_image(0,0, anchor="nw", image=canvas_image)
  
window.resizable(False, False)
window.mainloop()