import tkinter as tk

def say_hello():
    label.config(text="Hello! This is my first Python EXE.")

root = tk.Tk()
root.title("My First EXE")
root.geometry("350x180")

label = tk.Label(root, text="Click the button", font=("Arial", 14))
label.pack(pady=30)

button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()

root.mainloop()
