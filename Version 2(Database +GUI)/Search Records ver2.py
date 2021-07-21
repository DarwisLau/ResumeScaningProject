from tkinter import*
from tkinter import ttk
from tkinter.font import Font
from tkinter import messagebox
from tkinter.ttk import Treeview
from tkinter.ttk import Scrollbar

import mysql.connector
#mysql.conector is a driver to access mySQL database.
#It is used to select active applicant's information, for those who fulfill the criteria, from the database.
#Source: It is installed together when installing the mySQL software using mySQL installer. Source of the mySQL installer: https://dev.mysql.com/downloads/installer/


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

#Function called by selectFromActiveRecords_AND_OR() function
def determine_numberOfCriteriaFulfilled(record):

        """Function to determine and return the number of criteria that an applicant fulfilled.
           Input should be a 12-element list, which is one row of the results the execution of SelectFromActiveRecords procedure in the database.
           Output is integer."""

        #Determine the number of criteria fulfilled
        numberOfCriteriaFulfilled = 0
        if criteriaList[0] is not None and record[5].lower().find(criteriaList[0]) != -1: #languageWritten == dataLanguageWritten_1
                numberOfCriteriaFulfilled += 1
        if criteriaList[1] is not None and record[5].lower().find(criteriaList[1]) != -1: #languageWritten == dataLanguageWritten_2
                numberOfCriteriaFulfilled += 1
        if criteriaList[2] is not None and record[5].lower().find(criteriaList[2]) != -1: #languageWritten == dataLanguageWritten_3
                numberOfCriteriaFulfilled += 1
        if criteriaList[3] is not None and record[6].lower().find(criteriaList[3]) != -1: #languageSpoken == dataLanguageSpoken_1
                numberOfCriteriaFulfilled += 1
        if criteriaList[4] is not None and record[6].lower().find(criteriaList[4]) != -1: #languageSpoken == dataLanguageSpoken_2
                numberOfCriteriaFulfilled += 1
        if criteriaList[5] is not None and record[6].lower().find(criteriaList[5]) != -1: #languageSpoken == dataLanguageSpoken_3
                numberOfCriteriaFulfilled += 1
        if criteriaList[6] is not None and record[7].lower().find(criteriaList[6]) != -1: #programmingLanguage == dataProgrammingLanguage_1
                numberOfCriteriaFulfilled += 1
        if criteriaList[7] is not None and record[7].lower().find(criteriaList[7]) != -1: #programmingLanguage == dataProgrammingLanguage_2
                numberOfCriteriaFulfilled += 1
        if criteriaList[8] is not None and record[7].lower().find(criteriaList[8]) != -1: #programmingLanguage == dataProgrammingLanguage_3
                numberOfCriteriaFulfilled += 1
        if criteriaList[9] is not None and record[8].lower().find(criteriaList[9]) != -1: #pastWorkExperience == dataPastWorkExperience
                numberOfCriteriaFulfilled += 1
        if criteriaList[10] is not None and record[10].lower().find(criteriaList[10]) != -1: #highestEducation == dataHighestEducation
                numberOfCriteriaFulfilled += 1
        if criteriaList[11] is not None and record[11].lower().find(criteriaList[11]) != -1: #softSkill == dataSoftSkill_1
                numberOfCriteriaFulfilled += 1
        if criteriaList[12] is not None and record[11].lower().find(criteriaList[12]) != -1: #softskill == dataSoftSkill_2
                numberOfCriteriaFulfilled += 1
        if criteriaList[13] is not None and record[11].lower().find(criteriaList[13]) != -1: #softSkill == dataSoftSkill_3
                numberOfCriteriaFulfilled += 1
        if criteriaList[14] is not None and record[11].lower().find(criteriaList[14]) != -1: #softSkill == dataSoftSkill_4
                numberOfCriteriaFulfilled += 1
        if criteriaList[15] is not None and record[11].lower().find(criteriaList[15]) != -1: #softSkill == dataSoftSkill_5
                numberOfCriteriaFulfilled += 1
        return numberOfCriteriaFulfilled

