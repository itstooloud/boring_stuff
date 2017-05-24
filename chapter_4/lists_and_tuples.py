
# strings as lists
name = 'Zophie'
print(name[0])
for i in name:
    print('*** ' + i + ' ***')

print (name[2:])

eggs = [1,2,3]
eggs.append(4)
print(eggs)
del eggs[2]
print(eggs)

## delete is not a method, it's a statement. This is a peculiarity to me
## you append using eggs.append(4)
## but delete using del eggs[4]


##Tuples are like lists but they can't have their values modified. Tuples
## are indicated with () instead of []

fish = (1,2,'eat me')
print(fish)
## fish.append('suck my balls') this throws an error
print(fish)

## You MAY have a tuple with only one value, which is indicated with a trailing comma


my_list = ['eggs','cheese','bacon']
my_tuple = ('steve','burt','alex')

my_list_tupled = tuple(my_list)
my_tuple_listed = list(my_tuple)
print('my_list_tupled')
print(type(my_list_tupled))
print('my_tuple_listed')
print(type(my_tuple_listed))


    
