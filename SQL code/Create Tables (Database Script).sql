CREATE TABLE Applicant (
applicantID int NOT NULL AUTO_INCREMENT, 
applicantICNumber char(12) UNIQUE NOT NULL,
applicantName varchar(150) NOT NULL,
applicantEmail varchar(150) UNIQUE NOT NULL,
applicantContactNumber varchar(11) UNIQUE NOT NULL,
applicantLanguageWritten varchar(100) NOT NULL,
applicantLanguageSpoken varchar(100) NOT NULL,
applicantProgrammingLanguage varchar(100) NULL,
applicantHighestEducation varchar(100) NOT NULL,
applicantPastWorkExperience varchar(500) NOT NULL,
applicantPastWorkDuration varchar(30) NOT NULL,
applicantSoftSkill varchar(100) NOT NULL);


CREATE TABLE Application (
positionApplied varchar(50) NOT NULL,
isActive bit(1) NOT NULL DEFAULT 1,
applicantID int UNIQUE NOT NULL);



ALTER TABLE Applicant
ADD CONSTRAINT applicantID_pk PRIMARY KEY (applicantID);


ALTER TABLE Application
ADD CONSTRAINT fk_applicantID
  FOREIGN KEY (applicantID)
  REFERENCES Applicant(applicantID);
