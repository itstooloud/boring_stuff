##birthdays = {'Alice':'Apr 1','Bob':'Dec 12','Carol':'Mar 4'}
##
##while True:
##    print('Enter a name: (blank to quit)')
##    name = input()
##    if name == '':
##        break
##    if name in birthdays:
##        print(birthdays[name] + ' is the birthday of ' + name)
##    else:
##        print('I do not have birthday info for ' + name)
##        print('What is their birthday?')
##        bday = input()
##        birthdays[name] = bday
##        print('Birthday database updated.')
##        


##spam = {'color':'red','age':42}
##
##for v in spam.values():
##    print(v)
##
##for k in spam.keys():
##    print(k)
##
##for i in spam.items(): #items returns the key and value as a list
##    print(i)
##
##for k,v in spam.items():
##    print('key: ' + k +'. value: ' + str(v))
##
####checking whether a key or value exists in a dictionary
##
##spam = {'name':'Zophie','age':7}
##print(('name' in spam.keys())) # returns True

##picnicItems = {'apples':5,'cups':2}
##print('I am bringing ' + str(picnicItems.get('apples',0)) + ' apples.')
##print('I am bringing ' + str(picnicItems.get('eggs',0)) + ' eggs.')
##
## without the get method, this would return an error

##spam = {'name':'Pookie','age':5}
####if 'color' not in spam:
####    spam['color'] = 'black'
##spam.setdefault('color','black')
##
##for i in spam.items():
##    print(i)
##

import pprint #pretty print

message = 'It was a bright cold day in April, and the clocks were striking thirteen'
count = {}

for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count) #pprint seems to be just for dictionaries?

    
    
    
