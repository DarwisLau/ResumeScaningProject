DELIMITER //

CREATE PROCEDURE SelectOneFromActiveRecords (
IN dataApplicantICNumber char(12),
OUT dataApplicantName varchar(200),
OUT dataApplicantEmail varchar(150),
OUT dataApplicantContactNumber varchar(11),
OUT dataPositionApplied varchar(200),
OUT dataApplicantLanguageWritten varchar(500),
OUT dataApplicantLanguageSpoken varchar(500),
OUT dataApplicantProgrammingLanguage varchar(500),
OUT dataApplicantPastWorkExperience varchar(3000),
OUT dataApplicantPastWorkDuration varchar(300),
OUT dataApplicantHighestEducation varchar(800),
OUT dataApplicantSoftSkills varchar(1500)
)

BEGIN

SET dataApplicantName = (
  SELECT a.applicantName
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantEmail = (
  SELECT a.applicantEmail
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantContactNumber = (
  SELECT a.applicantContactNumber
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataPositionApplied = (
  SELECT n.positionApplied
    FROM Application n, Applicant a
    WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantLanguageWritten = (
  SELECT a.applicantLanguageWritten
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantLanguageSpoken = (
  SELECT a.applicantLanguageSpoken
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantProgrammingLanguage = (
  SELECT a.applicantProgrammingLanguage
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantPastWorkExperience = (
  SELECT a.applicantPastWorkExperience
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantPastWorkDuration = (
  SELECT a.applicantPastWorkDuration
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantHighestEducation = (
  SELECT a.applicantHighestEducation
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

SET dataApplicantSoftSkills = (
  SELECT a.applicantSoftSkills
    FROM Applicant a, Application n
	WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1 AND
      a.applicantID = n.applicantID);

END //


CREATE PROCEDURE UpdateRecord (
IN dataApplicantName varchar(200),
IN dataApplicantEmail varchar(150),
IN dataApplicantContactNumber varchar(11),
IN dataApplicantLanguageWritten varchar(500),
IN dataApplicantLanguageSpoken varchar(500),
IN dataApplicantProgrammingLanguage varchar(500),
IN dataApplicantPastWorkExperience varchar(3000),
IN dataApplicantPastWorkDuration varchar(300),
IN dataApplicantHighestEducation varchar(800),
#IN dataApplicantSoftSkills varchar(1500),
IN dataApplicantICNumber char(12),
IN dataApplicationPositionApplied varchar(200),
OUT message varchar(50)
)

#Procedure to update one record.
#Return "Record successfully edited" if the update was successful, error message if the update was not successful.

BEGIN

#Check whether an applicant with this IC number exists in the database or not
DECLARE existOrNotExist_ICNumber bit(1);

SET existOrNotExist_ICNumber = (SELECT EXISTS 
                        (SELECT applicantICNumber
                           FROM Applicant 
                           WHERE applicantICNumber = dataApplicantICNumber));

IF (existOrNotExist_ICNumber = 0) THEN
  SET message = "This IC number does not exist in the database.";

ELSE
#Update the record in the database
UPDATE Applicant
  SET applicantName = dataApplicantName,
    applicantEmail = dataApplicantEmail,
    applicantContactNumber = dataApplicantContactNumber,
    applicantLanguageWritten = dataApplicantLanguageWritten,
    applicantLanguageSpoken = dataApplicantLanguageSpoken,
    applicantProgrammingLanguage = dataApplicantProgrammingLanguage,
    applicantPastWorkExperience = dataApplicantPastWorkExperience,
    applicantPastWorkDuration = dataApplicantPastWorkDuration,
    applicantHighestEducation = dataApplicantHighestEducation
    #applicantSoftSkills = dataApplicantSoftSkills
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
  #((SELECT applicantSoftSkills FROM Applicant WHERE applicantICNumber = dataICNumber) = dataApplicantSoftSkills) AND
  ((SELECT positionApplied FROM Application WHERE applicantID = (SELECT applicantID FROM Applicant WHERE applicantICNumber = dataApplicantICNumber)) = dataApplicationPositionApplied)
THEN
  SET message = "Record successfully edited";
  
ELSE 
  SET message = "Something wrong when updating the record in the database.";
END IF;
END IF;

END //

DELIMITER ;