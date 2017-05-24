##animals =  ['cat', 'bat', 'rat', 'elephant', 'shark']
##
##i = 0
##
##while i < len(animals):
##    print(animals[i])
##    i = i + 1


#####################

## this does the same thing
##character_count = 0
##for i in range(len(animals)):
##    print(animals[i])
##    character_count = character_count + len(animals[i])
##    print(character_count)
##
##print('Total characters: ' + str(character_count))

######################

## nested lists

##a = [['cat','hat'],[10,20,30,40,50]]
##print(a[0][1])

#SLICES

spam = ['cat', 'bat', 'rat', 'elephant', 'shark']
#print(spam[0:2])

print(spam[3:])
print(spam[:])
print(spam[0:-1])
spam[2] = 'fish'

print(spam[3:])
print(spam[:])
print(spam[0:-1])
print(spam)
del spam[2]
print(spam)


