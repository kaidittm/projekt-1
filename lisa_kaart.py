from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
from tkinter import *
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

mõisted = {}
definitsioonid = []

fail = open("mõistete_fail.txt",'r', encoding = "UTF-8")
for rida in fail:
    rida = rida.strip().split("\t")
    mõisted[rida[0]] = rida[1]
fail.close()

def tagasi():
    window.destroy()
    if 'main' in sys.modules.keys():
        sys.modules.pop('main')
    import main

def edasi():
    window.destroy()
    if 'vaata_kaarte' in sys.modules.keys():
        sys.modules.pop('vaata_kaarte')
    import vaata_kaarte
    
def lisakaart():
    loeme = open("mõistete_fail.txt", "r", encoding = "UTF-8")
    for rida in loeme:
        rida = rida.strip().split("\t")
        definitsioonid.append(rida[0])
    loeme.close()
    
    mõisted[entry_3.get()] = entry_4.get()
    fail = open("mõistete_fail.txt", "a", encoding = "UTF-8")
    a = entry_3.get()+ "\t"+ entry_4.get() + "\n"
    fail.write(a)
    fail.close()
    entry_3.delete(0, END)
    entry_4.delete(0, END)
    entry_3.insert(0, "definitsioon")
    entry_4.insert(0, "seletus")

def kustuta():
    mõisted = {}
    fail = open("mõistete_fail.txt", "w")
    fail2 = open("küsida.txt", "w")
    fail.close()
    fail2.close()

window = Tk()
window.geometry("900x500")
window.configure(bg = "#FFFFFF")

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
button_image_11 = PhotoImage(file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lisakaart,
    relief="flat"
)

button_11.place(
    x=483.0,
    y=210.0,
    width=238.0,
    height=60.0
)

button_image_12 = PhotoImage(file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=edasi,
    relief="flat"
)

button_12.place(
    x=484.0,
    y=270.0,
    width=238.0,
    height=60.0
)

button_image_13 = PhotoImage(file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=kustuta,
    relief="flat"
)

button_13.place(
    x=461.0,
    y=346.0,
    width=281.0,
    height=60.0
)

button_image_14 = PhotoImage(file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=tagasi,
    relief="flat"
)
button_14.place(
    x=704.0,
    y=421.0,
    width=165.0,
    height=63.0
)

entry_image_3 = PhotoImage(file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    601.5,
    91.5,
    image=entry_image_3
)

entry_3 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_3.place(
    x=444.0,
    y=60.0,
    width=315.0,
    height=61.0
)

entry_3.insert(0, "definitsioon")

entry_image_4 = PhotoImage(file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    601.5,
    166.5,
    image=entry_image_4
)

entry_4 = Entry(
    bd=0,
    bg="#F1F1F1",
    highlightthickness=0
)
entry_4.place(
    x=444.0,
    y=135.0,
    width=315.0,
    height=61.0
)

entry_4.insert(0, "seletus")

canvas.create_rectangle(
    0.0,
    0.0,
    289.0,
    500.0,
    fill="#DEFDFD",
    outline="")

canvas.create_rectangle(
    289.0,
    0.0,
    290.0,
    500.0,
    fill="#0B0B0B",
    outline="")

window.resizable(False, False)
window.mainloop()