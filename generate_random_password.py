from random import randrange
import sys

def main():
    length = int(sys.argv[1])
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*-_+=/?.'
    password = ''
    for i in range(length):
        password += string[randrange(80)]
    print(password)
if __name__ == '__main__':
    main()
