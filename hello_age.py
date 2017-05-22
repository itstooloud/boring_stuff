#if/elif will exit as soon as one condition is met

print('Hello! What is your name?')
my_name = input()
if my_name == "Chris":
    print('Hello Chris! Youre me!')

print('Your age?')
my_age = input()
my_age = int(my_age)
if my_age > 20:
    print("you're old")
elif my_age <= 10:
    print("you're young")
else:
    print('you are a spring chicken!')
    

