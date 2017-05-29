print('''Dear Alice,

Eve's cat has been arrested for catnapping, cat burglary and extortion.

Sincerely,
Bob''')

# multi-line comments can be enclosed in triple quotes


''' this is a multiline comment put here to demonstrate that
you can do this in python when you have a comment
that takes more than one line '''

spam = 'Hello World!'
print(spam[0])
print(spam[0:12])
print(spam[:5]) # up until the 5th character
print(spam[6:]) # from the 6th character to the end

fizz = spam[0:5]

print(fizz)
print('upper: ' + spam.upper())

print('lower: ' + spam.lower())

print(spam.isupper()) # variable upper case
print(spam.islower()) # variable lower case
print('    '.isspace()) # does it contain empty space




