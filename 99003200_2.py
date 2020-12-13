import string
import random
import re


print("enter the option (for low=0, medium=1, strong=2,",
      "veiw pattern match=3): ")
option = int(input())
''' Enter option like for low level select 0,
for medium level select 1 and
 for high level select 2 '''


class password:
    # new super class 'password' is created

    def __init__(self):
        # created new constructor
        self.char1 = string.ascii_uppercase
        # contains upper case letters
        self.char2 = string.ascii_lowercase
        # contains lower case letters
        self.char3 = string.digits
        # contains digits
        self.char4 = string.punctuation
        # contains punctuations


class low(password):
    # new sub class 'low' is created in super class 'password'

    def low_level(self):
        # new function low_level is created
        out1 = self.char1+self.char2
        # adding both upper and lower case letters
        size = 0
        pass1 = ''
        length = int(input("enter the length of the password: "))
        # length of the password must be entered by user
        for x in range(size, length):
            pass1 += random.choice(out1)
        return pass1
        # random password is generated


class med(password):
    # new sub class 'med' is created in super class 'password'

    def med_level(self):
        # new function med_level is created
        out2 = self.char1+self.char2+self.char3
        # adding upper, lower case letters and digits
        size = 0
        pass2 = ''
        length = int(input("enter the length of the password: "))
        for x in range(size, length):
            pass2 += random.choice(out2)
        return pass2


class high(password):
    # new sub class 'high' is created in super class 'password'

    def high_level(self):
        # new function high_level is created
        out3 = self.char1+self.char2+self.char3+self.char4
        # adding lower and upper case letters, digits and punctuations
        size = 0
        pass3 = ''
        length = int(input("enter the length of the password: "))
        for x in range(size, length):
            pass3 += random.choice(out3)
        return pass3


def main():
    p1 = low()
    # object p1 is created using class 'low'
    p2 = med()
    # object p2 is created using class 'med'
    p3 = high()
    # object p3 is created using class 'high'
    if option == 0:
        # option 0 for low level password with lower and upper case letters
        print(p1.low_level())
        # print randomly generated password

    elif option == 1:
        '''option 1 for medium level password with lower, upper case letters
            and along with digits '''
        print(p2.med_level())

    elif option == 2:
        '''option 2 for high level password with lower, upper case letters,
            digits and puctuations '''
        print(p3.high_level())

    elif option == 3:
        print("\nPattern Matching for \'joseph@gmail.com' is:")
        print(re.match("[a-z]+@[a-z]+.[a-z]+", "joseph@gmail.com"))

    else:
        print("Invalid option! please choose correct option")
        # for invalid option entered

main()
