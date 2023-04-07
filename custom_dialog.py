import tkinter as tk
from tkinter import filedialog

class CustomFileDialog:
        def __init__(self, parent, file_types=(("Text files", "*.txt"), ("All files", "*.*"))):
            self.parent = parent
            self.file_path = None
            self.file_types = file_types

        def show(self):
            file_path = filedialog.askopenfilename(parent=self.parent, filetypes=self.file_types)
            if file_path:
               self.file_path = file_path
               return self.file_path

        
