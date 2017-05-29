#pyperclip is installed via the command line with this command
# pip3 install pyperclip
#! usr/bin/env python3
# then to use it, it has to be imported

import pyperclip

pyperclip.copy('Hello world')

print(pyperclip.paste())
