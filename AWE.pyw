from tkinter import Button, Tk
import keyboard
import win32gui

width = 16
height = 40
win = Tk()
xCoord = win.winfo_screenwidth() - width
yCoord = win.winfo_screenheight() - height
win.geometry(f"{width}x{height}+{xCoord}+{yCoord}")
win.overrideredirect(1)

def handleClick():
    keyboard.press_and_release("win+ctrl+left")

Button(win, text=(" ← "), width=width, height=height, command=handleClick).pack()

def setOnTop():
    if win32gui.GetWindowText(win32gui.GetForegroundWindow()) == "Amazon WorkSpaces":
        win.attributes('-topmost', True)
    win.after(100, setOnTop)

win.after(100, setOnTop)
win.mainloop()
