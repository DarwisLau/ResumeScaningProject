from tkinter import*
from tkinter import ttk
from tkinter.font import Font
import mysql.connector
from tkinter.ttk import Treeview
from tkinter.ttk import Scrollbar

#Window size, title
root = Tk()
root.geometry('1920x1080')
root.maxsize(1920,1080)
root.title("Search record")

#Define image for Background and button
bg= PhotoImage(file='D:/GUI Image/background.png')
SearchButtonImg = PhotoImage(file='D:/GUI Image/search button.png')

#Background
my_canvas = Canvas(root,width=1920,height=1080)
my_canvas.pack(fill='both', expand=True)
my_canvas.configure(highlightthickness=0)
my_canvas.create_image(0,0, image=bg, anchor="nw")


#Defining our font
Header1Font = Font(family="Montserrat", size=30, weight="normal",slant="roman",underline=0,overstrike=0)
Header2Font = Font(family="Montserrat Medium", size=30, weight="normal",slant="roman",underline=0,overstrike=0)
Header3Font = Font(family="Montserrat Medium", size=15, weight="normal",slant="roman",underline=0,overstrike=0)

#Creating Header
Header = Canvas(root, width=1920,height=158,bg='#BAE2DC')
Header.place(x=0,y=0)
Header.configure(highlightbackground='#707070')

#header text
Header.create_text(140,42,anchor="nw", text="Resume Scanning Project", font=Header1Font)
Header.create_text(1549,42,anchor="nw", text="Search Records", font=Header2Font)
Header.create_text(140,85,anchor="nw", text="ALL Project by Muhammad Darwis and Chan Khai Shen", font=Header3Font)

#Create A Main Frame
main_frame = Frame(root)
main_frame.place(anchor="nw",height=600,width=1610,x=160,y=318)

#Create canvas 
scrollcanvas = Canvas(main_frame)
scrollcanvas.pack(side=LEFT, fill=BOTH, expand=1)

#create treeview
my_tree = ttk.Treeview(root)
my_canvas.create_window(160,318,height=600,anchor="nw",window=my_tree)

#Add a scrollbar to the canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_tree.yview)
my_scrollbar.pack(side=RIGHT, fill=Y)

#Configuring scrollbar to treeview
my_tree.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_tree.yview)


#define our columns
my_tree['columns'] = ("Name", "Email", "IC No.", "Phone Number", "Position Applied", "Language (Written)","Language (Spoken)","Programming Language","Past Work Experience","Duration","Highest Education", "Soft Skills")

#Format our columns
my_tree.column("#0", width=0, minwidth=0,stretch=NO)
my_tree.column("Name", anchor=W, width=200, minwidth=200,stretch=NO)
my_tree.column("Email", anchor=W, width=160,minwidth=160,stretch=NO)
my_tree.column("IC No.", anchor=CENTER, width=80,minwidth=80,stretch=NO)
my_tree.column("Phone Number", anchor=CENTER, width=120,minwidth=120,stretch=NO)
my_tree.column("Position Applied", anchor=W, width=130,minwidth=130,stretch=NO)
my_tree.column("Language (Written)", anchor=W, width=130,minwidth=130,stretch=NO)
my_tree.column("Language (Spoken)", anchor=W, width=130,minwidth=130,stretch=NO)
my_tree.column("Programming Language",anchor=W, width=140,minwidth=140,stretch=NO)
my_tree.column("Past Work Experience", anchor=W, width=130,minwidth=130,stretch=NO)
my_tree.column("Duration", anchor=CENTER, width=120,minwidth=120,stretch=NO)
my_tree.column("Highest Education", anchor=W, width=130,minwidth=130,stretch=NO)
my_tree.column("Soft Skills", anchor=W, width=120,minwidth=120,stretch=NO)

#Create Header
my_tree.heading("#0", text=" ", anchor=W)
my_tree.heading("Name", text="Name", anchor=W)
my_tree.heading("Email", text="Email", anchor=W)
my_tree.heading("IC No.", text="IC No.", anchor=CENTER)
my_tree.heading("Phone Number", text="Phone Number", anchor=CENTER)
my_tree.heading("Position Applied", text="Position Applied", anchor=W)
my_tree.heading("Language (Written)",text="Language (Written)", anchor=W)
my_tree.heading("Language (Spoken)",text="Language (Spoken)", anchor=W)
my_tree.heading("Programming Language",text="Programing Language",anchor=W)
my_tree.heading("Past Work Experience",text="Past Work Experience", anchor=W)
my_tree.heading("Duration", text="Duration",anchor=CENTER)
my_tree.heading("Highest Education", text="Highest Education",anchor=W)
my_tree.heading("Soft Skills", text="Soft skills",anchor=W)

#Checkbox for name search bar to appear
def nametoggle():
	if nameVar.get():
		namesearch.place(anchor="nw",x=160,y=290,width=200)
	else:
		namesearch.place_forget()
		namesearch.delete(0,'end')
nameVar= BooleanVar()
namebox = Checkbutton(root, text="Name", variable=nameVar,command=nametoggle)
namesearch=Entry(root)
my_canvas.create_window(160,260, anchor="nw",window=namebox)

#Checkbox for IC search bar to appear
def ICtoggle():
	if ICVar.get():
		ICsearch.place(anchor="nw",x=520,y=290,width=80)
	else:
		ICsearch.place_forget()
		ICsearch.delete(0,'end')
