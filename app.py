#! /usr/bin/python

import tkinter as tk
import psutil

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter GUI Application")
        self.geometry("600x400")
        self.configure(bg='black')  # Set the background to dark color
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, text="Hello, Tkinter!", fg='white', bg='black')
        label.pack(pady=20)

        # Add a button with blue as the thematic color
        button = tk.Button(self, text="Show File Systems", fg='white', bg='blue', command=self.show_filesystems)
        button.pack(pady=10)

        self.text_area = tk.Text(self, fg='white', bg='black')
        self.text_area.pack(pady=10, fill=tk.BOTH, expand=True)

    def show_filesystems(self):
        partitions = psutil.disk_partitions()
        self.text_area.delete(1.0, tk.END)  # Clear the text area
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            self.text_area.insert(tk.END, f"Device: {partition.device}\n")
            self.text_area.insert(tk.END, f"Mountpoint: {partition.mountpoint}\n")
            self.text_area.insert(tk.END, f"File system type: {partition.fstype}\n")
            self.text_area.insert(tk.END, f"Total Size: {usage.total / (1024 * 1024):.2f} MB\n")
            self.text_area.insert(tk.END, f"Used: {usage.used / (1024 * 1024):.2f} MB\n")
            self.text_area.insert(tk.END, f"Free: {usage.free / (1024 * 1024):.2f} MB\n")
            self.text_area.insert(tk.END, f"Percentage Used: {usage.percent}%\n")
            self.text_area.insert(tk.END, "-"*40 + "\n")

if __name__ == "__main__":
    app = App()
    app.mainloop()
