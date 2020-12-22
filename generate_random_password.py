from random import randrange

def main():
    string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890~`!@#$%^&*-_+=/?.,'
    password = ''
    for i in range(16):
        password += string[randrange(80)]
    print(password)
if __name__ == '__main__':
    main()