#Function executed when Search button is pressed
def selectFromActiveRecords():        

        """Function to select all active applicants that fulfill one of the criteria listed by user.
           This function does not have specific input parameters, but the function will get the criteria from the search bar.
           Output is either one or multiple rows of active applicants' information, for those who fulfill one of the criteria; or all active applicants, if all of the search bars is empty; or a message box that shows error message. If there are no active applicants or none of the active applicants fulfill the criteria, the table will be left blank."""

        #Get criteria from search bar
        if nameVar.get():
                dataName = namesearch.get()
                if len(dataName) > 150:
                        messagebox.showinfo("Error", "The character limit for applicant's name is 150.")
                        return
                dataName = "%" + dataName + "%"
        else:
                dataName = "%%"
        if ICVar.get():
                dataICNumber = ICsearch.get()
                dataICNumber = dataICNumber.replace(" ", "")
                dataICNumber = dataICNumber.replace("-", "")
                if len(dataICNumber) > 12:
                        messagebox.showinfo("Error", "The maximum number of digits of IC number is 12.")
                        return
                dataICNumber = "%" + dataICNumber + "%"
        else:
                dataICNumber = "%%"
        if PosVar.get():
                dataPositionApplied = Possearch.get()
                if len(dataPositionApplied) > 50:
                        messagebox.showinfo("Error", "The character limit for position applied is 50.")
                        return
                dataPositionApplied = "%" + dataPositionApplied + "%"
        else:
                dataPositionApplied = "%%"
        if WrittenVar.get():
                keywordLanguageWritten = Writtensearch.get()
                keywordLanguageWritten = keywordLanguageWritten.replace(", ", ",")
                keywordLanguageWritten = keywordLanguageWritten.replace(" ,", ",")
                listLanguageWritten = keywordLanguageWritten.split(",")
                for languageWritten in listLanguageWritten:
                        if len(languageWritten) >100:
                                messagebox.showinfo("Error", "The character limit for applicant's language (written) is 100.")
                                return
                if len(listLanguageWritten) > 3:
                        messagebox.showinfo("Error", "The maximum number of criteria for applicant's language (written) is 3.")
                        return
                elif len(listLanguageWritten) == 3:
                        dataLanguageWritten_1 = "%" + listLanguageWritten[0] + "%"
                        dataLanguageWritten_2 = "%" + listLanguageWritten[1] + "%"
                        dataLanguageWritten_3 = "%" + listLanguageWritten[2] + "%"
                elif len(listLanguageWritten) == 2:
                        dataLanguageWritten_1 = "%" + listLanguageWritten[0] + "%"
                        dataLanguageWritten_2 = "%" + listLanguageWritten[1] + "%"
                        dataLanguageWritten_3 = "%%"
                else:
                        dataLanguageWritten_1 = "%" + listLanguageWritten[0] + "%"
                        dataLanguageWritten_2 = "%%"
                        dataLanguageWritten_3 = "%%"
        else:
                dataLanguageWritten_1 = "%%"
                dataLanguageWritten_2 = "%%"
                dataLanguageWritten_3 = "%%"
        if SpokenVar.get():
                keywordLanguageSpoken = Spokensearch.get()
                keywordLanguageSpoken = keywordLanguageSpoken.replace(", ", ",")
                keywordLanguageSpoken = keywordLanguageSpoken.replace(" ,", ",")
                listLanguageSpoken = keywordLanguageSpoken.split(",")
                for languageSpoken in listLanguageSpoken:
                        if len(languageSpoken) >100:
                                messagebox.showinfo("Error", "The character limit for applicant's language (spoken) is 100.")
                                return
                if len(listLanguageSpoken) > 3:
                        messagebox.showinfo("Error", "The maximum number of criteria for applicant's language (spoken) is 3.")
                        return
                elif len(listLanguageSpoken) == 3:
                        dataLanguageSpoken_1 = "%" + listLanguageSpoken[0] + "%"
                        dataLanguageSpoken_2 = "%" + listLanguageSpoken[1] + "%"
                        dataLanguageSpoken_3 = "%" + listLanguageSpoken[2] + "%"
                elif len(listLanguageSpoken) == 2:
                        dataLanguageSpoken_1 = "%" + listLanguageSpoken[0] + "%"
                        dataLanguageSpoken_2 = "%" + listLanguageSpoken[1] + "%"
                        dataLanguageSpoken_3 = "%%"
                else:
                        dataLanguageSpoken_1 = "%" + listLanguageSpoken[0] + "%"
                        dataLanguageSpoken_2 = "%%"
                        dataLanguageSpoken_3 = "%%"
        else:
                dataLanguageSpoken_1 = "%%"
                dataLanguageSpoken_2 = "%%"
                dataLanguageSpoken_3 = "%%"
        if ProgramVar.get():
                keywordProgrammingLanguage = Programsearch.get()
                keywordProgrammingLanguage = keywordProgrammingLanguage.replace(", ", ",")
                keywordProgrammingLanguage = keywordProgrammingLanguage.replace(" ,", ",")
                listProgrammingLanguage = keywordProgrammingLanguage.split(",")
                for programmingLanguage in listProgrammingLanguage:
                        if len(programmingLanguage) >100:
                                messagebox.showinfo("Error", "The character limit for applicant's programming language is 100.")
                                return
                if len(listProgrammingLanguage) > 3:
                        messagebox.showinfo("Error", "The maximum number of criteria for applicant's programming language is 3.")
                        return
                elif len(listProgrammingLanguage) == 3:
                        dataProgrammingLanguage_1 = "%" + listProgrammingLanguage[0] + "%"
                        dataProgrammingLanguage_2 = "%" + listProgrammingLanguage[1] + "%"
                        dataProgrammingLanguage_3 = "%" + listProgrammingLanguage[2] + "%"
                elif len(listProgrammingLanguage) == 2:
                        dataProgrammingLanguage_1 = "%" + listProgrammingLanguage[0] + "%"
                        dataProgrammingLanguage_2 = "%" + listProgrammingLanguage[1] + "%"
                        dataProgrammingLanguage_3 = "%%"
                else:
                        dataProgrammingLanguage_1 = "%" + listProgrammingLanguage[0] + "%"
                        dataProgrammingLanguage_2 = "%%"
                        dataProgrammingLanguage_3 = "%%"
        else:
                dataProgrammingLanguage_1 = "%%"
                dataProgrammingLanguage_2 = "%%"
                dataProgrammingLanguage_3 = "%%"
        if ExpVar.get():
                dataPastWorkExperience = Expsearch.get()
                if len(dataPastWorkExperience) > 500:
                        messagebox.showinfo("Error", "The character limit for applicant's past work experience is 500.")
                        return
                dataPastWorkExperience = "%" + dataPastWorkExperience + "%"
        else:
                dataPastWorkExperience = "%%"
        if EduVar.get():
                dataHighestEducation = Edusearch.get()
                if len(dataHighestEducation) >100:
                        messagebox.showinfo("Error", "The character limit for applicant's highest education is 100.")
                        return
                dataHighestEducation = "%" + dataHighestEducation + "%"
        else:
                dataHighestEducation = "%%"
        if SoftSkillVar.get():
                keywordSoftSkill = SoftSkillsearch.get()
                keywordSoftSkill = keywordSoftSkill.replace(", ", ",")
                keywordSoftSkill = keywordSoftSkill.replace(" ,", ",")
                listSoftSkill = keywordSoftSkill.split(",")
                for softSkill in listSoftSkill:
                        if len(softSkill) >100:
                                messagebox.showinfo("Error", "The character limit for applicant's soft skill is 100.")
                                return
                if len(listSoftSkill) > 5:
                        messagebox.showinfo("Error", "The maximum number of criteria for soft skill is 5.")
                        return
                elif len(listSoftSkill) == 5:
                        dataSoftSkill_1 = "%" + listSoftSkill[0] + "%"
                        dataSoftSkill_2 = "%" + listSoftSkill[1] + "%"
                        dataSoftSkill_3 = "%" + listSoftSkill[2] + "%"
                        dataSoftSkill_4 = "%" + listSoftSkill[3] + "%"
                        dataSoftSkill_5 = "%" + listSoftSkill[4] + "%"
                elif len(listSoftSkill) == 4:
                        dataSoftSkill_1 = "%" + listSoftSkill[0] + "%"
                        dataSoftSkill_2 = "%" + listSoftSkill[1] + "%"
                        dataSoftSkill_3 = "%" + listSoftSkill[2] + "%"
                        dataSoftSkill_4 = "%" + listSoftSkill[3] + "%"
                        dataSoftSkill_5 = "%%"
                elif len(listSoftSkill) == 3:
                        dataSoftSkill_1 = "%" + listSoftSkill[0] + "%"
                        dataSoftSkill_2 = "%" + listSoftSkill[1] + "%"
                        dataSoftSkill_3 = "%" + listSoftSkill[2] + "%"
                        dataSoftSkill_4 = "%%"
                        dataSoftSkill_5 = "%%"
                elif len(listSoftSkill) == 2:
                        dataSoftSkill_1 = "%" + listSoftSkill[0] + "%"
                        dataSoftSkill_2 = "%" + listSoftSkill[1] + "%"
                        dataSoftSkill_3 = "%%"
                        dataSoftSkill_4 = "%%"
                        dataSoftSkill_5 = "%%"
                else:
                        dataSoftSkill_1 = "%" + listSoftSkill[0] + "%"
                        dataSoftSkill_2 = "%%"
                        dataSoftSkill_3 = "%%"
                        dataSoftSkill_4 = "%%"
                        dataSoftSkill_5 = "%%"
        else:
                dataSoftSkill_1 = "%%"
                dataSoftSkill_2 = "%%"
                dataSoftSkill_3 = "%%"
                dataSoftSkill_4 = "%%"
                dataSoftSkill_5 = "%%"

        #List out the criteria and remove"%" so that it can be used for sorting
        global criteriaList
        criteriaList = [dataLanguageWritten_1, dataLanguageWritten_2, dataLanguageWritten_3, dataLanguageSpoken_1, dataLanguageSpoken_2, dataLanguageSpoken_3, dataProgrammingLanguage_1, dataProgrammingLanguage_2, dataProgrammingLanguage_3, dataPastWorkExperience, dataHighestEducation, dataSoftSkill_1, dataSoftSkill_2, dataSoftSkill_3, dataSoftSkill_4, dataSoftSkill_5]
        count = 0
        while count <= 15:
                criterion = criteriaList[count]
                if criterion == "%%":
                        criterionOriginal = None
                else:
                        criterionOriginal = criterion.replace("%", "")
                        criterionOriginal = criterionOriginal.lower()
                criteriaList[count] = criterionOriginal
                count += 1

        #Select from the database
        database = mysql.connector.connect (
                host = "localhost",
                user = "Resume_Scanning_Project_Admin",
                password = "AbcdeF,123456!",
                database = "ResumeScanningProject"
        )
        databaseCursor = database.cursor()
        try:
                databaseCursor.callproc ("SelectFromActiveRecords", (dataName, dataICNumber, dataPositionApplied, dataLanguageWritten_1, dataLanguageWritten_2, dataLanguageWritten_3, dataLanguageSpoken_1, dataLanguageSpoken_2, dataLanguageSpoken_3, dataProgrammingLanguage_1, dataProgrammingLanguage_2, dataProgrammingLanguage_3, dataPastWorkExperience, dataHighestEducation, dataSoftSkill_1, dataSoftSkill_2, dataSoftSkill_3, dataSoftSkill_4, dataSoftSkill_5))

                #Clear the table
                for eachRow in my_tree.get_children():
                        my_tree.delete(eachRow)

                #Display in the table
                for result in databaseCursor.stored_results():
                        rowNumber = 0
                        heightOfTheRow = 20
                        for row in sorted(result, key = determine_numberOfCriteriaFulfilled, reverse = True):

                                #Display in multiple lines
                                heightOfRow = 20
                                characterLimitInLine = [23, 32, None, None, 15, 20, 20, 20, 19, 15, 20, 14]
                                listCell = []
                                number = 0
                                for number in range(number, 12, number+1):
                                        cell = row[number]
                                        lenCell = len(cell)
                                        limit = characterLimitInLine[number]
                                        if limit is not None and lenCell > limit:
                                                count = 0
                                                while len(cell[count:]) > limit:
                                                        findSpace = cell.rfind(" ", count, count+(limit-1))
                                                        if findSpace != -1:
                                                                cell = cell[0:findSpace] + "\n" + cell[findSpace+1:]
                                                                count = findSpace + 1
                                                        else:
                                                                cell = cell[0:count+(limit-1)] + "\n" + cell[count+(limit-1):]
                                                                count = count + limit
                                                        heightOfRow += 20
                                                if heightOfRow > heightOfTheRow:
                                                        heightOfTheRow = heightOfRow
                                                heightOfRow = 20
                                        listCell.append(cell)
                                
                                style.configure('Treeview', rowheight=heightOfTheRow)
                                my_tree.insert(parent="", index="end", iid=rowNumber, text="", values=(listCell[0], listCell[1], listCell[2], listCell[3], listCell[4], listCell[5], listCell[6], listCell[7], listCell[8], listCell[9], listCell[10], listCell[11]))
                                rowNumber += 1

        except mysql.connector.Error as errorMessage:
                messagebox.showinfo("Error", errorMessage)
        finally:
                databaseCursor.close()
                database.close()

#Used for displaying multiple lines
style = ttk.Style(root)

#Search Button
ButtonSearch = Button(root, text="Search", borderwidth=0,highlightthickness=0,bd=0,command=selectFromActiveRecords)
my_canvas.create_window(1770,290,anchor="nw",window=ButtonSearch)


root.mainloop()
