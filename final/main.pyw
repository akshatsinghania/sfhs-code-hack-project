#imports
from tkinter import Tk, Frame, Button, SUNKEN, Y
import loginGui, signUpGui
import tkinter.font as tkFont

#Switching File, given the fileName
def switchFile(file):
    def main():
        deleteMe = clearRoot()
        try:
            file.main(root, WIDTH, HEIGHT, wu, hu)
            deleteMe.place_forget()
            final(root)
        except Exception:pass
    return main

def final(root):

    global WIDTH, HEIGHT, wu, hu

    WIDTH = root.winfo_screenwidth()
    HEIGHT = root.winfo_screenheight()

    wu = WIDTH/1000
    hu = HEIGHT/1000

    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.maxsize(WIDTH, HEIGHT); root.minsize(WIDTH, HEIGHT)
    root.title("Account Setup")
    root.config(bg = "cyan")

    with open("data.txt", "a"):
        pass

    buttonWidth, buttonHeight = wu*450, hu*550
    marginX, marginY = 30*wu, 50*hu

    containerSize = 350*hu

    startX = marginX
    endX = WIDTH - marginX - buttonWidth
    startY = marginY
    
    makeButton(root, "Log In", switchFile(loginGui), buttonWidth, buttonHeight, startX, startY)
    makeButton(root, "Sign up", switchFile(signUpGui), buttonWidth, buttonHeight, endX, startY)

    root.mainloop()

#Button Design
def makeButton(root, Text, Function, width, height, xPos, yPos):
    font = tkFont.Font(size = -int(height/3))
    button = Button(root, text = Text, bg="black", fg = "yellow",
            font = font, borderwidth = 15, relief = SUNKEN, command = Function)
    button.place(x = xPos, y = yPos, width = width, height = height)

def clearRoot():
    frame = Frame(root, bg = "white")
    frame.place(x = 0,  y = 0, width = WIDTH, height = HEIGHT)
    return frame

    
#Execution
if __name__ == "__main__":
    root = Tk()
    root.state('zoomed')
    final(root)
