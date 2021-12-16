from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
from tkinter import *
import sys

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()

window.geometry("450x250")
window.configure(bg = "#FFFFFF")
window.title("")

def tagasi():
    window.destroy()
    if 'õpi_kaart' in sys.modules.keys():
        sys.modules.pop('õpi_kaart')
    import õpi_kaart      

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 250,
    width = 450,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")

canvas_image = PhotoImage(file=relative_to_assets("õige.png"))
canvas.create_image(0,0, anchor="nw", image=canvas_image)

canvas.place(x = 0, y = 0)
button_image_18 = PhotoImage(file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=tagasi,
    relief="flat"
)
button_18.place(
    x=142.0,
    y=166.0,
    width=165.0,
    height=60.0
)
window.resizable(False, False)
window.mainloop()