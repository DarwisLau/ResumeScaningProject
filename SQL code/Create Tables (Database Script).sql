CREATE TABLE Applicant (
applicantID int NOT NULL AUTO_INCREMENT, 
applicantICNumber char(12) UNIQUE NOT NULL,
applicantName varchar(200) NOT NULL,
applicantEmail varchar(150) UNIQUE NOT NULL,
applicantContactNumber varchar(11) UNIQUE NOT NULL,
applicantLanguageWritten varchar(500) NULL,
applicantLanguageSpoken varchar(500) NULL,
applicantProgrammingLanguage varchar(500) NULL,
applicantHighestEducation varchar(800) NULL,
applicantPastWorkExperience varchar(3000) NULL,
applicantPastWorkDuration varchar(300) NULL,
applicantSoftSkills varchar(1500) NULL);

CREATE TABLE Application (
positionApplied varchar(200) NOT NULL,
isActive bit(1) NOT NULL DEFAULT 1,
applicantID int UNIQUE NOT NULL);


ALTER TABLE Applicant
ADD CONSTRAINT applicantID_pk PRIMARY KEY (applicantID);


ALTER TABLE Application
ADD CONSTRAINT fk_applicantID
  FOREIGN KEY (applicantID)
  REFERENCES Applicant(applicantID);
