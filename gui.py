import tkinter as tk

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")


label = tk.Label(root,text="Testing", font=('ComicSans', 18))
label.pack(padx=20, pady=20)

button = tk.Button(root, height=3,)

button.grid

root.mainloop()