import string    
import random


def pwd_generator():
    S = int(input("Enter length of password: "))
    if S < 4:
        print("String length must be greater than 4")
        return
    
    passwd = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = S))
    print("The randomly generated password is: ",str(passwd))

pwd_generator()


# FOR PASSWORD VALIDATION
# if not any x.isdigit() for char in passwd:
#     print('Password should have at least one numeral')
        
# elif not anychar.isupper() for char in passwd:
#     print('Password should have at least one uppercase letter')
        
# elif not any(char.islower() for char in passwd):
#     print('Password should have at least one lowercase letter')
        
# elif not any(char in string.punctuation for char in passwd):
#     print('Password should have at least one symbols ')

