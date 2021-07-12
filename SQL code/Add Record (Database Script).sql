DELIMITER //

CREATE PROCEDURE InsertNewRecord (
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

#Procedure to insert one record.
#Return "Record successfully added" if the insertion was successful, return error message if the insertion was not successful.

BEGIN

#Check whether the applicant already exists or not
IF (SELECT EXISTS
     (SELECT applicantICNumber
       FROM Applicant
       WHERE applicantICNumber = dataApplicantICNumber) = 1)
THEN
  SET message = "The applicant already exists.";

#Insert the record
ELSE
INSERT INTO Applicant (
applicantICNumber,
applicantName,
applicantEmail,
applicantContactNumber,
applicantLanguageWritten,
applicantLanguageSpoken,
applicantProgrammingLanguage,
applicantPastWorkExperience,
applicantPastWorkDuration,
applicantHighestEducation,
applicantSoftSkill
)
VALUES (
dataApplicantICNumber,
dataApplicantName,
dataApplicantEmail,
dataApplicantContactNumber,
dataApplicantLanguageWritten,
dataApplicantLanguageSpoken,
dataApplicantProgrammingLanguage,
dataApplicantPastWorkExperience,
dataApplicantPastWorkDuration,
dataApplicantHighestEducation,
dataApplicantSoftSkill
);

INSERT INTO Application (
positionApplied,
applicantID)
VALUES (
dataApplicationPositionApplied,
(SELECT applicantID
   FROM Applicant
   WHERE applicantICNumber = dataApplicantICNumber));

#Check whether the insertion was susccessful or not
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
  SET message = "Record successfully added";
  
ELSE 
  SET message = "Something wrong when inserting the record into the database.";
END IF;
END IF;

END //

DELIMITER ;
