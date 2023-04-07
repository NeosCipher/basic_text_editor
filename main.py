#! usr/bin/python

import tkinter as tk
from text_editor import TextEditor

def main():
    main_window = tk.Tk()
    app = TextEditor(main_window)
    app.run_window()
    
if __name__ == '__main__':
    main()