ICVar=BooleanVar()
ICbox = Checkbutton(root, text="IC No.", variable=ICVar,command=ICtoggle)
ICsearch=Entry(root)
my_canvas.create_window(520,260,anchor="nw",window=ICbox)

#Checkbox for position applied search bar to appear
def Postoggle():
	if PosVar.get():
		Possearch.place(anchor="nw",x=720,y=290,width=120)
	else:
		Possearch.place_forget()
		Possearch.delete(0,'end')
PosVar=BooleanVar()
Posbox=Checkbutton(root, text="Position", variable=PosVar,command=Postoggle)
Possearch=Entry(root)
my_canvas.create_window(720,260,anchor="nw",window=Posbox)

#Checkbox for Language written search bar to appear
def Writtentoggle():
	if WrittenVar.get():
		Writtensearch.place(anchor="nw",x=850,y=290,width=120)
	else:
		Writtensearch.place_forget()
		Writtensearch.delete(0,'end')
WrittenVar=BooleanVar()
Writtenbox=Checkbutton(root,text="Language(Written)", variable=WrittenVar,command=Writtentoggle)
Writtensearch=Entry(root)
my_canvas.create_window(850,260,anchor="nw",window=Writtenbox)

#Checkbox for language spoken search bar to appear
def Spokentoggle():
	if SpokenVar.get():
		Spokensearch.place(anchor="nw",x=980,y=290,width=120)
	else:
		Spokensearch.place_forget()
		Spokensearch.delete(0,'end')
SpokenVar=BooleanVar()
Spokenbox=Checkbutton(root,text="Language(Spoken)", variable=SpokenVar,command=Spokentoggle)
Spokensearch=Entry(root)
my_canvas.create_window(980,260,anchor="nw",window=Spokenbox)

#Checkbox for programming language search bar to appear
def Programtoggle():
	if ProgramVar.get():
		Programsearch.place(anchor="nw",x=1110,y=290,width=130)
	else:
		Programsearch.place_forget()
		Programsearch.delete(0,'end')
ProgramVar=BooleanVar()
Programbox=Checkbutton(root,text="Program language", variable=ProgramVar,command=Programtoggle)
Programsearch=Entry(root)
my_canvas.create_window(1110,260,anchor="nw",window=Programbox)

#Checkbox for past work search bar to appear
def Exptoggle():
	if ExpVar.get():
		Expsearch.place(anchor="nw",x=1250,y=290,width=120)
	else:
		Expsearch.place_forget()
		Expsearch.delete(0,'end')
ExpVar=BooleanVar()
Expbox=Checkbutton(root,text="Past work exp", variable=ExpVar,command=Exptoggle)
Expsearch=Entry(root)
my_canvas.create_window(1250,260,anchor="nw",window=Expbox)

#Checkbox for highest education search bar to appear
def Edutoggle():
	if EduVar.get():
		Edusearch.place(anchor="nw",x=1500,y=290,width=120)
	else:
		Edusearch.place_forget()
		Edusearch.delete(0,'end')
EduVar=BooleanVar()
Edubox=Checkbutton(root,text="Highest Education", variable=EduVar,command=Edutoggle)
Edusearch=Entry(root)
my_canvas.create_window(1500,260,anchor="nw",window=Edubox)

#Checkbox for soft skills search bar to appear
def SoftSkilltoggle():
	if SoftSkillVar.get():
		SoftSkillsearch.place(anchor="nw",x=1630,y=290,width=120)
	else:
		SoftSkillsearch.place_forget()
		SoftSkillsearch.delete(0,'end')
SoftSkillVar=BooleanVar()
SoftSkillbox=Checkbutton(root,text="Soft Skills", variable=SoftSkillVar,command=SoftSkilltoggle)
SoftSkillsearch=Entry(root)
my_canvas.create_window(1630,260,anchor="nw",window=SoftSkillbox)

#Search Button (Need to add command)
ButtonSearch = Button(root, text="Search", borderwidth=0,highlightthickness=0,bd=0)
my_canvas.create_window(1770,290,anchor="nw",window=ButtonSearch)

#Dummy data to test scroll feature pls remove when testing to insert data from database
#Add dataheading
my_tree.insert(parent="", index="end", iid=0, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislsu01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=1, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=2, text="", values=("Muhammad Darwis Bins Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=3, text="", values=("Muhammad Darwisss Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=7, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=8, text="", values=("Muhammad Dsrwis Bin Akmal Lau", "darwislas01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=9, text="", values=("Muhammad Darwis Bsin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=10, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=11, text="", values=("Muhammad Dxarwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=14, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@smail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=15, text="", values=("Muhammad DarwisdBin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=16, text="", values=("Muhammad Dasrwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=17, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=18, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmasil.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=19, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=20, text="", values=("Muhammad sis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=25, text="", values=("Muhammad Darwiss Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=27, text="", values=("Muhasmmad Darwis Bin Akmal Lau", "darwialas01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=28, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=29, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwsislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=30, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))
my_tree.insert(parent="", index="end", iid=31, text="", values=("Muhammad Darwis Bin Akmal Lau", "darwislau01@gmail.com", 990811075213, +601112412505, "Software Engineer", "Technician"))


root.mainloop()