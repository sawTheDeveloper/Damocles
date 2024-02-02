import tkinter as tk
from tkinter import ttk
import requests

# Model
class Model:
    def fetch_data(self):
        self.response = requests.get('https://jsonplaceholder.typicode.com/posts')
        self.data = self.response.json()
        return self.data

# View
class View:
    def __init__(self, root):
        self.root = root
        self.setup()

    def setup(self):
        self.root.geometry("300x200")
        self.root.title("Damocles Tech")
        self.root.iconbitmap('./img/SawchoticLogo2012.ico')

        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 16), background="#39FF14", foreground="white")
        style.configure("TLabel", font=("Helvetica", 20), foreground="#39FF14")

        self.label = ttk.Label(self.root, text="Damocles Tech", style="TLabel")
        self.label.pack(pady=10)

        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(pady=10)

        self.fetch_button = ttk.Button(self.root, text="Fetch Api", style="TButton")
        self.fetch_button.pack()

    def set_button_command(self, command):
        self.fetch_button.config(command=command)

    def update_listbox(self, data):
        for item in data:
            self.listbox.insert(tk.END, item['title'])

# Controller
class Controller:
    def __init__(self, root):
        self.model = Model()
        self.view = View(root)
        self.view.set_button_command(self.fetch_data)

    def fetch_data(self):
        data = self.model.fetch_data()
        self.view.update_listbox(data)

if __name__ == '__main__':
    root = tk.Tk()
    app = Controller(root)
    root.mainloop()