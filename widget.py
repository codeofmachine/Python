import tkinter as tk
from tkinter import ttk

def button_func():
    entry_text = entry.get()
    #upgrade thé label
    #label.configure (text = "some other text")
    label['text'] = entry_text
    entry['state'] = 'disable'
    #print(label.configure())
    
#creater window
window = tk.Tk()
window.title('Getting and settings widgets')
window.geometry('3x5')

#widgets
label = ttk.Label(master = window, text = 'Some text')
label.pack()

entry = ttk.Entry(master = window)
entry.pack()

button = ttk.Button(master = window, text = 'The button', command = button_func)
button.pack()

#run
window.mainloop()
