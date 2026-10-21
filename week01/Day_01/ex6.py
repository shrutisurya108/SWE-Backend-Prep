# Password validator (real signup feature):
# a password is valid if length ≥ 8, it has at least one digit, one uppercase letter and one lowercase letter. 
# Print "valid" or the first rule that fails. Hint: ch.isdigit(), ch.isupper(), ch.islower().

def hasDigit(pwd):
    for ch in pwd:
        if ch.isdigit():
            return True
    return False

def hasUpper(pwd):
    for ch in pwd:
        if ch.isupper():
            return True
    return False

def hasLower(pwd):
    for ch in pwd:
        if ch.islower():
            return True
    return False

pwd = input("Enter the password: ")
if len(pwd) < 8:
    print("password should be atleast 8 characters long!")
    exit()
if  not hasDigit(pwd):
    print("password should have atleast 1 digit!")
    exit()
if not hasUpper(pwd):
    print("password must have atleast 1 uppercase character!")
    exit()
if not hasLower(pwd):
    print("password must have atleast 1 lowercase character!")
    exit()
print("Valid!")