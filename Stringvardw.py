import tkinter as tk
from tkinter import ttk
window = tk.Tk()
window.title('StringVar')
exercise_var = tk.StringVar(value = 'test')
entry1 = ttk.Entry(master = window, textvariable = exercise_var)
entry1.pack()
entry2 = ttk.Entry(master = window, textvariable = exercise_var)
entry2.pack()
label = ttk.Label(master = window, textvariable = exercise_var)
label.pack()
window.mainloop()