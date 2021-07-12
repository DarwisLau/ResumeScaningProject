DELIMITER //

CREATE PROCEDURE SelectOneFromActiveRecords (
IN dataApplicantICNumber char(12),
OUT dataApplicantName varchar(150),
OUT dataApplicantEmail varchar(150),
OUT dataApplicantContactNumber varchar(11),
OUT dataPositionApplied varchar(50),
OUT dataApplicantLanguageWritten varchar(100),
OUT dataApplicantLanguageSpoken varchar(100),
OUT dataApplicantProgrammingLanguage varchar(100),
OUT dataApplicantPastWorkExperience varchar(500),
OUT dataApplicantPastWorkDuration varchar(30),
OUT dataApplicantHighestEducation varchar(100),
OUT dataApplicantSoftSkill varchar(100)
)

#Procedure to select an active applicant's information.
#Return the applicant's information if the applicant exists and is active, do not return anything if the applicant does not exist or is not active.

BEGIN

#Name
SET dataApplicantName = (
  SELECT a.applicantName
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Email address
SET dataApplicantEmail = (
  SELECT a.applicantEmail
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Contact number
SET dataApplicantContactNumber = (
  SELECT a.applicantContactNumber
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Position applied
SET dataPositionApplied = (
  SELECT n.positionApplied
    FROM Application n, Applicant a
    WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Language (written)
SET dataApplicantLanguageWritten = (
  SELECT a.applicantLanguageWritten
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Language (spoken)
SET dataApplicantLanguageSpoken = (
  SELECT a.applicantLanguageSpoken
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Programming language
SET dataApplicantProgrammingLanguage = (
  SELECT a.applicantProgrammingLanguage
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Past work experience
SET dataApplicantPastWorkExperience = (
  SELECT a.applicantPastWorkExperience
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Past work duration
SET dataApplicantPastWorkDuration = (
  SELECT a.applicantPastWorkDuration
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Highest education
SET dataApplicantHighestEducation = (
  SELECT a.applicantHighestEducation
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

#Soft skill
SET dataApplicantSoftSkill = (
  SELECT a.applicantSoftSkill
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

END //


CREATE PROCEDURE UpdateRecord (
IN dataApplicantName varchar(150),
IN dataApplicantEmail varchar(150),
IN dataApplicantContactNumber varchar(11),
IN dataApplicantLanguageWritten varchar(100),
IN dataApplicantLanguageSpoken varchar(100),
IN dataApplicantProgrammingLanguage varchar(100),
IN dataApplicantPastWorkExperience varchar(500),
IN dataApplicantPastWorkDuration varchar(30),
IN dataApplicantHighestEducation varchar(100),
IN dataApplicantSoftSkill varchar(100),
IN dataApplicantICNumber char(12),
IN dataApplicationPositionApplied varchar(50),
OUT message varchar(50)
)

#Procedure to update one record.
#Return "Record successfully edited" if the update was successful, return error message if the update was not successful.

BEGIN

#Check whether the applicant exists or not
IF ((SELECT EXISTS 
     (SELECT applicantICNumber
       FROM Applicant
       WHERE applicantICNumber = dataApplicantICNumber)) = 0)
THEN
  SET message = "The applicant does not exists.";

#Check whether the applicant is active or not
ELSEIF ((SELECT n.isActive
         FROM Application n, Applicant a
         WHERE a.applicantICNumber = dataApplicantICNumber AND
           n.applicantID = a.applicantID) = 0)
THEN
  SET message = "The applicant is not active.";

#Update the record
ELSE
UPDATE Applicant
  SET applicantName = dataApplicantName,
    applicantEmail = dataApplicantEmail,
    applicantContactNumber = dataApplicantContactNumber,
    applicantLanguageWritten = dataApplicantLanguageWritten,
    applicantLanguageSpoken = dataApplicantLanguageSpoken,
    applicantProgrammingLanguage = dataApplicantProgrammingLanguage,
    applicantPastWorkExperience = dataApplicantPastWorkExperience,
    applicantPastWorkDuration = dataApplicantPastWorkDuration,
    applicantHighestEducation = dataApplicantHighestEducation,
    applicantSoftSkill = dataApplicantSoftSkill
  WHERE applicantICNumber = dataApplicantICNumber;

UPDATE Application
  SET positionApplied = dataApplicationPositionApplied
  WHERE applicantID = (
    SELECT applicantID 
    FROM Applicant
    WHERE applicantICNumber = dataApplicantICNumber);

#Check whether the update was successful or not
IF ((SELECT applicantName FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantName) AND
  ((SELECT applicantEmail FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantEmail) AND
  ((SELECT applicantContactNumber FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantContactNumber) AND
  ((SELECT applicantLanguageWritten FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantLanguageWritten) AND
  ((SELECT applicantLanguageSpoken FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantLanguageSpoken) AND
  ((SELECT applicantProgrammingLanguage FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantProgrammingLanguage) AND
  ((SELECT applicantPastWorkExperience FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantPastWorkExperience) AND
  ((SELECT applicantPastWorkDuration FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantPastWorkDuration) AND
  ((SELECT applicantHighestEducation FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantHighestEducation) AND
  ((SELECT applicantSoftSkill FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantSoftSkill) AND
  ((SELECT positionApplied FROM Application WHERE applicantID = (SELECT applicantID FROM Applicant WHERE applicantICNumber = dataApplicantICNumber)) = dataApplicationPositionApplied)
THEN
  SET message = "Record successfully edited";
  
ELSE 
  SET message = "Something wrong when updating the record in the database.";
END IF;
END IF;

END //

DELIMITER ;
