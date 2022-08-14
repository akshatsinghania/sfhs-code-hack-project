from tkinter import *


import time
# screen_width = self.root.winfo_screenwidth()
# screen_height = self.root.winfo_screenheight()

class MeditationComponent():
    def __init__(self,root,load_page):
        self.load_page=load_page
        self.root=root
        print("running")
        self.root.state('zoomed')
        self.choose_meditation_time_screen()

    def initiate_canvas(self):
        self.canvas = Canvas(self.root, bg='white', highlightthickness=0)
        self.canvas.pack(fill=BOTH, expand=True)


    def choose_meditation_time_screen(self):
        widgets = []
        return_button = Button(self.root,text="return",command=lambda w=widgets: self.return_home(w))
        return_button.grid(column=0,row=0)
        widgets.append(return_button)
        choose_meditation_title = Label(self.root,text="Choose your meditation time")
        widgets.append(choose_meditation_title)
        choose_meditation_title.grid(column=1,row=1)

        time_options = [
            [10, 15], 
            [20, 30]
        ]

        for row_num, row in enumerate(time_options):
            for col_num, option in enumerate(row):
                cur_button = Button(self.root, text=option, command = lambda x=option:self.start_meditation(x, widgets))
                widgets.append(cur_button)
                cur_button.grid(column=col_num+2, row=row_num+2)

        
    # def clear_root(self):
    #     frame = Frame(self.root, bg = "white")
    #     frame.grid(x = 0,  y = 0, width = WIDTH, height = HEIGHT)
    #     return frame

    def clear_root(self, widgets_to_delete):
        for widget in widgets_to_delete:
            try:
                widget.grid_forget()
                widget.forget()
            except:
                pass

       
    def start_meditation(self, duration, widgets):
        self.clear_root(widgets)
        self.meditation_screen(duration)

    def return_home(self,widgets):
        self.load_page(widgets)
        

    
    def meditation_screen(self, duration):
        self.initiate_canvas()
        
        widgets=[]

        return_button = Button(self.root,text="return",command=lambda w=widgets: self.return_home(w))
        return_button.place(x=0, y=0)
        widgets.append(return_button)
        widgets.append(self.canvas)
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        print(width, height)

        x = width//2
        y = height//2
        r = height//10

        def get_coords(x, y, r):
            x0 = x - r
            y0 = y - r
            x1 = x + r
            y1 = y + r
            return x0, y0, x1, y1

        start_time = time.time()

        self.oval = self.canvas.create_oval(*get_coords(x, y, r),fill="#ADD8E6",outline="")
        change = 200

        while time.time() - start_time < duration * 60:
            for i in range(change):
                # self.root.after(6*i, lambda : self.canvas.coords(self.oval,*get_coords(x,y,r+i)))
                self.canvas.coords(self.oval,*get_coords(x,y,r+i))
                self.root.update()
                time.sleep(0.02)

            new_r = r + change
            time.sleep(0.5)
            self.root.update()

            for i in range(change):
                # self.root.after(6*i, lambda : self.canvas.coords(self.oval,*get_coords(x,y,r+i)))
                self.canvas.coords(self.oval,*get_coords(x,y,new_r-i))
                self.root.update()
                time.sleep(0.02)

        time.sleep(3)
        
        self.canvas.pack_forget()
        self.choose_meditation_time_screen()
            

        




