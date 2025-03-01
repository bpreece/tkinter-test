import tkinter as tk

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter GUI Application")
        self.geometry("400x300")
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Hello, Tkinter!")
        label.pack(pady=20)

if __name__ == "__main__":
    app = App()
    app.mainloop()
