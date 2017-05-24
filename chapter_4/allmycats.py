##catNames = []
##
##while True:
##    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (or enter nothing to stop):')
##    name = input()
##    if name == '':
##        break
## #   catNames = catNames + [name] # this has to be in brackets to append it to the set
##    catNames.append(name) # this line and the one above it do the same thing
##
##print('The cat names are:')
##for steve in catNames:
##    print('  ' + steve)
##    
### different version of that
##
##i = 0
##while i < len(catNames):
##    print(' ' + catNames[i])
##    i = i + 1
##    
### yet another way to do the same thing
##
##for i in range(len(catNames)):
##    print('Cat number ' + str(i) + ' is ' + catNames[i])
##    
### The in operator
##
##if 'Alex' in catNames:
##    print('You have at least one cat called Alex')
##    
#### wow, this is interesting, the MULTIPLE ASSIGNMENT TRICK
##
##cat = ['fat','black','loud']
##size = cat[0]
##color = cat[1]
##disposition = cat[2]
##print('Long form value assignments:')
##print(size)
##print(color)
##print(disposition)
##
#### instead of doing that, you can do this:
##
##size, color, disposition = cat
##
##print('Short form value assignments:')
##print(size)
##print(color)
##print(disposition)
##
#### finding the index of a value in a list
##print('the index of BLACK is:')
##
##print (cat.index('black'))
##
##

spam = ['cat','dog','bat']
spam.insert(1,'fish')
print(spam)
spam.remove('fish')
print('removed fish')
print(spam)


#sorting lists

spam.sort()
print(spam)

spam.sort(reverse=True)
print('reverse sort: ' + str(spam))

# sorting with a key

spam = ['a','A','Z','z']
spam = spam.sort(key=str.lower)
print(spam)







