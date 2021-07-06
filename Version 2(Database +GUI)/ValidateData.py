"""This file contains code for data validation."""



def standardise_applicantICNumber (ICNumber):

    """Function to standardise applicants' IC numbers, because each applicant's
       IC number has to be unique.
       Input should be string.
       Output is string."""


    #Remove space, "-"
    ICNumber = ICNumber.replace(" ", "")
    ICNumber = ICNumber.replace("-", "")

    return ICNumber



def validate_applicantICNumber (ICNumber):

    """Function to check if an applicant's IC number is valid and return error
       message if the applicant's IC number is not valid.
       Input should be string.
       Output is string or no output.
       Note: applicantICNumber char(12) UNIQUE NOT NULL
       Valid format: YYMMDDPB###G, YYMMDD-PB-###G"""


    #Number of characters
    if len(ICNumber) == 0:
        return "Applicant's IC number must be filled."

    #Syntax
    elif len(ICNumber) == 12 and ICNumber.isdigit() == True:
        #YYMMDD
        import datetime
        try:
            datetime.datetime.strptime(ICNumber[0:6], "%y%m%d")
        except ValueError:
            return "The applicant's IC number is not valid (digit 1-6)."
        #PB
        list_placeOfBirth = ['01', '02' '03', '04', '05', '06', '07', '08', '09', '10', '11', '12', '13', '14', '15', '16', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64', '65', '66', '67', '68', '71', '72', '74', '75', '76', '77', '78', '79', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91', '92', '93', '98', '99']
        if ICNumber[6:8] not in list_placeOfBirth:
            return "The applicant's IC number is not valid (digit 7-8)."
    else:
        return "The applicant's IC number is not in the correct format (should be YYMMDDPB###G or YYMMDD-PB-###G)."



def validate_applicantName (name):

    """Function to check if an applicant's name is valid and return error
       message if the applicant's name is not valid.
       Input should be string.
       Output is string or no output.
       Note: applicantName varchar(200) NOT NULL"""


    #Number of characters
    if len(name) > 200:
        return "The character limit for applicant's name is 200."
    elif len(name) == 0:
        return "Applicant's name must be filled."



def standardise_applicantEmail (email):

    """Function to standardise applicants's email addresses, because each
       applicant's email address has to be unique.
       Input should be string.
       Output is string."""


    #Remove space (front and back)
    email = email.strip()

    return email



def validate_applicantEmail (email):

    """Function to check if an applicant's email address is valid and return
       error message if the applicant's email address is not valid.
       Input should be string.
       Output is string or no output.
       Note: applicantEmail varchar(150) UNIQUE NOT NULL"""


    #Number of characters
    if len(email) > 150:
        return "The character limit for applicant's email address is 150."
    elif len(email) == 0:
        return "Applicant's email address must be filled."

    #Syntax
    else:
        from validate_email import validate_email
        #Validate_email is a package for Python that check if an email is valid, properly formatted and really exists.
        #It is used to check the syntax of the applicant's email address.
        #Source: https://pypi.org/project/validate_email/
        if validate_email(email) == False:
            return "The syntax of the applicant's email address is not correct."



def standardise_applicantContactNumber (contactNumber):

    """Function to standardise applicants' contact numbers, because each
       applicant's contact number has to be unique.
       Input should be string.
       Output is string."""

    
    #Remove "+", "(", ")", "-", space, country code
    contactNumber = contactNumber.replace(" ", "")
    contactNumber = contactNumber.replace("-", "")
    contactNumber = contactNumber.replace("+", "")
    contactNumber = contactNumber.replace("(", "")
    contactNumber = contactNumber.replace(")", "")
    if contactNumber[0:1] == "6":
        contactNumber = contactNumber.replace("6", "")

    return contactNumber



def validate_applicantContactNumber (contactNumber):
    
    """Function to check if an applicant's contact number is valid and return
       error message if the applicant's contact number is not valid..
       Input should be string.
       Output is string or no output.
       Note: applicantContactNumber varchar(11) UNIQUE NOT NULL"""


    #Number of characters
    if len(contactNumber) == 0:
        return "Applicant's contact number must be filled."

    else:
        #Remove symbol, space, country code
        contactNumber = contactNumber.replace(" ", "")
        contactNumber = contactNumber.replace("-", "")
        contactNumber = contactNumber.replace("+", "")
        contactNumber = contactNumber.replace("(", "")
        contactNumber = contactNumber.replace(")", "")
        if contactNumber[0:1] == "6":
            contactNumber = contactNumber.replace("6", "")

        #Syntax
        list_mobilePrefix = ['012', '013', '014', '016', '017', '018', '019']
        list_landlinePrefix = ['04', '05', '06', '07', '082', '083', '084', '085', '086', '087', '088', '089', '09']
        if contactNumber[0:3] in ['011', '015'] and len(contactNumber) == 11:
            pass
        elif contactNumber[0:3] in list_mobilePrefix and len(contactNumber) == 10:
            pass
        elif contactNumber[0:2] == '03' and len(contactNumber) ==  10:
            pass
        elif contactNumber[0:2] in list_landlinePrefix and len(contactNumber) == 9:
            pass
        elif contactNumber[0:3] in list_landlinePrefix and len(contactNumber) == 9:
            pass
        else:
            return "The applicant's contact number is not valid."       

        

def validate_positionApplied (positionApplied):

    """Function to check if an position applied is valid and return error
       message if the applicant's position applied is not valid.
       Input should be string.
       Output is string or no output.
       Note: positionApplied varchar(200) NOT NULL"""


    #Number of characters
    if len(positionApplied) > 200:
        return "The character limit for applicant's language (written) is 200."
    elif len(positionApplied) == 0:
        return "Position applied must be filled."



def validate_otherData (languageWritten, languageSpoken, programmingLanguage, pastWorkExperience, pastWorkDuration, highestEducation):

    """Function to check if an applicant's language(s) (written), language(s)
       (spoken), programming language(s), past work experience, past work
       duration, and highest education are valid and return error message if
       any of these data is not valid.
       All 6 inputs should be string.
       Output is string or no output.
       Note: applicantLanguageWritten varchar(500) NULL
             applicantLanguageSpoken varchar(500) NULL
             applicantProgrammingLanguage varchar(500) NULL
             appplicantPastWorkExperience varchar(3000) NULL
             applicantPastWorkDuration varchar(300) NULL
             applicantHighestEducation varchar(800) NULL
             applicantSoftSkills varchar(1500) NULL"""


    #Number of characters
    if len(languageWritten) > 500:
        return "The character limit for applicant's language (written) is 500."
    elif len(languageSpoken) > 500:
        return "The character limit for applicant's language (spoken) is 500."
    elif len(programmingLanguage) > 500:
        return "The character limit for applicant's programming language(s) is 500."
    elif len(pastWorkExperience) > 3000:
        return "The character limit for applicant's past work experience is 3000."
    elif len(pastWorkDuration) > 300:
        return "The character limit for applicant's past work duration is 300."
    elif len(highestEducation) > 800:
        return "The character limit for applicant's highest education is 800."
    #Soft slills

