# Password validator (real signup feature):
# a password is valid if length ≥ 8, it has at least one digit, one uppercase letter and one lowercase letter. 
# Print "valid" or the first rule that fails. Hint: ch.isdigit(), ch.isupper(), ch.islower().

def validate_password(pwd: str) -> str:
    if len(pwd) < 8:
        return "Password must be at least 8 characters long"
    if not any(ch.isdigit() for ch in pwd):
        return "Password must contain at least 1 digit"
    if not any(ch.isupper() for ch in pwd):
        return "Password must contain at least 1 uppercase letter"
    if not any(ch.islower() for ch in pwd):
        return "Password must contain at least 1 lowercase letter"
    return "valid"

print(validate_password(input("Enter the password: ")))