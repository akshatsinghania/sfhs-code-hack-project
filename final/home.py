from tkinter import *
from meditation import main
from games import game
from music import music
# Create a Label Widget to display the text or Image


class Home():
    def __init__(self,root):
        
        self.root=root
        self.screen()
    
    def screen(self):
        widgets=[]
        self.root.state('zoomed')
        options = [
            ["meditation"],
            ["music"],
            ['games']
        ]
        self.title=Label(self.root, text = "JustRelax", bg="black", fg = "yellow", padx = "50", pady = "30",font=('Arial',50))
        self.title.pack(fill = X, side = TOP, pady = 5)
        widgets.append(self.title)
        for i in range(len(options)):
            for j in range(len(options[i])) :
                frame = Frame(self.root)
                option_button = Button(frame, text = options[i][j],height=5,width=20,command=lambda o=options[i][j],w=widgets:self.load_page(o,w)).pack()
                frame.pack()
                widgets.append(frame)
                widgets.append(option_button)

    def clear_page(self,widgets):
        for widget in widgets:
            try:
                widget.forget()
                widget.grid_forget()
            except:
                pass

            
    def load_page(self,page,widgets):
        pages = {
            "meditation":{"function":main.MeditationComponent,"clear_root":True},
            "games":{"function":game.main,"clear_root":False},
            "music":{"function":music.music_player,"clear_root":False},
            "home":{"function":Home,"clear_root":False}
        }
        def load_home(widgets):
            print("w",widgets)
            self.clear_page(widgets)
            self.screen()
        App = pages[page]['function']
        if(pages[page]['clear_root']):
            self.clear_page(widgets)
            app = App(self.root,load_home)
        else:
            app = App()
        
        



    
    

