#This file contains the dummy data in the database

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'940102071234', 'Aminah binti Yusof', 'aminahyusof@gmail.com', '01122223333', 'English, Malay', 'English, Malay, Indonesian, Dialect Jawa', 'Python, Java, C++, PHP, Perl, Ruby', 'Programmer (ABC Software Design Sdn. Bhd.), 2016-2021', '6 years', 'Degree of Software Engineering, XYZ College, Penang (2016)', 'Energetic, active, optimistic, leadership, teamwork, flexibility, effective communication');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Software engineer', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '940102071234'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'000203072345', 'Candra a/l Subramaniam', 'candrasubramaniam@yahoo.com', '0123333444', 'English, Malay, Tamil', 'English, Malay, Tamil, Indonesian', 'Python, Oracle, C#', 'Fresh graduate', 'Fresh graduate', 'Degree of Software Design, WXY College, Penang (2021)', 'Teamwork, adaptability, optimistic, active');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Software engineer', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '000203072345'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'970304073456', 'Lim Lip Eng', 'lipenglim@gmail.com', '0134444555', 'English, Malay, Chinese', 'English, Malay, Chinese, Indonesian, Dialect Hokkien', 'Java Script, C#, C++', 'Software designer (BCD Industrial Sdn. Bhd.), 2019-2021', '3 years', 'Degree of Software Analysis, VWX College, Penang (2019)', 'Adaptability, energetic, able to work for long hours, teamwork, flexibility');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Software engineer', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '970304073456'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'020405074567', 'Lee Chun Meng', 'chunmenglee@yahoo.com', '0145555666', 'English, Malay, Chinese', 'English, Malay, Indonesian, Chinese', '', 'Fresh graduate', 'Fresh graduate', 'Diploma of Accounting, UVW College, Penang (2021)', 'Flexibility, optimistic');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Accountant', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '020405074567'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'970506075678', 'Nazliza binti Samad', 'nazlinasamad@yahoo.com', '01566667777', 'English, Malay', 'English, Malay, Indonesian, Japanese, Dialect Jawa', '', 'Accountant (CDE Enterprise Sdn. Bhd.), 2017-2021', '5 years', 'Degree of Finance, TUV College, Penang (2020)', 'Leadership, problem solving, conflict resolution, willing to learn new things, dependability');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Accountant', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '970506075678'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'940607076789', 'Murugan a/l Gopal', 'murugangopal@gmail.com', '0167777888', 'English, Malay, Tamil', 'English, Malay, Indonesian, Tamil, Korean', '', 'Accountant (DEF Trading Sdn. Bhd.), 2014-1021', '8 years', 'Diploma of Economics, STU College, Penang (2014)', 'Effective communication, friendly, optimistic, adaptability, flexibility');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Accountant', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '940607076789'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'950708077890', 'Sangkita a/p Ravi', 'sangkitaravi@yahoo.com', '0178888999', 'English, Malay, Tamil, Chinese', 'English, Malay, Tamil, Indonesian, Chinese, Dialect Hokkien', '', 'Technician (EFG Manufacturing Sdn. Bhd.), 2015-2021', '7 years', 'Diploma of Biotechnology, RST College, Penang (2015)', 'Positive attitude, teamwork, adaptability, critical thinking, empathy, mutual respect');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Technician', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '950708077890'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'980809078901', 'Soo Seng Poh', 'sengpohsoo@gmail.com', '0189999000', 'English, Malay, Chinese', 'English, Malay, Chinese, Indonesian, Dialect Hokkien', '', 'Technician (FGH Industrial Sdn. Bhd.), 2018-2021', '4 years', 'Diploma of Electrical Engineering, QRS College, Penang (2018)', 'Leadership, active listening, good communication, time management, decisiveness');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Technician', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '980809078901'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'020910079012', 'Suhana binti Abu Bakar', 'suhanaabubakar@yahoo.com', '046467777', 'English, Malay', 'English, Malay, Dialect Jawa, Indonesian', '', 'Fresh graduate', 'Fresh graduate', 'Diploma of Electronics, PQR College, Penang', 'Negotiation, teamwork, critical thinking, problem solving');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Technician', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '020910079012'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'971011070123', 'Farid bin Leman', 'faridleman@gmail.com', '0101111222', 'English, Malay, Thai', 'English, Malay, Indonesian, Thai, Dialect Jawa', 'Java, Oracle', 'Data analyst (GHI Solutions Sdn. Bhd.), 2019-2021', '3 years', 'Degree of Data Analysis, OPQ college, Penang (2019)', 'Teamwork, optimistic, problem solving, active, friendly');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Data analyst', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '971011070123'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'991112073210', 'Goh Lay Ching', 'laychinggoh@yahoo.com', '01133334444', 'English, Malay, Chinese', 'English, Malay, Japanese, Chinese, Dialect Hokkien, Indonesian', 'Java, Python, C#, Ruby', 'Data analyst (HIJ Enterprise Sdn. Bhd.), 2020-2021', '1 year', 'Degree of Data Analysis, NOP College, Penang (2020)', 'Energetic, active listening, positive attitude, flexibility, adaptability, time management, able to work under strict deadlines');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Data analyst', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '991112073210'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'001213074321', 'Suntheren a/l Raju', 'suntherenraju@gmail.com', '0124444555', 'English, Malay, Tamil', 'English, Malay, Tamil, Indonesian', 'Oracle, C++, Java', 'Fresh graduate', 'Fresh graduate', 'Degree of Data Analysis, MNO College, Penang (2021)', 'Active listening, critical thinking, friendly, able to work for long hours, energetic');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Data analyst', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '001213074321'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'001231071111', 'Sim Chun Teik', 'chunteiksim@gmail.com', '0161616666', 'English, Malay, Chinese', 'English, Malay, Chinese, Indonesian, Dialect Hokkien', 'Python, Java', 'Programmer (SCT Software Development Sdn. Bhd.), 1/1/2020-20/6/2021', '1 year 5 months 20 days', 'Diploma of Programming, TCS College, Penang (2020)', 'Teamwork,active, conflict resolution, friendly');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Software Engineer', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '001231071111'));

INSERT INTO Applicant (
applicantICNumber, applicantName, applicantEmail, applicantContactNumber, applicantLanguageWritten, applicantLanguageSpoken, applicantProgrammingLanguage, applicantPastWorkExperience, applicantPastWorkDuration, applicantHighestEducation, applicantSoftSkill)
VALUES (
'011231073333', 'Stephen Ooi Boon Keat', 'stephenboonkeatooi@gmail.com', '0171717777', 'English, Malay, Chinese', 'English, Malay, Chinese, Indonesian, Dialect Hokkien', '', 'Fresh graduate', 'Fresh graduate', 'Diploma of Accounting, OBK College, Penang (2021)', 'Teamwork, energetic, friendly, decisive');
INSERT INTO Application (
positionApplied, applicantID)
VALUES (
'Accountant', (SELECT applicantID FROM Applicant WHERE applicantICNumber = '011231073333'));
