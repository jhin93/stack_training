import tkinter as tk

root = tk.TK()
root.geometry("300x200")
root.title("My First GUI App")

label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

root.mainloop()