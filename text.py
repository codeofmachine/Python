import tkinter as tk
import time
from tkinter import ttk

def button_func():
    enter = 'Great'
    label['text'] = enter
    text['state'] = 'disable'

#creater window
window = tk.Tk()
window.title('Window and Widgets')
window.geometry("9x5")

#create label
label = ttk.Label(window, text = 'Novelist as Vocation').pack()

#creter widget
text = tk.Text(master = window).pack()

#creater button
button = ttk.Button(master = window, text = 'How was', command = button_func).pack()

#run
window.mainloop()
