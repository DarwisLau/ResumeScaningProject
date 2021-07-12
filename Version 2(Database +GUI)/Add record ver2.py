from tkinter import*
from tkinter.font import Font



#Function executed when Save button is pressed
def insertNewRecord ():

    """Function to add new record into the database.
       This function does not have specific input parameters, but the function will get the applicant's information from the form.
       Output is a message box that shows the message "Record successfully added" if the insertion was successful, or promts error message if the insertion was not successful."""

    
    #Validate data and set the variables
    from ValidateData import standardise_applicantICNumber, validate_applicantICNumber, standardise_applicantEmail, validate_applicantEmail, standardise_applicantContactNumber, validate_applicantContactNumber, validate_otherData
    #ValidateData contains code for data validation.
    #It is used to make sure that the data is valid before it is inserted into the database.
    #Source: Part of this project
    from tkinter import messagebox
    
    #IC number
    dataICNumber = entryIC.get()
    dataICNumber = standardise_applicantICNumber (dataICNumber)
    errorMessage = validate_applicantICNumber (dataICNumber)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return

    #Email address
    dataEmail = entryEmail.get()
    dataEmail = standardise_applicantEmail (dataEmail)
    errorMessage = validate_applicantEmail (dataEmail)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return

    #Contact number
    dataContactNumber = entryContact.get()
    dataContactNumber = standardise_applicantContactNumber (dataContactNumber)
    errorMessage = validate_applicantContactNumber (dataContactNumber)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return

    #Name, position applied, language (written), language (spoken), programming language, past work experience, past work duration, highest education, soft skill
    dataName = entryName.get()
    dataPositionApplied = entryPosition.get()
    dataLanguageWritten = entryLangWrite.get()
    dataLanguageSpoken = entryLangSpoke.get()
    dataProgrammingLanguage = entryCodeLang.get()
    dataPastWorkExperience = entryWorkExp.get()
    dataPastWorkDuration = entryDuration.get()
    dataHighestEducation = entryHighestEdu.get()
    dataSoftSkill = entrySoftSkill.get() #Still not sure about the "entrySoftSkill" name
    errorMessage = validate_otherData (dataName, dataPositionApplied, dataLanguageWritten, dataLanguageSpoken, dataProgrammingLanguage, dataPastWorkExperience, dataPastWorkDuration, dataHighestEducation, dataSoftSkill)
    if errorMessage is not None:
        messagebox.showinfo("Error", errorMessage)
        return

    outMessage = None
    

    #Insert into database
    import mysql.connector
    #mysql.conector is a driver to access mySQL database.
    #It is used to insert a new record into the database, and check whether the insertion of record was successful or not.
    #Source: It is installed together when installing the mySQL software using mySQL installer. Source of the mySQL installer: https://dev.mysql.com/downloads/installer/
    database = mysql.connector.connect (
        host = "localhost",
        user = "Resume_Scanning_Project_Admin",
        password = "AbcdeF,123456!",
        database = "ResumeScanningProject"
    )
    databaseCursor = database.cursor()
    try:
        returnMessage = databaseCursor.callproc ("InsertNewRecord", (dataICNumber, dataName, dataEmail, dataContactNumber, dataLanguageWritten, dataLanguageSpoken, dataProgrammingLanguage, dataPastWorkExperience, dataPastWorkDuration, dataHighestEducation, dataSoftSkill, dataPositionApplied, outMessage))
        database.commit()
        if returnMessage[12] == "Record successfully added":
            messagebox.showinfo("", returnMessage[12])
        else:
            messagebox.showinfo("Error", returnMessage[12])
    except mysql.connector.Error as errorMessage:
        messagebox.showinfo("Error", errorMessage)
    finally:
        databaseCursor.close()
        database.close()



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

#Form fill
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

#Save Button
img_label = Label(image=SaveButtonImg)
entryButtonSave = Button(root, image=SaveButtonImg, borderwidth=0, highlightthickness=0, bd=0, command=insertNewRecord)
my_canvas.create_window(140, 803, anchor="nw", window=entryButtonSave)


root.mainloop()
