from config.mongodb import get_db
from user.userModel import generateCodeModel, sendmail, userPassword, checkMail

def generateCode(email):
    code = generateCodeModel(email)
    check = checkMail(email)

    if check == False:  
        return False
    else :  
        sendmail(email, code)
        return True
    

def loginService(email, password):
    result = userPassword(email, password)

    return result