DELIMITER //

CREATE PROCEDURE SelectOneFromAllRecords (
IN dataApplicantICNumber char(12)
)

#Procedure to select an applicanr's information.
#Return the applicant's information if the applicant exists, do not return anything if the applicant does not exist.

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
  a.applicantSoftSkill,
  n.isActive
  FROM Applicant a
  INNER JOIN Application n
  ON a.applicantID = n.applicantID
    WHERE a.applicantICNumber = dataApplicantICNumber;

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
  SET message = "The applicant does not exist.";

#Change archive status
ELSE
UPDATE Application n
INNER JOIN Applicant a
ON n.applicantID = a.applicantID
  SET n.isActive = dataApplicationIsActive
  WHERE a.applicantICNumber = dataApplicantICNumber;

#Check whether the change of archive status was successful or not
IF ((SELECT isActive FROM Application n INNER JOIN Applicant a ON n.applicantID = a.applicantID WHERE applicantICNumber = dataapplicantICNumber) = dataApplicationIsActive) THEN
SET message = "Record status changed";
ELSE
SET message = "Something wrong when changing archive status of the applicant in the database.";
END IF;
END IF;

END //

DELIMITER ;
