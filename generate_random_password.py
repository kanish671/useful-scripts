from random import randrange
import sys

def main():
    length = int(sys.argv[1])   # length of password
    option = int(sys.argv[2])   # option of password type
    # options - 1 - alphabetic lowercase, 2 - alphabetic mixed, 3 - alphanumeric, 4 - alphanumeric + special characters
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    numbers = '0123456789'
    specialcharacters = '~`!@#$%^&*-_+=/?.'
    password = ''
    for _ in range(length):
        string = lowercase
        if option == 2:
            string = string + uppercase
        if option == 3:
            string = string + uppercase + numbers
        if option == 4:
            string = string + uppercase + numbers + specialcharacters
        stringlength = len(string)
        password += string[randrange(stringlength)]
    print(password)

if __name__ == '__main__':
    main()
