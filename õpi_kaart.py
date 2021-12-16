from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, font
from random import choice
import sys
import time

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def tagasi():
    window.destroy()
    if 'main' in sys.modules.keys():
        sys.modules.pop('main')
    import main

def vahele():
    window.destroy()
    if 'õpi_kaart' in sys.modules.keys():
        sys.modules.pop('õpi_kaart')
    import õpi_kaart   

def kontrolli():
    if mõisted[mõiste].lower() == entry_1.get().lower():
        f7 = open("õigete_vastuste_hulk.txt", "a", encoding = "UTF-8")
        f7.write(mõiste)
        f7.write('\n')
        f7.close()
        window.destroy()
        if 'vastus_õige' in sys.modules.keys():
            sys.modules.pop('vastus_õige')
        import vastus_õige
  
    else:
        fail5 = open("vastus_vale.txt", "w", encoding = "UTF-8")
        fail5.write(mõiste)
        fail5.close()
        window.destroy()
        if "vastus_vale" in sys.modules.keys():
            sys.modules.pop('vastus_vale')
        import vastus_vale

def lisa_edetabelisse():
    global aeg, entry_2
    f1 = open("edetabel.txt", "a", encoding = "UTF-8")
    f2 = open("mõistete_fail.txt", "r", encoding = "UTF-8")
    n1 = 0
    for i in f2:
        if i != "":
            n1 += 1
    f2.close()

    f3 = open("õigete_vastuste_hulk.txt", "r", encoding = "UTF-8")
    n2 = 0
    for j in f3:
        if j != "":
            n2 += 1
    f3.close()
    
    nimi = entry_2.get()
    f1.write(nimi)
    f1.write("\t")
    aeg = str(aeg)
    f1.write(aeg)
    f1.write("\t")
    protsent = str(round(n2/n1*100)) + "%"
    f1.write(protsent)
    f1.write("\n")
    f1.close()

    window.destroy()
    if 'main' in sys.modules.keys():
        sys.modules.pop('main')
    import main

mõisted = {}
küsida_list = []
fail3 = open("küsida.txt", "r", encoding = "UTF-8")
for rida in fail3:
    rida = rida.strip()
    küsida_list.append(rida)
fail3.close()

fail2 = open("mõistete_fail.txt", "r", encoding = "UTF-8")
for rida in fail2:
    rida = rida.strip().split('\t')
    mõisted[rida[0]] = rida[1]
fail2.close()

fail6 = open("vastus_vale.txt", encoding = "UTF-8")
rida = fail6.readline()
fail6.close()
fail7 = open("vastus_vale.txt", "w")
fail7.close()

if rida != "":
    mõiste = rida.strip()
  
else:
    try:
        mõiste = choice(küsida_list)

    except:
        mõiste = False

fail4 = open("küsida.txt", "w", encoding = "UTF-8")
if mõiste != False and mõiste in küsida_list:
    küsida_list.remove(mõiste)
for i in küsida_list:
    kirjuta = i + "\n"
    fail4.write(kirjuta)
fail4.close()

window = Tk()

window.geometry("900x500")
window.configure(bg = "#FFFFFF")
font1 = font.Font(family="Baskerville Old Face", size=14)
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

canvas_image = PhotoImage(file=relative_to_assets("äär.png"))
canvas.create_image(0,0, anchor="nw", image=canvas_image)

canvas.place(x = 0, y = 0)

if mõiste != False:
    if len(mõiste) < 25:
        canvas.create_text(
          402,
          140,
          anchor="nw",
          text=mõiste,
          fill="#000000",
          font=font1)

    else:
        ridu = int(len(mõiste)/25)
        kõrgus = 160-ridu*20 
        for i in range(ridu):
            canvas.create_text(
              402,
              kõrgus,
              anchor="nw",
              text=mõiste[i*25:(i*25)+25],
              fill="#000000",
              font=font1)
            kõrgus += 20


    button_image_6 = PhotoImage(file=relative_to_assets("button_6.png"))
    button_6 = Button(
      image=button_image_6,
      borderwidth=0,
      highlightthickness=0,
      command=tagasi,
      relief="flat")
    
    button_6.place(
      x=721.0,
      y=429.0,
      width=167.0,
      height=58.0)

    button_image_7 = PhotoImage(file=relative_to_assets("button_7.png"))
    button_7 = Button(
      image=button_image_7,
      borderwidth=0,
      highlightthickness=0,
      command=kontrolli,
      relief="flat")
    
    button_7.place(
      x=541.0,
      y=262.0,
      width=219.0,
      height=60.0)

    button_image_8 = PhotoImage(file=relative_to_assets("button_8.png"))
    button_8 = Button(
      image=button_image_8,
      borderwidth=0,
      highlightthickness=0,
      command=vahele,
      relief="flat")
    
    button_8.place(
      x=541.0,
      y=330.0,
      width=219.0,
      height=63.0)

    entry_1 = Entry(
      bd=0,
      bg="#F2F2F2",
      highlightthickness=0)
    
    entry_1.place(
      x=412.0,
      y=186.0,
      width=331.0,
      height=62.0)

    entry_image_1 = PhotoImage(file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
      577.5,
      218.0,
      image=entry_image_1)

else:
    #aeg
    end = time.time()
    end = float(end)
    f1 = open("time.txt", "r")
    for i in f1:
        start = i.strip()
        start = float(start)
    f1.close()
    aeg = end - start

    if aeg > 60 and aeg < 120:
        labeli_tekst = str(int(aeg/60)) + " minut ja " + str(round(aeg % 60)) + " sekundit."

    elif aeg > 120:
        labeli_tekst = str(int(aeg/60)) + " minutit ja " + str(round(aeg % 60, 0)) + " sekundit."

    else:
        labeli_tekst = str(round(aeg, 2)) + " sekundit."

    canvas_image_1 = PhotoImage(file=relative_to_assets("vastatud.png"))
    canvas.create_image(390,80, anchor="nw", image=canvas_image_1)

    canvas_image_2 = PhotoImage(file=relative_to_assets("sisesta.png"))
    canvas.create_image(420,190, anchor="nw", image=canvas_image_2)

    canvas_image_3 = PhotoImage(file=relative_to_assets("äär.png"))
    canvas.create_image(0,0, anchor="nw", image=canvas_image_3)

    canvas.place(x = 0, y = 0)
    button_image_9 = PhotoImage(file=relative_to_assets("button_9.png"))
    button_9 = Button(
      image=button_image_9,
      borderwidth=0,
      highlightthickness=0,
      command=lisa_edetabelisse,
      relief="flat")
    button_9.place(
      x=450.0,
      y=298.0,
      width=281.0,
      height=60.0)

    canvas.create_text(
      590,
      140,
      anchor="center",
      text=labeli_tekst,
      fill="#000000",
      font=font1)

    button_image_10 = PhotoImage(file=relative_to_assets("button_10.png"))
    button_10 = Button(
      image=button_image_10,
      borderwidth=0,
      highlightthickness=0,
      command=tagasi,
      relief="flat")
    button_10.place(
      x=686.0,
      y=397.0,
      width=165.0,
      height=63.0)

    entry_image_2 = PhotoImage(file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
      587.5,
      258.5,
      image=entry_image_2)
    entry_2 = Entry(
      bd=0,
      bg="#F1F1F1",
      highlightthickness=0)
    entry_2.place(
      x=430.0,
      y=227.0,
      width=315.0,
      height=61.0)
 
window.resizable(False, False)
window.mainloop()