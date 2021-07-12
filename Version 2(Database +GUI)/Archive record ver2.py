from tkinter import*
from tkinter.font import Font



#Function executed when Search Button is pressed
def selectOneFromAllRecords():

    """Function to select an applicant's information from database and return the information to the applicant info section.
       This function does not have specific input parameters, but the function will get the applicant's IC number from the IC search panel (expected string).
       Output is either applicant's information (displayed in applicant info section), or a message box that shows the error message (if there is any error message) from the database software. If the applicant does not exist in the
       database, the applicant info section will be left blank. If the applicant's programming language column is empty, the line for programming language will be left blank."""


    #Set the variables
    dataICNumber = entryIC.get()
    from ValidateData_ver2 import standardise_applicantICNumber
    #ValidateData contains code for data validation.
    #It is used to remove "-" or space from IC number before it is used to query applicant's information in the database.
    #Source: Part of this project
    dataICNumber = standardise_applicantICNumber (dataICNumber)
    dataName = ""
    dataEmail = ""
    dataContactNumber = ""
    dataPositionApplied = ""
    dataLanguageWritten = ""
    dataLanguageSpoken = ""
    dataProgrammingLanguage = ""
    dataPastWorkExperience = ""
    dataPastWorkDuration = ""
    dataHighestEducation = ""
    dataSoftSkill = ""
    dataIsActive = ""


    #Select from database
    import mysql.connector
    #mysql.conector is a driver to access mySQL database.
    #It is used to query applicant's information in the database, and get the result of the query.
    #Source: It is installed together when installing the mySQL software using mySQL installer. Source of the mySQL installer: https://dev.mysql.com/downloads/installer/
    database = mysql.connector.connect (
        host = "localhost",
        user = "Resume_Scanning_Project_Admin",
        password = "AbcdeF,123456!",
        database = "ResumeScanningProject"
    )
    databaseCursor = database.cursor()
    try:
        result = databaseCursor.callproc ("SelectOneFromAllRecords", (dataICNumber, dataName, dataEmail, dataContactNumber, dataPositionApplied, dataLanguageWritten, dataLanguageSpoken, dataProgrammingLanguage, dataPastWorkExperience, dataPastWorkDuration, dataHighestEducation, dataSoftSkill, dataIsActive))

        #Display the applicant's information in the applicant info section
        if result[1] is None:
            text_Name.set("")
        else:
            text_Name.set(result[1])
        if result[2] is None:
            text_Email.set("")
        else:
            text_Email.set(result[2])
        if result[3] is None:
            text_Contact.set("")
        else:
            text_Contact.set(result[3])
        if result[4] is None:
            text_Position.set("")
        else:
            text_Position.set(result[4])
        if result[5] is None:
            text_LangWrite.set("")
        else:
            text_LangWrite.set(result[5])
        if result[6] is None:
            text_LangSpoke.set("")
        else:
            text_LangSpoke.set(result[6])
        if result[7] is None:
            text_CodeLang.set("")
        else:
            text_CodeLang.set(result[7])
        if result[8] is None:
            text_WorkExp.set("")
        else:
            text_WorkExp.set(result[8])
        if result[9] is None:
            text_Duration.set("")
        else:
            text_Duration.set(result[9])
        if result[10] is None:
            text_HighestEdu.set("")
        else:
            text_HighestEdu.set(result[10])
        if result[11] is None:
            text_SoftSkill.set("")
        else:
            text_SoftSkill.set(result[11])
        var.set(result[12])

    except mysql.connector.Error as errorMessage:
        from tkinter import messagebox
        messagebox.showinfo("Error", errorMessage)
    finally:
        databaseCursor.close()
        database.close()



