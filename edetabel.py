from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, font
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("900x500")
window.configure(bg = "#FFFFFF")
window.title("")

font1 = font.Font(family="Baskerville Old Face", size=14)

def tagasi():
    window.destroy()
    if 'main' in sys.modules.keys():
        sys.modules.pop('main')
    import main

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 500,
    width = 900,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_image = PhotoImage(file=relative_to_assets("edetabel.png"))
canvas.create_image(0,0, anchor="nw", image=canvas_image)

canvas.place(x = 0, y = 0)
button_image_5 = PhotoImage(file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=tagasi,
    relief="flat"
)

button_5.place(
    x=630.0,
    y=409.0,
    width=195.0,
    height=67.0
)

fail = open("edetabel.txt", "r", encoding = "UTF-8")
ajad = {}

for rida in fail:
    rida = rida.strip().split("\t")
    aeg = float(rida[1])
    nimi = rida[0]
    protsent = rida[2]
    ajad[aeg] = [nimi, protsent]

fail.close()

tulemused = list(ajad.keys())
tulemused.sort()

kaugus = 40
kõrgus = 60
for i in range(10):
    try:
        aeg = tulemused[i]
        nimi = ajad[aeg][0]
        protsent = ajad[aeg][1]
        aeg = round(aeg,1)
        if aeg > 60:
            ajakulu = str(int(aeg/60)) + " min " + str(round(aeg % 60)) + " s"

        else:
            ajakulu = str(round(aeg,2)) + " s" 
    
        if i+1 < 10:
            tekst = "  " + str(i+1) + ".  " + nimi

        else:
            tekst = str(i+1) + ".  " + nimi

        canvas.create_text(
        kaugus,
        kõrgus,
        anchor="nw",
        text=tekst,
        fill="#000000",
        font=font1)

        canvas.create_text(
        kaugus + 390,
        kõrgus,
        anchor="nw",
        text=ajakulu,
        fill="#000000",
        font=font1)

        canvas.create_text(
        kaugus + 670,
        kõrgus,
        anchor="nw",
        text=protsent,
        fill="#000000",
        font=font1)

        kõrgus += 35

    except:
        break

window.resizable(False, False)
window.mainloop()