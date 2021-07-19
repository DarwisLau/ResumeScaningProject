DELIMITER //

CREATE PROCEDURE SelectOneFromActiveRecords (
IN dataApplicantICNumber char(12)
)

#Procedure to select an active applicant's information.
#Return the applicant's information if the applicant exists and is active, do not return anything if the applicant does not exist or is not active.

BEGIN

SELECT a.applicantName,
  a.applicantEmail,
  a.applicantContactNumber,
  n.positionApplied,
  a.applicantLanguageWritten,
  a.applicantLanguageSpoken,
  a.applicantProgrammingLanguage,
  a.applicantPastWorkExperience,
  a.applicantPastWorkDuration,
  a.applicantHighestEducation,
  a.applicantSoftSkill
  FROM Applicant a
  INNER JOIN Application n
  ON a.applicantID = n.applicantID
    WHERE a.applicantICNumber = dataApplicantICNumber AND
      n.isActive = 1;

END //


CREATE PROCEDURE UpdateRecord (
IN dataApplicantICNumber char(12),
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
  SET message = "The applicant does not exist.";

#Check whether the applicant is active or not
ELSEIF ((SELECT n.isActive
         FROM Application n
         INNER JOIN Applicant a
         ON n.applicantID = a.applicantID
         WHERE a.applicantICNumber = dataApplicantICNumber) = 0)
THEN
  SET message = "The applicant is not active.";

#Update the record
ELSE
UPDATE Applicant a
INNER JOIN Application n
ON a.applicantID = n.applicantID
  SET a.applicantName = dataApplicantName,
    a.applicantEmail = dataApplicantEmail,
    a.applicantContactNumber = dataApplicantContactNumber,
    a.applicantLanguageWritten = dataApplicantLanguageWritten,
    a.applicantLanguageSpoken = dataApplicantLanguageSpoken,
    a.applicantProgrammingLanguage = dataApplicantProgrammingLanguage,
    a.applicantPastWorkExperience = dataApplicantPastWorkExperience,
    a.applicantPastWorkDuration = dataApplicantPastWorkDuration,
    a.applicantHighestEducation = dataApplicantHighestEducation,
    a.applicantSoftSkill = dataApplicantSoftSkill,
    n.positionApplied = dataApplicationPositionApplied
  WHERE a.applicantICNumber = dataApplicantICNumber;

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
  ((SELECT positionApplied FROM Application n INNER JOIN Applicant a ON n.applicantID = a.applicantID WHERE a.applicantICNumber = dataApplicantICNumber) = dataApplicationPositionApplied)
THEN
  SET message = "Record successfully edited";
ELSE 
  SET message = "Something wrong when updating the record in the database.";
END IF;
END IF;

END //

DELIMITER ;
