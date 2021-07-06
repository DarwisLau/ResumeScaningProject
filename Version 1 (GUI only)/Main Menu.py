from tkinter import*
from tkinter.font import Font
import os
from subprocess import call
import sys


#Functions to call on the other scripts
def click_add_record():
	call(["python","Add record.py"])
def click_edit_record():
	call(["python","Edit Record.py"])
def click_archive_record():
	call(["python",'Archive record.py'])
def click_search_record():
	call(["python","search record test.py"])



#Window size, title
root = Tk()
root.geometry('1920x1080')
root.maxsize(1920,1080)
root.title("Add Record")

#Define image for Background and button
bg= PhotoImage(file='D:/GUI Image/background.png')

#Background
my_canvas = Canvas(root,width=1920,height=1080)
my_canvas.pack(fill='both', expand=True)
my_canvas.configure(highlightthickness=0)
my_canvas.create_image(0,0, image=bg, anchor="nw")

#Defining our font
MenuTitleFont = Font(family="Montserrat Medium", size=40, weight="bold",slant="roman",underline=0,overstrike=0)
ProjectTitleFont = Font(family="Montserrat", size=80, weight="bold",slant="roman",underline=0,overstrike=0)
SubTitleFont = Font(family="Montserrat Medium", size=35, weight="normal",slant="roman",underline=0,overstrike=0)
ButtonFont = Font(family="Montserrat Medium", size=30, weight="normal",slant="roman",underline=0,overstrike=0)

#Creating Menu BG
Menu = Canvas(root, width=483,height=1080,bg='#B6E5DD')
Menu.place(x=0,y=0)
Menu.configure(highlightthickness=0)
Menu.create_line(0,140,483,140,fill="#707070")

#Menu Text
Menu.create_text(90,38,anchor="nw",text="Main",font=MenuTitleFont)
Menu.create_text(229,69,anchor="nw",text="Menu",font=MenuTitleFont)

#Project Title Text
my_canvas.create_text(646,401,anchor="nw",text="Resume Scanning",font=ProjectTitleFont)
my_canvas.create_text(646,499,anchor="nw",text="Project", font=ProjectTitleFont, fill="white")
my_canvas.create_text(646,625,anchor="nw",text="ALL Project", font=SubTitleFont, fill="white")
my_canvas.create_text(930,625,anchor="nw",text="by Muhd Darwis", font=SubTitleFont)
my_canvas.create_text(646,670,anchor="nw",text="& Chan Khai Shen", font=SubTitleFont)

#Create Button
buttonAdd = Button(root, text=">Add Record",command=click_add_record, bg="#B6E5DD",borderwidth=0,highlightthickness=0,bd=0, )
buttonAdd['font']=ButtonFont
Menu.create_window(90,324,anchor="nw", window=buttonAdd)

buttonEdit = Button(root, text=">Edit Record",command=click_edit_record, bg="#B6E5DD",borderwidth=0,highlightthickness=0,bd=0)
buttonEdit['font']=ButtonFont
Menu.create_window(90,456,anchor="nw", window=buttonEdit)

buttonArchive = Button(root, text=">Archive Record",command=click_archive_record, bg="#B6E5DD",borderwidth=0,highlightthickness=0,bd=0)
buttonArchive['font']=ButtonFont
Menu.create_window(90,586,anchor="nw", window=buttonArchive)

buttonSearch = Button(root, text=">Search Record",command=click_search_record, bg="#B6E5DD", borderwidth=0, highlightthickness=0,bd=0)
buttonSearch['font']=ButtonFont
Menu.create_window(90,719,anchor="nw", window=buttonSearch)


root.mainloop()