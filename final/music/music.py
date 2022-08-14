from tkinter import *
import tkinter as tk
from tkinter import ttk, filedialog
from pygame import mixer
import os


def music_player():
    root=Tk()
    root.title("Music Player")
    root.geometry("920x500")
    root.configure(bg="#151618")
    root.resizable(False, False)

    mixer.init()

    def openfolder():
        path=filedialog.askdirectory()
        if path:
            os.chdir(path)
            songs=os.listdir(path)
            for song in songs:
                if song.endswith(".mp3"):
                    playlist.insert(END,song)

    def playsong():
        music_name=playlist.get(ACTIVE)
        mixer.music.load(playlist.get(ACTIVE))
        mixer.music.play()







    #buttons
    play=PhotoImage(master=root,file="./final/music/imgs/playb.png")
    Button(root,image=play,bd=0,bg='#151618',command=playsong).place(x=200,y=0)

    pause=PhotoImage(master=root,file="./final/music/imgs/pauseb.png")
    Button(root,image=pause,bd=0,bg='#151618',command=mixer.music.pause).place(x=200,y=100)

    unpause=PhotoImage(master=root,file="./final/music/imgs/resume.png")
    Button(root,image=unpause,bd=0,bg='#151618',command=mixer.music.unpause).place(x=200,y=200)

    replay=PhotoImage(master=root,file="./final/music/imgs/replay.png")
    Button(root,image=replay,bd=0,bg='#151618',command=mixer.music.rewind).place(x=200,y=300)

    Label(root,bg='#151618').pack(side=RIGHT)


    selectfolder=PhotoImage(master=root,file="./final/music/imgs/musicfolder.png")
    music_frame = Frame(root,bd=0,relief=RIDGE,bg='black')
    music_frame.place(x=330,y=50,width=560,height=400)

    Button(root,image=selectfolder,bg="#000000",command=openfolder).place(x=330,y=10)

    scroll=Scrollbar(music_frame)
    playlist=Listbox(music_frame,width=100,font=("arial",10),bg='#151618',fg="grey",selectbackground="lightblue", cursor="hand2",bd=0,yscrollcommand=scroll.set)
    scroll.config(command=playlist.yview)
    scroll.pack(side=RIGHT, fill=Y)
    playlist.pack(side=LEFT,fill=BOTH)


    root.mainloop()

