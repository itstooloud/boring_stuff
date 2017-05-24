##
####def spam():
####    global eggs
####    eggs = 'spam'
####
####eggs = 'global'
####spam()
####print(eggs)
##
####using the word global inside the def means that when you refer to that variable within
####the function, you are referring to the global variable and can change it.
##
####def spam():
####    global eggs
####    eggs = 'spam' #this is a the global
####
####def bacon():
####    eggs = 'bacon' #this is a local variable
####
####def ham():
####    print(eggs) #this is the global
####
####eggs = 42 #this is the global
####spam()
####print(eggs)
##
#### if you try to use a global variable inside a function without assigning a value to it, you'll get an error
##
##def spam():
##    print(eggs) #this will give an error
## ##   eggs = 'spam local'
##
##eggs = 'global'
##
##spam()
##
#### it only throws the error because the function assigns a value to eggs. Commenting it out should remove the error
