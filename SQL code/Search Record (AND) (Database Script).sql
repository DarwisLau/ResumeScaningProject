DELIMITER //

CREATE PROCEDURE SelectFromActiveRecords_AND (
IN dataApplicantName varchar(152),
IN dataApplicantICNumber varchar(14),
IN dataApplicationPositionApplied varchar(52),
IN dataApplicantLanguageWritten_1 varchar(102),
IN dataApplicantLanguageWritten_2 varchar(102),
IN dataapplicantLanguageWritten_3 varchar(102),
IN dataApplicantLanguageSpoken_1 varchar(102),
IN dataApplicantLanguageSpoken_2 varchar(102),
IN dataApplicantLanguageSpoken_3 varchar(102),
IN dataApplicantProgrammingLanguage_1 varchar(102),
IN dataApplicantProgrammingLanguage_2 varchar(102),
IN dataApplicantProgrammingLanguage_3 varchar(102),
IN dataApplicantPastWorkExperience varchar(502),
IN dataApplicantHighestEducation varchar(102),
IN dataApplicantSoftSkill_1 varchar(102),
IN dataApplicantSoftSkill_2 varchar(102),
IN dataApplicantSoftSkill_3 varchar(102),
IN dataApplicantSoftSkill_4 varchar(102),
IN dataApplicantSoftSkill_5 varchar(102)
)

#Procedure to select information of active applicants who fulfill the criteria specified using the AND logic.
#Return information of all column, of the active applicants, who fulfill all the criteria, if one or more criteria is listed; return information of all column, of all active applicants, if no criterion is listed.
#The minimum number of criterion is zero; the maximum number of criteria for position applied, applicant's name, IC number, past work experience, and highest education are one each, whereas the maximum number of criteria for applicant's language (written), language (spoken), and programming language are 3 each, while the maximum number of criteria for applicant's soft skill is 5.

BEGIN

#Select information of the active applicants who fulfill the criteria
SELECT a.applicantName,
  a.applicantEmail,
  a.applicantICNumber,
  a.applicantContactNumber,
  n.positionApplied,
  a.applicantLanguageWritten,
  a.applicantLanguageSpoken,
  a.applicantProgrammingLanguage,
  a.applicantPastWorkExperience,
  a.applicantPastWorkDuration,
  a.applicantHighestEducation,
  a.applicantSoftSkill
  FROM Applicant a, Application n
  WHERE a.applicantID = n.applicantID AND
	n.isActive = 1 AND
	a.applicantName LIKE dataApplicantName AND
    a.applicantICNumber LIKE dataApplicantICNumber AND
	n.positionApplied LIKE dataApplicationPositionApplied AND
	a.applicantLanguageWritten LIKE dataApplicantLanguageWritten_1 AND
    a.applicantLanguageWritten LIKE dataApplicantLanguageWritten_2 AND
    a.applicantLanguageWritten LIKE dataApplicantLanguageWritten_3 AND
	a.applicantLanguageSpoken LIKE dataApplicantLanguageSpoken_1 AND
    a.applicantLanguageSpoken LIKE dataApplicantLanguageSpoken_2 AND
    a.applicantLanguageSpoken LIKE dataApplicantLanguageSpoken_3 AND
	a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_1 AND
	a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_2 AND
    a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_3 AND
    a.applicantPastWorkExperience LIKE dataApplicantPastWorkExperience AND
	a.applicantHighestEducation LIKE dataApplicantHighestEducation AND
	a.applicantSoftSkill LIKE dataApplicantSoftSkill_1 AND
    a.applicantSoftSkill LIKE dataApplicantSoftSkill_2 AND
    a.applicantSoftSkill LIKE dataApplicantSoftSkill_3 AND
    a.applicantSoftSkill LIKE dataApplicantSoftSkill_4 AND
    a.applicantSoftSkill LIKE dataApplicantSoftSkill_5;

END //

DELIMITER ;