#Function executed when Save Button is pressed
def changeArchiveStatus ():

    """Function to change an applicant's archive status in the database.
       This function does not have specific input parameters, but the functio will get the applicant's new archive status from the radio button.
       Output is a message box that shows the message "Record status changed" if the change of archive status was successful, or promts error message if the change of archive status was not successful."""
   

    #Validate data and set the variables
    from ValidateData import standardise_applicantICNumber
    #ValidateData contains code for data validation.
    #It is used to remove "-" and space from IC number and make sure that the other data is valid before it is updated in the database.
    #Source: Part of this project
    from tkinter import messagebox
    
    #IC number
    dataICNumber = entryIC.get()
    dataICNumber = standardise_applicantICNumber (dataICNumber)

    #Archive status
    dataIsActive = var.get()

    outMessage = None


    #Change archive status in database
    import mysql.connector
    #mysql.conector is a driver to access mySQL database.
    #It is used to update applicant's information in the database, and check whether the update was successful or not.
    #Source: It is installed together when installing the mySQL software using mySQL installer. Source of the mySQL installer: https://dev.mysql.com/downloads/installer/
    database = mysql.connector.connect (
        host = "localhost",
        user = "Resume_Scanning_Project_Admin",
        password = "AbcdeF,123456!",
        database = "ResumeScanningProject"
    )
    databaseCursor = database.cursor()
    try:
        returnMessage = databaseCursor.callproc ("ChangeArchiveStatus", (dataICNumber, dataIsActive, outMessage))
        database.commit()
        if returnMessage[2] == "Record status changed":
            messagebox.showinfo("", returnMessage[2])
        else:
            messagebox.showinfo("Error", returnMessage[2])
    except mysql.connector.Error as errorMessage:
        messagebox.showinfo("Error", errorMessage)
    finally:
        databaseCursor.close()
        database.close()



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

#Search Button
img_label = Label(image=SearchButtonImg)
ButtonSave = Button(root, image=SearchButtonImg, borderwidth=0,highlightthickness=0,bd=0,command=selectOneFromAllRecords)
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

#Form fill
entryIC = Entry(root, width = 100)
my_canvas.create_window(500, 265, anchor="nw", window=entryIC)

#Display Applicant Info textvariable
text_Name = StringVar()
text_Email = StringVar()
text_Contact = StringVar()
text_Position = StringVar()
text_LangWrite = StringVar()
text_LangSpoke = StringVar()
text_CodeLang = StringVar()
text_WorkExp = StringVar()
text_Duration = StringVar()
text_HighestEdu = StringVar()
text_SoftSkill = StringVar()

#Display Applicant Info space
query_Label_Name = Label(root, width=85, textvariable=text_Name)
my_canvas.create_window(500, 318, anchor="nw", window=query_Label_Name)

query_Label_Email = Label(root, width = 85, textvariable=text_Email)
my_canvas.create_window(500, 375, anchor="nw", window=query_Label_Email)

query_Label_Contact = Label(root, width = 85, textvariable=text_Contact)
my_canvas.create_window(500, 428, anchor="nw", window=query_Label_Contact)

query_Label_Position = Label(root, width = 85, textvariable=text_Position)
my_canvas.create_window(500, 483, anchor="nw", window=query_Label_Position)

query_Label_LangWrite = Label(root, width = 85, textvariable=text_LangWrite)
my_canvas.create_window(500, 538, anchor="nw", window=query_Label_LangWrite)

query_Label_LangSpoke = Label(root, width = 85, textvariable=text_LangSpoke)
my_canvas.create_window(500, 592, anchor="nw", window=query_Label_LangSpoke)

query_Label_CodeLang = Label(root, width = 85, textvariable=text_CodeLang)
my_canvas.create_window(500, 650, anchor="nw", window=query_Label_CodeLang)

query_Label_WorkExp = Label(root, width = 50, textvariable=text_WorkExp)
my_canvas.create_window(500, 704, anchor="nw", window=query_Label_WorkExp)

query_Label_Duration = Label(root, width = 50, textvariable=text_Duration)
my_canvas.create_window(1040, 704, anchor="nw", window=query_Label_Duration)

query_Label_HighestEdu = Label(root, width = 85, textvariable=text_HighestEdu)
my_canvas.create_window(500, 762, anchor="nw", window=query_Label_HighestEdu)

#Save Button
img_label = Label(image=SaveButtonImg)
entryButtonSave = Button(root, image=SaveButtonImg, borderwidth=0, highlightthickness=0, bd=0, command=changeArchiveStatus)
my_canvas.create_window(140, 858, anchor="nw", window=entryButtonSave)


#RadioButton to change applicant status
var = IntVar()

ActiveCheck=Radiobutton(root, image=ActCheckboxImg, variable=var, value=1, borderwidth=0, highlightthickness=0,bd=0)
my_canvas.create_window(471,804, anchor="nw", window=ActiveCheck)

InActiveCheck=Radiobutton(root, image=InactCheckboxImg, variable=var,value=0,borderwidth=0, highlightthickness=0,bd=0)
my_canvas.create_window(630,804, anchor="nw", window=InActiveCheck)


root.mainloop()
