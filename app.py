#! /usr/bin/python

import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter GUI Application")
        self.geometry("400x300")
        self.configure(bg='black')  # Set the background to dark color
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Hello, Tkinter!", fg='white', bg='black')
        label.pack(pady=20)

        # Add a button with blue as the thematic color
        button = tk.Button(self, text="Click Me", fg='white', bg='blue')
        button.pack(pady=10)

if __name__ == "__main__":
    app = App()
    app.mainloop()
