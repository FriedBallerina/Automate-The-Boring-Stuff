import re

declineMessage = 'Please make sure the password is strong. '
acceptMessage = 'Your password is saved. You may log in now.'
passwordRegexHasLowercase = re.compile(r'[a-z]')
passwordRegexHasUppercase = re.compile(r'[A-Z]')
passwordRegexHasDigit = re.compile(r'\d')

def passwordStrengthDetector():
    while True:
        userPassword = input('Please type in your password. The password needs to be strong, i.e. at least eight characters long, contain both uppercase and lowercase characters, and have at least one digit')
        if len(userPassword) < 8:
            print(declineMessage)
        else:
            if bool(passwordRegexHasDigit.search(userPassword)) == False:
                continue
            elif bool(passwordRegexHasUppercase.search(userPassword)) == False:
                continue
            elif bool(passwordRegexHasLowercase.search(userPassword)) == False:
                continue
            else:
                print(acceptMessage)
                break
passwordStrengthDetector()