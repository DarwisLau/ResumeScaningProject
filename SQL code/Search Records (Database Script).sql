DELIMITER //

CREATE PROCEDURE SelectFromActiveRecords (
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

#Procedure to select information of active applicants who fulfill one of the criteria.
#Return active applicants' information, for those who fulfill one of the criteria, if one or more criteria is listed; return all active applicants' information, if no criterion is listed.
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
  FROM Applicant a
  INNER JOIN Application n
  ON a.applicantID = n.applicantID
  WHERE
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
    a.applicantSoftSkill LIKE dataApplicantSoftSkill_5
UNION
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
  FROM Applicant a
  INNER JOIN Application n
  ON a.applicantID = n.applicantID 
  WHERE 
    n.isActive = 1 AND
    ((CASE
      WHEN dataApplicantName = "%%" THEN a.applicantName = NULL
      ELSE a.applicantName LIKE dataApplicantName
	END)
    OR
    (CASE
      WHEN dataApplicantICNumber = "%%" THEN a.applicantICNumber = NULL
      ELSE a.applicantICNumber LIKE dataApplicantICNumber
	END)
    OR(CASE
	  WHEN dataApplicantLanguageWritten_1 = "%%" THEN a.applicantLanguageWritten = NULL
	  ELSE a.applicantLanguageWritten LIKE dataApplicantLanguageWritten_1
	END)
    OR
    (CASE 
      WHEN dataApplicantLanguageWritten_2 = "%%" THEN a.applicantLanguageWritten = NULL
	  ELSE a.applicantLanguageWritten LIKE dataApplicantLanguagewritten_2
    END)
    OR
    (CASE
      WHEN dataApplicantLanguageWritten_3 = "%%" THEN a.applicantLanguageWritten = NULL
      ELSE a.applicantLanguageWritten LIKE dataApplicantLanguageWritten_3
	END)
    OR
    (CASE
      WHEN dataApplicantLanguageSpoken_1 = "%%" THEN a.applicantLanguageSpoken = NULL
      ELSE a.applicantLanguageSpoken LIKE dataApplicantLanguageSpoken_1
	END)
    OR
    (CASE
      WHEN dataApplicantLanguageSpoken_2 = "%%" THEN a.applicantLanguageSpoken = NULL
      ELSE a.applicantLanguageSpoken LIKE dataApplicantLanguageSpoken_2
	END)
    OR
    (CASE
      WHEN dataApplicantLanguageSpoken_3 = "%%" THEN a.applicantLanguageSpoken = NULL
      ELSE a.applicantLanguageSpoken LIKE dataApplicantLanguageSpoken_3
	END)
    OR
    (CASE
      WHEN dataApplicantProgrammingLanguage_1 != "%%" AND
        dataApplicantProgrammingLanguage_2 != "%%" AND
        dataApplicantProgrammingLanguage_3 != "%%"
          THEN a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_1 OR
            a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_2 OR
            a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_3
	  WHEN dataApplicantProgrammingLanguage_1 != "%%" AND
        dataApplicantProgrammingLanguage_2 != "%%"
          THEN a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_1 OR
            a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_2
	  WHEN dataApplicantProgrammingLanguage_1 != "%%"
        THEN a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_1
	  ELSE
        a.applicantProgrammingLanguage = NULL
	END)
    OR
    (CASE
      WHEN dataApplicantProgrammingLanguage_3 = "%%" THEN a.applicantProgrammingLanguage = NULL
      ELSE a.applicantProgrammingLanguage LIKE dataApplicantProgrammingLanguage_3
	END)
    OR
    (CASE
      WHEN dataApplicantPastWorkExperience = "%%" THEN a.applicantPastWorkExperience = NULL
      ELSE a.applicantPastWorkExperience LIKE dataApplicantPastWorkExperience
	END)
    OR
    (CASE
      WHEN dataApplicantHighestEducation = "%%" THEN a.applicantHighestEducation = NULL
      ELSE a.applicantHighestEducation LIKE dataApplicantHighestEducation
	END)
    OR
    (CASE
      WHEN dataApplicantSoftSkill_1 = "%%" THEN a.applicantSoftSkill = NULL
      ELSE a.applicantSoftSkill LIKE dataApplicantSoftSkill_1
	END)
    OR
    (CASE
      WHEN dataApplicantSoftSkill_2 = "%%" THEN a.applicantSoftSkill = NULL
      ELSE a.applicantSoftSkill LIKE dataApplicantSoftSkill_2
	END)
    OR
    (CASE
      WHEN dataApplicantSoftSkill_3 = "%%" THEN a.applicantSoftSkill = NULL
      ELSE a.applicantSoftSkill LIKE dataApplicantSoftSkill_3
	END)
    OR
    (CASE
      WHEN dataApplicantSoftSkill_4 = "%%" THEN a.applicantSoftSkill = NULL
      ELSE a.applicantSoftSkill LIKE dataApplicantSoftSkill_4
	END)
    OR
    (CASE
      WHEN dataApplicantSoftSkill_5 = "%%" THEN a.applicantSoftSkill = NULL
      ELSE a.applicantSoftSkill LIKE dataApplicantSoftSkill_5
	END));

END //

DELIMITER ;
