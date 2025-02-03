import tkinter as tk
from tkinter import ttk

window = tk.Tk()
window.title('Combo and Spin')

items = ('IceCream', 'Pizza', 'Broccoli')
#change1 = tk.StringVar(items)
combo = ttk.Combobox(window)
combo['values'] = items
#combo.configure(value = items)
change = ttk.Label(window, text='a label')
#combo.bind(<ComboboxSelected>, event = change ['change1'])
combo.pack()
change.pack()
spin_int = tk.IntVar(value = 12)
spin = ttk.Spinbox(window, from_ = 1, to = 20, increment = 1)
#spin['value'] = (1,2,3,4,5)
spin.pack()
window.mainloop()