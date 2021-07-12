DELIMITER //

CREATE PROCEDURE SelectOneFromAllRecords (
IN dataApplicantICNumber char(12),
OUT dataApplicantName varchar(200),
OUT dataApplicantEmail varchar(150),
OUT dataApplicantContactNumber varchar(11),
OUT dataApplicationPositionApplied varchar(200),
OUT dataApplicantLanguageWritten varchar(500),
OUT dataApplicantLanguageSpoken varchar(500),
OUT dataApplicantProgrammingLanguage varchar(500),
OUT dataApplicantPastWorkExperience varchar(3000),
OUT dataApplicantPastWorkDuration varchar(300),
OUT dataApplicantHighestEducation varchar(800),
OUT dataApplicantSoftSkill varchar(1500),
OUT dataApplicationIsActive bit(1)
)

#Procedure to select an applicanr's information.
#Return the applicant's information if the applicant exists, do not return anything if the applicant does not exist.

BEGIN

#Name
SET dataApplicantName = (
  SELECT applicantName
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Email address
SET dataApplicantEmail = (
  SELECT applicantEmail
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Contact number
SET dataApplicantContactNumber = (
  SELECT applicantContactNumber
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Position applied
SET dataApplicationPositionApplied = (
  SELECT n.positionApplied
    FROM Application n, Applicant a
    WHERE a.applicantICNumber = dataApplicantICNumber AND
          n.applicantID = a.applicantID);

#Language (written)
SET dataApplicantLanguageWritten = (
  SELECT applicantLanguageWritten
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#language (spoken)
SET dataApplicantLanguageSpoken = (
  SELECT applicantLanguageSpoken
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Programming language
SET dataApplicantProgrammingLanguage = (
  SELECT applicantProgrammingLanguage
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Past work experience
SET dataApplicantPastWorkExperience = (
  SELECT applicantPastWorkExperience
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Past work duration
SET dataApplicantPastWorkDuration = (
  SELECT applicantPastWorkDuration
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Highest education
SET dataApplicantHighestEducation = (
  SELECT applicantHighestEducation
    FROM Applicant
	WHERE applicantICNumber = dataApplicantICNumber);

#Soft skill
SET dataApplicantSoftSkill = (
  SELECT applicantSoftSkill
    FROM Applicant
    WHERE applicantICNumber = dataApplicantICNumber);

#Archive status
SET dataApplicationIsActive = (
  SELECT n.isActive
    FROM Application n, Applicant a
    WHERE a.applicantICNumber = dataApplicantICNumber AND
          n.applicantID = a.applicantID);

END //


CREATE PROCEDURE ChangeArchiveStatus (
IN dataApplicantICNumber char(12),
IN dataApplicationIsActive bit(1),
OUT message varchar(50)
)

#Procedure to change an applicant's archive status.
#Return "Record  status changed" if the change of archive status was successful, return error message if the change of archive status was not successful.

BEGIN

#Check whether the applicant exists or not
IF ((SELECT EXISTS
     (SELECT applicantICNumber
       FROM Applicant
       WHERE applicantICNumber = dataApplicantICNumber)) = 0)
THEN
  SET message = "The applicant already exists.";

#Change archive status
ELSE
UPDATE Application
  SET isActive = dataApplicationIsActive
  WHERE applicantID = (
   SELECT applicantID
     FROM Applicant
     WHERE applicantICNumber = dataApplicantICNumber);

#Check whether the change of archive status was successful or not
IF ((SELECT isActive FROM Application WHERE applicantID = (SELECT applicantID FROM Applicant WHERE applicantICNumber = dataapplicantICNumber)) = dataApplicationIsactive) THEN
SET message = "Record status changed";

ELSE
SET message = "Something wrong when changing archive status of the applicant in the database.";
END IF;
END IF;

END //

DELIMITER ;