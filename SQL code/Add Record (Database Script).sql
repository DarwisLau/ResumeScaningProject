DELIMITER //

CREATE PROCEDURE InsertNewRecord (
IN dataApplicantICNumber char(12),
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
IN dataApplicationPositionApplied varchar(200),
OUT message varchar(50)
)

#Procedure to insert one record.
#Return "Record successfully added" if the insertion was successful, error message if the insertion was not successful.

BEGIN

#Validate the unique keys
DECLARE existOrNotExist_ICNumber bit(1);
DECLARE existOrNotExist_email bit(1);
DECLARE existOrNotExist_contactNumber bit(1);

SET existOrNotExist_ICNumber = (SELECT EXISTS (
								  SELECT applicantICNumber
                                    FROM Applicant
                                    WHERE applicantICNumber = dataApplicantICNumber));

SET existOrNotExist_email = (SELECT EXISTS (
                               SELECT applicantEmail
                                 FROM Applicant
                                 WHERE applicantEmail = dataApplicantEmail));

SET existOrNotExist_contactNumber = (SELECT EXISTS (
									   SELECT applicantContactNumber
                                         FROM Applicant
                                         WHERE applicantContactNumber = dataApplicantContactNumber));

IF (existOrNotExist_ICNumber = 1) THEN
  SET message = "This IC number already exist in the database.";

ELSEIF (existOrNotExist_email = 1) THEN
  SET message = "This email address already exist in the database.";

ELSEIF (existOrNotExist_contactNumber = 1) THEN
  SET message = "This contact number already exist in the database.";

ELSE
#Insert the record into the database
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
applicantHighestEducation
#applicantSoftSkills
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
dataApplicantHighestEducation
#dataApplicantSoftSkills
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
  #((SELECT applicantSoftSkills FROM Applicant WHERE applicantICNumber = dataApplicantICNumber) = dataApplicantSoftSkills) AND
  ((SELECT positionApplied FROM Application WHERE applicantID = (SELECT applicantID FROM Applicant WHERE applicantICNumber = dataApplicantICNumber)) = dataApplicationPositionApplied)
THEN
  SET message = "Record successfully added";
  
ELSE 
  SET message = "Something wrong when inserting the record into the database.";
END IF;
END IF;

END //

DELIMITER ;