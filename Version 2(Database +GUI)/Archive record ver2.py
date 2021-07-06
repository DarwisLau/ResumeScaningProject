from tkinter import*
from tkinter.font import Font


#Window size, title
root = Tk()
root.geometry('1920x1080')
root.maxsize(1920,1080)
root.title("Archive Record")

#Define image for Background and button
bg= PhotoImage(file='D:/GUI Image/background.png')
SaveButtonImg =PhotoImage(file='D:/GUI Image/update button.png')
BackToMenuButtonImg =PhotoImage(file='D:/GUI Image/Back to menu.png')
ActCheckboxImg= PhotoImage(file='D:/GUI Image/active.png')
InactCheckboxImg=PhotoImage(file='D:/GUI Image/inactive.png')
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
FormFont = Font(family="Montserrat Medium", size=25, weight="normal",slant="roman",underline=0,overstrike=0)
FillFont = Font(family="Montserrat Medium", size=20, weight="normal",slant="roman",underline=0,overstrike=0)


#Creating Header
Header = Canvas(root, width=1920,height=158,bg='#BAE2DC')
Header.place(x=0,y=0)
Header.configure(highlightbackground='#707070')

#header text
Header.create_text(140,42,anchor="nw", text="Resume Scanning Project", font=Header1Font)
Header.create_text(1549,42,anchor="nw", text="Archive Record", font=Header2Font)
Header.create_text(140,85,anchor="nw", text="ALL Project by Muhammad Darwis and Chan Khai Shen", font=Header3Font)

#Search applicant using IC No.
my_canvas.create_text(140,203,anchor="nw", text="Search Applicant Using IC No.:", font=FormFont)
my_canvas.create_text(140,254,anchor="nw", text="Applicant IC No. :", font=FillFont)

#Search Button (Need to add command)
img_label = Label(image=SearchButtonImg)
ButtonSave = Button(root, image=SearchButtonImg, borderwidth=0,highlightthickness=0,bd=0)
my_canvas.create_window(1110,252,anchor="nw",window=ButtonSave)

#Display Applicant info text
my_canvas.create_text(140,309,anchor="nw", text="Name:", font=FillFont)
my_canvas.create_text(140,364,anchor="nw", text="Email Address:", font=FillFont)
my_canvas.create_text(140,419,anchor="nw", text="Contact No.:", font=FillFont)
my_canvas.create_text(140,474,anchor="nw", text="Position Applied:", font=FillFont)
my_canvas.create_text(140,529,anchor="nw", text="Language (written):", font=FillFont)
my_canvas.create_text(140,584,anchor="nw", text="Language (spoken):", font=FillFont)
my_canvas.create_text(140,639,anchor="nw", text="Programming Language:", font=FillFont)
my_canvas.create_text(140,694,anchor="nw", text="Past Work Experience:", font=FillFont)
my_canvas.create_text(880,694,anchor="nw", text="Duration:", font=FillFont)
my_canvas.create_text(140,749,anchor="nw", text="Highest Education:", font=FillFont)
my_canvas.create_text(140,804,anchor="nw", text="Applicant Status:", font=FillFont)

#Form fill (Must add command for input)
entryIC = Entry(root, width = 100)
my_canvas.create_window(500, 265, anchor="nw", window=entryIC)

#Display Applicant Info space (Must display info from database)
query_Label_Name = Label(root, width=85)
my_canvas.create_window(500, 318, anchor="nw", window=query_Label_Name)

query_Label_Email = Label(root, width = 85)
my_canvas.create_window(500, 375, anchor="nw", window=query_Label_Email)

query_Label_Contact = Label(root, width = 85)
my_canvas.create_window(500, 428, anchor="nw", window=query_Label_Contact)

query_Label_Position = Label(root, width = 85)
my_canvas.create_window(500, 483, anchor="nw", window=query_Label_Position)

query_Label_LangWrite = Label(root, width = 85)
my_canvas.create_window(500, 538, anchor="nw", window=query_Label_LangWrite)

query_Label_LangSpoke = Label(root, width = 85)
my_canvas.create_window(500, 592, anchor="nw", window=query_Label_LangSpoke)

query_Label_CodeLang = Label(root, width = 85)
my_canvas.create_window(500, 650, anchor="nw", window=query_Label_CodeLang)

query_Label_WorkExp = Label(root, width = 50)
my_canvas.create_window(500, 704, anchor="nw", window=query_Label_WorkExp)

query_Label_Duration = Label(root, width = 50)
my_canvas.create_window(1040, 704, anchor="nw", window=query_Label_Duration)

query_Label_HighestEdu = Label(root, width = 85)
my_canvas.create_window(500, 762, anchor="nw", window=query_Label_HighestEdu)

#Save Button (Need to add command)
img_label = Label(image=SaveButtonImg)
entryButtonSave = Button(root, image=SaveButtonImg, borderwidth=0, highlightthickness=0, bd=0)
my_canvas.create_window(140, 858, anchor="nw", window=entryButtonSave)

#Back to Menu Button (need to add command)
img_label = Label(image=BackToMenuButtonImg)
entryButtonMenu = Button(root, image=BackToMenuButtonImg, borderwidth=0, highlightthickness=0, bd=0)
my_canvas.create_window(1602, 189, anchor="nw", window=entryButtonMenu)

#RadioButton to change applicant status (need to add command and link to button)
var = IntVar()

ActiveCheck=Radiobutton(root, image=ActCheckboxImg, variable=var, value=1, borderwidth=0, highlightthickness=0,bd=0)
my_canvas.create_window(471,804, anchor="nw", window=ActiveCheck)

InActiveCheck=Radiobutton(root, image=InactCheckboxImg, variable=var,value=2,borderwidth=0, highlightthickness=0,bd=0)
my_canvas.create_window(630,804, anchor="nw", window=InActiveCheck)



root.mainloop()