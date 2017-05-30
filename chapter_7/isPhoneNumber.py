
#! Python 3

# extremely verbose way to check if the input fits the pattern of a phone number

def isPhoneNumber(text):
    
    if len(text) < 12:
        return False
    
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    
    if text[3] != '-':
        return False
        
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
            
    if text[7] != '-':
        return False
        
    for i in range(8,12):
        if not text[i].isdecimal():
            return False
            
    return True #return True if all the above conditions are not met. Execution stops w False
    
     

print('555-123-1545 is a phone number:')

print(isPhoneNumber('555-123-1545'))

print('Moshi moshi is a phone number:')
print(isPhoneNumber('moshimoshi'))


# function to find phone numbers inside a longer string

message = 'Call me at 156-345-3435 tomorrow. 454-656-3234 is my office.'

print(message)

for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
    
print('Done')



