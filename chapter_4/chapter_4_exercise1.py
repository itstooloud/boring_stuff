# end of chapter 4 exercises

# takes a list and outputs a string such that the last entry is preceded by 'and'

# i.e. 'apples, bananas, tofu, and cats'

spam = ['apples','bananas','tofu','cats']

def formalize_list(list):
    global message
    number = len(list)
    print(number)

    i = 0
    while i < (number - 1):
        message = message + list[i] + ', '
        print(message)
        i += 1
 
message = ''
formalize_list(spam)
i = len(spam) - 1
message = message + 'and ' + spam[i]
print(message)
