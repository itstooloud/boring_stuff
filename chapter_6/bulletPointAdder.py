# This program will take input from the clipboard and add a star and a space
# to the beginning of each line, i.e. turn it into a bullet point list

#! python3

import pyperclip
text = pyperclip.paste()

#TODO: separate list and add stars

lines = text.split('\n')
##print(lines)

for i in range(len(lines)):  #loop through all the indexes for the 'lines' list
    lines[i] = '* - ' + lines[i] #add the bullet point to the beginning of the line

text = '\n'.join(lines) # join them back together with the bullets

    
    
pyperclip.copy(text) #add this shit back to the clipboard

    