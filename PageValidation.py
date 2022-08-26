while True:
    print('Enter your age:')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age:')

while True:
    print('Select a new password(letters and numbers only):')
    Password = input()
    if len(Password) < 10 :
        print('Invalid Password')
    elif Password.isalnum():
        print('You\'re good to go')
        break
    print('Passwords can only have letters and numbers')
