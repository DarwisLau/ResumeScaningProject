from tkinter import*
from tkinter.font import Font


#Window size, title
root = Tk()
root.geometry('1920x1080')
root.maxsize(1920,1080)
root.title("Add Record")

#Define image for Background and button
bg= PhotoImage(file='D:/GUI Image/background.png')
SaveButtonImg =PhotoImage(file='D:/GUI Image/Save button.png')
BackToMenuButtonImg =PhotoImage(file='D:/GUI Image/Back to menu.png')

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
Header.create_text(1602,42,anchor="nw", text="Add Record", font=Header2Font)
Header.create_text(140,85,anchor="nw", text="ALL Project by Muhammad Darwis and Chan Khai Shen", font=Header3Font)

#Form text
my_canvas.create_text(140,203,anchor="nw", text="Enter Applicants Information:", font=FormFont)
my_canvas.create_text(140,254,anchor="nw", text="Applicant IC No. :", font=FillFont)
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
my_canvas.create_text(140,810,anchor="nw", text="Soft Skills:", font=FillFont)

#Form fill (Must add command for input)
entryIC = Entry(root, width = 100)
my_canvas.create_window(500, 265, anchor="nw", window=entryIC)

entryName = Entry(root, width = 100)
my_canvas.create_window(500, 318, anchor="nw", window=entryName)

entryEmail = Entry(root, width = 100)
my_canvas.create_window(500, 375, anchor="nw", window=entryEmail)

entryContact = Entry(root, width = 100)
my_canvas.create_window(500, 428, anchor="nw", window=entryContact)

entryPosition = Entry(root, width = 100)
my_canvas.create_window(500, 483, anchor="nw", window=entryPosition)

entryLangWrite = Entry(root, width = 100)
my_canvas.create_window(500, 538, anchor="nw", window=entryLangWrite)

entryLangSpoke = Entry(root, width = 100)
my_canvas.create_window(500, 592, anchor="nw", window=entryLangSpoke)

entryCodeLang = Entry(root, width = 100)
my_canvas.create_window(500, 650, anchor="nw", window=entryCodeLang)

entryWorkExp = Entry(root, width = 60)
my_canvas.create_window(500, 704, anchor="nw", window=entryWorkExp)

entryDuration = Entry(root, width = 60)
my_canvas.create_window(1040, 704, anchor="nw", window=entryDuration)

entryHighestEdu = Entry(root, width = 100)
my_canvas.create_window(500, 762, anchor="nw", window=entryHighestEdu)

entrySoftSkills = Entry(root, width = 100)
my_canvas.create_window(500, 820, anchor="nw", window=entrySoftSkills)

#Save Button (Need to add function)
img_label = Label(image=SaveButtonImg)
ButtonSave = Button(root, image=SaveButtonImg, borderwidth=0, highlightthickness=0, bd=0)
my_canvas.create_window(140, 878, anchor="nw", window=ButtonSave)



root.mainloop()