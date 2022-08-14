from tkinter import Button, Entry, Label, X,  TOP, Frame, LEFT, StringVar, Tk
import tkinter.font as tkFont
from home import Home


import utility

def login_or_not(username, password):
    return utility.checkIfCorrect(username, password)

def clear_root(widgets_to_delete):
    for widget in widgets_to_delete:
        widget.grid_forget()
        widget.forget()

#Login Logic
def check(widgets,root):
    global loginMessage

    try:loginMessage.grid_forget()
    except Exception:pass

    if login_or_not(username.get(), password.get()):
        loginMessage = Label(frame, text = "you are now logged in", font = messageHeight)
        # Change screen to homepage
        clear_root(widgets)
        home = Home(root)

        
    else:
        loginMessage = Label(frame, text = "incorrect username or password", font = messageHeight)

    loginMessage.grid(row = 2, column = 1)

def main(root, WIDTH, HEIGHT, wu, hu):
    #Initialization
    global frame, username, password, packs
    global messageHeight
    widgets=[]
    messageHeight = tkFont.Font(size = -int(HEIGHT/20))
    
    root.title("Log In")
    packs = []

    #Setting Heading and Frame
    heading=utility.headingDesign("Log In", packs, root, HEIGHT)
    widgets.append(heading)
    frame = utility.formFrameDesign(root, packs, WIDTH)
    widgets.append(frame)

    #Labels
    username_label=utility.entranceLabelDesign(frame, "username: ", 0, 0, HEIGHT)
    password_label=utility.entranceLabelDesign(frame, "password: ", 1, 0, HEIGHT)
    widgets.append(username_label)
    widgets.append(password_label)

    #Inputs
    username,username_entry = utility.entranceDesign(frame, 0, 1, HEIGHT)
    password,password_entry = utility.entranceDesign(frame, 1, 1, HEIGHT)
    
    widgets.append(username_entry)
    widgets.append(password_entry)
    

    submitButton = Button(frame, text = "Log In", command = lambda w=widgets,r=root: check(w,r), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    submitButton.grid(row = 2, column = 0)
    widgets.append(submitButton)
    

    goBack = Button(frame, text = "go back", command = lambda : utility.back(packs, root), font = tkFont.Font(size = -int(HEIGHT/14)), borderwidth = 10)
    goBack.grid(row = 3, column = 0)
    widgets.append(goBack)
    
    root.mainloop()

if __name__ == "__main__":
    root = utility.basicStructure(612, 378, 1, "Log In")
    main(root, 612, 378, 612/1000, 378/1000)

