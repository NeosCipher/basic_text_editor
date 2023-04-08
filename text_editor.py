#! /usr/bin/python

import tkinter as tk
from tkinter import ttk
from custom_dialog import CustomFileDialog
from tkinter import filedialog

class TextEditor:
    def __init__(self, master_window):
        self.master_window = master_window
        self.master_window.title("Text Editor")
        self.file_path = None 
        self.generate_widgets()

    def load_file(self):
        custom_dialog = CustomFileDialog(self.master_window)
        file_path = custom_dialog.show()
        # Handling of the file and the input
        if file_path:
            with open(file_path, 'r') as file:
                self.text.delete(1.0, tk.END)
                self.text.insert(tk.END, file.read())
                self.file_path = file_path

    def save_file(self):
        # Handling of the file and the input
        if self.file_path:
            with open(self.file_path, 'w') as file:
                file.write(self.text.get(1.0, tk.END))
        else:
            self.save_file_as()

    def save_file_as(self):
        # Handling of the file and the input
        custom_dialog = CustomFileDialog(self.master_window)
        file_path = custom_dialog.show()
        if file_path:
            with open(file_path, 'w') as file:
                file.write(self.text.get(1.0, tk.END))
                self.file_path = file_path

    def call_config(self):
        # TODO: Set the function to call the config window
        return None

    def in_progress(self):
        # TODO: To do after completin the design of the interface
        return None

    def generate_widgets(self):
        # Generating the menu and each of its windows
        menubar = tk.Menu(self.master_window)

        # File submenu
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Open", command=self.load_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As...", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.master_window.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        self.master_window.config(menu=menubar)
    
        # Settings submenu
        settings = tk.Menu(self.master_window)
        settings = tk.Menu(menubar, tearoff=0)
        settings.add_command(label="Configuration", command=self.call_config)
        settings.add_command(label="In Progress", command=self.in_progress)
        menubar.add_cascade(label="Settings", menu=settings)
        self.master_window.config(menu=menubar)

        # Generatig the area for writing
        self.text = tk.Text(self.master_window)
        self.text.pack(fill=tk.BOTH, side=tk.LEFT, expand=1)
        
        # Generating the scrollbar widget
        self.scrollbar = tk.Scrollbar(self.master_window)
        self.scrollbar.pack(fill=tk.Y, side=tk.TOP, expand=1)
        self.text.configure(yscrollcommand=self.scrollbar.set)

    def run_window(self):
        self.master_window.mainloop()
