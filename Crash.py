from tkinter import messagebox

def crash():
    messagebox.showwarning('CRASHER','Try to close me... :)')
    crash()

crash()