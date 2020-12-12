import string
# import string library function
import random
# import random module

option = int(input("enter the option (for weak=0, medium=1, strong=2): "))
''' Enter option like for low level select 0,
for medium level select 1 and
 for high level select 2 '''


class password:
    # new class password is created

    def randompassword():
        # new function randompassword() is created
        if option == 0:
            # option 0 for low level password with lower and upper case letters
            low = string.ascii_uppercase
            low += string.ascii_lowercase
            # adding lower and upper case letters using ascii function
            size = 0
            pass1 = ''
            length = int(input("enter the length of the password: "))
            # length of the password must be entered by user
            for x in range(size, length):
                pass1 += random.choice(low)
            return pass1

        elif option == 1:
            '''option 1 for medium level password with lower, upper case letters
            and along with digits '''
            med = string.ascii_uppercase
            med += string.ascii_lowercase
            med += string.digits
            ''' adding lower case, upper case letters and digits
            using digits function for adding digits '''
            size = 0
            pass2 = ''
            length = int(input("enter the password length: "))
            # length of the password must be entered by user
            for x in range(size, length):
                pass2 += random.choice(med)
            return pass2

        elif option == 2:
            '''option 2 for high level password with lower, upper case letters,
            digits and puctuations '''
            high = string.ascii_uppercase
            high += string.ascii_lowercase
            high += string.digits
            high += string.punctuation
            # adding punctuations using string.punctuation function
            size = 0
            pass3 = ''
            length = int(input("enter the password length: "))
            for x in range(size, length):
                pass3 += random.choice(high)
            return pass3

        else:
            print("Invalid option! please choose correct option")

    print(randompassword())
    # print the randomly generated password


def main():
    # defining main funtion
    p = password()
    # new object created using class password
    p.randompassword()
    # function call
