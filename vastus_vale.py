from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage, font
import sys
from tkinter import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def pane_kinni():
    window.destroy()
    if 'õpi_kaart' in sys.modules.keys():
        sys.modules.pop('õpi_kaart')
    import õpi_kaart

def järgmine():
    window.destroy()
    if 'õpi_kaart' in sys.modules.keys():
        sys.modules.pop('õpi_kaart')
    import õpi_kaart

def näita_vastust():
    f1 = open("mõistete_fail.txt", "r", encoding="UTF-8")
    f2 = open("vastus_vale.txt", "r", encoding = "UTF-8")
    küsitud_mõiste = f2.readline().strip()
    f2.close()
    f3 = open("vastus_vale.txt", "w")
    f3.close()
    for rida in f1:
        rida = rida.strip().split("\t")
        definitsioon = rida[0]
        mõiste = rida[1]
        if definitsioon == küsitud_mõiste:
            näita = mõiste
            break

    f1.close()
    
    button_19.destroy()
    button_20.destroy()
    
    kaugus = 225
    kõrgus = 110
    ridade_arv = 0
    
    if len(mõiste) > 30:
        ridu = len(mõiste) // 30 + 1
        for i in range(ridu):
            if (i*30)+29 < len(näita):
                if näita[i*30] != " " and näita[(i*30)+29] != " ":
                    canvas.create_text(
                    kaugus,
                    kõrgus,
                    anchor="center",
                    text=näita[i*30:(i*30)+30]+"-",
                    font=font1,
                    fill="#000000")
            
                else:
                    canvas.create_text(
                    kaugus,
                    kõrgus,
                    anchor="center",
                    text=näita[i*30:(i*30)+30],
                    font=font1,
                    fill="#000000")
                    
            else:
                canvas.create_text(
                kaugus,
                kõrgus,
                anchor="center",
                text=näita[i*30:(i*30)+30],
                font=font1,
                fill="#000000")
                    
            ridade_arv += 1
    
            kõrgus += 40     
    else:
        ridade_arv += 1
        canvas.create_text(
        kaugus,
        kõrgus,
        anchor="center",
        text=näita,
        font=font1,
        fill="#000000")    
         
    if ridade_arv > 2:
        juurde = ridade_arv - 2
        uus = 250
        for i in range(juurde):
            uus += 37

    else:
        uus = 250

    if uus > 1000:
      uus = 1000

    uus_str = str(uus)
    suurus = "450x" + uus_str
    canvas["height"] = uus
    window.geometry(suurus)
    
    button_21.place(
        x=113.0,
        y=uus-80,
        width=223.0,
        height=60.0
    )

window = Tk()

window.geometry("450x250")
window.configure(bg = "#FFFFFF")
window.title("")

font1 = font.Font(family="Baskerville Old Face", size=14)

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 250,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas_image = PhotoImage(file=relative_to_assets("vale.png"))
canvas.create_image(0,0, anchor="nw", image=canvas_image)

canvas.place(x = 0, y = 0)
button_image_19 = PhotoImage(file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=pane_kinni,
    relief="flat"
)
button_19.place(
    x=12.0,
    y=166.0,
    width=186.0,
    height=60.0
)

button_image_20 = PhotoImage(file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=näita_vastust,
    relief="flat"
)
button_20.place(
    x=210.0,
    y=166.0,
    width=223.0,
    height=60.0
)

button_image_21 = PhotoImage(file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=järgmine,
    relief="flat"
)

window.resizable(False, False)
window.mainloop()
