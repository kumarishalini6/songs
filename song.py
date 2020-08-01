from tkinter.filedialog import askdirectory
from tkinter import *
import os
import pygame

def Next():
    global index
    index -=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    

def Previous():
    global index
    index +=1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
   

def Stop():
    pygame.mixer.music.stop()
   
   


root=Tk()
root.geometry("440x630")

listofsongs =[]

index=0



def directorychooser():
    directory=askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            listofsongs.append(files)
        
    

    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    #pygame.mixer.music.play()

    listofsongs.reverse() 

directorychooser()


frame=Frame(root,bd=15,bg="cadet blue",relief=RIDGE).place(x=0,y=0,relwidth=1,relheight=1)
label=Label(frame,text='Music Player',bg="cadet blue",fg="cornsilk",font=("arial",20,'bold')).place(x=150,y=20)

scrollbar = Scrollbar(frame)
scrollbar.place(x=395,y=50,height=300)
listbox=Listbox(frame, yscrollcommand = scrollbar.set,bg="cornsilk" )
listbox.place(x=25,y=50,width=372,height=300)  
scrollbar.config( command = listbox.yview ) 



for items in listofsongs:
    listbox.insert(0,items)



   

nextbtn=Button(frame,text="Next song",bd=8,font=("arial",20,'bold'),bg="powder blue",command=Next).place(x=150,y=365)
previoustbtn=Button(frame,text="Previous song",bd=8,font=("arial",20,'bold'),bg="powder blue",command=Previous).place(x=120,y=439)
stopbtn=Button(frame,text="Stop song",bd=8,font=("arial",20,'bold'),bg="powder blue",command=Stop).place(x=150,y=513)





root.mainloop()
  
