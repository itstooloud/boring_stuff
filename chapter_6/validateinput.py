#validate user input

while True:
    print('Enter your age: ')
    age = input()
    if age.isdecimal():
        break
    print('Please enter a number for your age.')
    
while True:
    print('Select a new password (letters and numbers only):')
    password = input()
    if password.isalnum():
        break
    print('Your password must contain letters and numbers.')
    
