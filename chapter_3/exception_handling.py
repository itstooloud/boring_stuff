##def spam(divideBy):
##    try:
##        return 42 / divideBy
##    except ZeroDivisionError:
##        print('Error! Invalid argument.')
##        
##print(spam(2))
##print(spam(12))
##print(spam(0))
##print(spam(1))


## exceptions can be handled with try and except statements
## it can also look like this:
##
##def spam(divideBy):
##    
##    return 42 / divideBy
##
##    try:        
##        print(spam(2))
##        print(spam(12))
##        print(spam(0))
##        print(spam(1))
##
##    except ZeroDivisionError:
##        print('Error! Invalid argument.')

## In this case it doesn't print out the print(spam(1)) because once
## it jumps to the except, it doesn't keep executing the try
