from tkinter import*
from tkinter.font import Font
from tkinter import messagebox

import mysql.connector
#mysql.conector is a driver to access mySQL database.
#It is used to select active applicant's information from the database and update applicant's information in the database.
#Source: It is installed together when installing the mySQL software using mySQL installer. Source of the mySQL installer: https://dev.mysql.com/downloads/installer/

from ValidateData import standardise_applicantICNumber, validate_applicantICNumber, standardise_applicantEmail, validate_applicantEmail, standardise_applicantContactNumber, validate_applicantContactNumber, validate_otherData
#ValidateData contains code for data validation.
#It is used to make sure that data is valid before it is pased into the database, to select or update active applicant's information.
#Source: Part of this project


#Window size, title
root = Tk()
root.geometry('1920x1080')
root.maxsize(1920,1080)
root.title("Edit Record")

#Define image for Background and button
bg= PhotoImage(file='D:/GUI Image/background.png')
SaveEditButtonImg =PhotoImage(file='D:/GUI Image/save edit button.png')
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
Header.create_text(1549,42,anchor="nw", text="Edit Record", font=Header2Font)
Header.create_text(140,85,anchor="nw", text="ALL Project by Muhammad Darwis and Chan Khai Shen", font=Header3Font)

#Form text
my_canvas.create_text(140,203,anchor="nw", text="Search Applicant Using IC No.:", font=FormFont)
my_canvas.create_text(140,254,anchor="nw", text="Applicant IC No. :", font=FillFont)

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

#IC search fill
entryIC = Entry(root, width = 100)
my_canvas.create_window(500, 265, anchor="nw", window=entryIC)

#Function executed when Search Button is pressed
def selectOneFromActiveRecords ():

    """Function to select an active applicant's information from database and return the information to the blank spaces.
       This function does not have specific input parameters, but the function will get the applicant's IC number from the IC search panel (expected string).
       Output is either applicant's information (displayed in the entries), or a message box that shows the error message from the database software. If the applicant does not exist in the
       database or is not active, then all blank spaces will not be fiiled."""

    #Clear the entries
    entryList = [entryName, entryEmail, entryContact, entryPosition, entryLangWrite, entryLangSpoke, entryCodeLang, entryWorkExp, entryDuration, entryHighestEdu, entrySoftSkills]
    for entry in entryList:
        entry.delete(0, END)

    #Get and validate IC number
    dataICNumber = entryIC.get()
    dataICNumber = standardise_applicantICNumber (dataICNumber)
    errorMessage = validate_applicantICNumber (dataICNumber)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return

    #Select from database
    database = mysql.connector.connect (
        host = "localhost",
        user = "Resume_Scanning_Project_Admin",
        password = "AbcdeF,123456!",
        database = "ResumeScanningProject"
    )
    databaseCursor = database.cursor()
    try:
        databaseCursor.callproc ("SelectOneFromActiveRecords", (dataICNumber,))

        #Display the applicant's information in the entries
        index = 0
        for result in databaseCursor.stored_results():
            for row in result.fetchall():
                while index <= 10:
                    entryList[index].insert(0, row[index])
                    index += 1

    except mysql.connector.Error as errorMessage:
        messagebox.showinfo("Error", errorMessage)
    finally:
        databaseCursor.close()
        database.close()

#Search Button
img_label = Label(image=SearchButtonImg)
ButtonSave = Button(root, image=SearchButtonImg, borderwidth=0,highlightthickness=0,bd=0,command=selectOneFromActiveRecords)
my_canvas.create_window(1110,252,anchor="nw",window=ButtonSave)

#Edit fill
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

entrySoftSkills = Entry(root,width = 100)
my_canvas.create_window(500, 820, anchor="nw", window=entrySoftSkills)

#Function executed when Save Edit Button is pressed
def updateRecord ():

    """Function to update applicant's information in the database.
       This function does not have specific input parameters, but the functio will get the applicant's information from the entries.
       Output is a message box that shows the message "Record successfully edited" if the update was successful, or a message box that promts error message if the update was not successful."""

    #Get data, validate data and set the variables
    dataICNumber = entryIC.get()
    dataICNumber = standardise_applicantICNumber (dataICNumber)
    errorMessage = validate_applicantICNumber (dataICNumber)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return
    dataEmail = entryEmail.get()
    dataEmail = standardise_applicantEmail (dataEmail)
    errorMessage = validate_applicantEmail (dataEmail)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return
    dataContactNumber = entryContact.get()
    dataContactNumber = standardise_applicantContactNumber (dataContactNumber)
    errorMessage = validate_applicantContactNumber (dataContactNumber)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return
    dataName = entryName.get()
    dataPositionApplied = entryPosition.get()
    dataLanguageWritten = entryLangWrite.get()
    dataLanguageSpoken = entryLangSpoke.get()
    dataProgrammingLanguage = entryCodeLang.get()
    dataPastWorkExperience = entryWorkExp.get()
    dataPastWorkDuration = entryDuration.get()
    dataHighestEducation = entryHighestEdu.get()
    dataSoftSkill =  entrySoftSkills.get()
    errorMessage = validate_otherData (dataName, dataPositionApplied, dataLanguageWritten, dataLanguageSpoken, dataProgrammingLanguage, dataPastWorkExperience, dataPastWorkDuration, dataHighestEducation, dataSoftSkill)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return
    outMessage = None

    #Update in database
    database = mysql.connector.connect (
        host = "localhost",
        user = "Resume_Scanning_Project_Admin",
        password = "AbcdeF,123456!",
        database = "ResumeScanningProject"
    )
    databaseCursor = database.cursor()
    try:
        returnMessage = databaseCursor.callproc ("UpdateRecord", (dataICNumber, dataName, dataEmail, dataContactNumber, dataLanguageWritten, dataLanguageSpoken, dataProgrammingLanguage, dataPastWorkExperience, dataPastWorkDuration, dataHighestEducation, dataSoftSkill, dataPositionApplied, outMessage))
        database.commit()
        if returnMessage[12] == "Record successfully edited":
            messagebox.showinfo("", returnMessage[12])
        else:
            messagebox.showinfo("Error", returnMessage[12])
    except mysql.connector.Error as errorMessage:
        messagebox.showinfo("Error", errorMessage)
    finally:
        databaseCursor.close()
        database.close()


#Save Edit Button
img_label = Label(image=SaveEditButtonImg)
ButtonSaveEdit = Button(root, image=SaveEditButtonImg, borderwidth=0, highlightthickness=0, bd=0, command=updateRecord)
my_canvas.create_window(140, 803, anchor="nw", window=ButtonSaveEdit)


root.mainloop()
