import tkinter as tk
from tkinter import ttk
import psutil

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tkinter GUI Application")
        self.geometry("800x400")
        self.configure(bg='black')  # Set the background to dark color
        self.resizable(True, True)  # Make the window resizable
        self.create_widgets()

    def create_widgets(self):
        # Add a button with a less bright blue color and no border, and larger text
        button = tk.Button(self, text="Show File Systems", fg='white', bg='#0000cc', bd=0, font=('TkDefaultFont', 12), command=self.show_filesystems)
        button.pack(pady=10)

        # Create a Treeview widget with a scrollbar
        frame = tk.Frame(self)
        frame.pack(pady=10, fill=tk.BOTH, expand=True)

        style = ttk.Style()
        style.configure("Treeview", background='black', foreground='white', fieldbackground='black')
        style.configure("Treeview.Heading", background='black', foreground='white')

        self.tree = ttk.Treeview(frame, columns=("Device", "Mountpoint", "Type", "Total Size (MB)", "Used (MB)", "Free (MB)", "Percent Used"), show='headings', style="Treeview")
        self.tree.heading("Device", text="Device")
        self.tree.heading("Mountpoint", text="Mountpoint")
        self.tree.heading("Type", text="Type")
        self.tree.heading("Total Size (MB)", text="Total Size (MB)")
        self.tree.heading("Used (MB)", text="Used (MB)")
        self.tree.heading("Free (MB)", text="Free (MB)")
        self.tree.heading("Percent Used", text="Percent Used")

        scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.pack(fill=tk.BOTH, expand=True)

    def show_filesystems(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        partitions = psutil.disk_partitions()
        for partition in partitions:
            usage = psutil.disk_usage(partition.mountpoint)
            self.tree.insert("", "end", values=(
                partition.device,
                partition.mountpoint,
                partition.fstype,
                f"{usage.total / (1024 * 1024):.2f}",
                f"{usage.used / (1024 * 1024):.2f}",
                f"{usage.free / (1024 * 1024):.2f}",
                f"{usage.percent}%"
            ))

if __name__ == "__main__":
    app = App()
    app.mainloop()
