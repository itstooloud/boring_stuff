


#! usr/bin/env python3
# shebang line so the program can be run from the command line and take variables

#pw.py and insecure password locker program

PASSWORDS = {'email':'F7min1BDDuvMJuxES5JHSDS877kdfdfd',
             'blog': '4545HHDSFksdhdfIEWhfh88',
             'luggage': '12345'}

# command line arguments are handled with sys.argv
# the first item is sys.argv is a string containing the program's filename
# and the second item is the first command line argument


import sys
import pyperclip

if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password.')
    sys.exit()

account = sys.argv[1] # first command line argument is the account name

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
    
else:
    print('There is no account named ' + account)
    
#print(PASSWORDS)

