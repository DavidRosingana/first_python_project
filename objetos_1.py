from tkinter import *
from tkinter import ttk


def calculo_ft_m(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass



root = Tk()
root.title("Conversor ft / m")

mainframe = ttk.Frame(root, padding="15 15 15 15")
mainframe.grid()

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)

feet_entry.grid(column=2, row=1)

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2)
ttk.Button(mainframe, text="Calcular", command=calculo_ft_m()).grid(column=3, row=3)

ttk.Label(mainframe, text="Pies").grid(column=3, row=1)
ttk.Label(mainframe, text="Equivale a").grid(column=1, row=2)
ttk.Label(mainframe, text="Metros").grid(column=3, row=2)

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculo_ft_m)

root.mainloop()
