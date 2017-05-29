### write a function to display total inventory from a database of
### different players who may
##
##stuff = {'rope':1,'torch':12,'gold coin':2,'dagger':1,'arrow':13}
##
##
##
def displayInventory(inventory):
    counter = 0
    for k,v in inventory.items():
        print('key: ' + k + ', value: ' + str(v))
        counter = counter + v

    print('Total stuff: ' + str(counter))

##displayInventory(stuff)



def addtoInventory(inventory, addedItems):

    for i in addedItems:
        if i in inventory:
            inventory[i] = inventory[i] + 1
        else:
            inventory[i] = 1
            
    return inventory       
        


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin','dagger','gold coin','gold coin','ruby']

inv = addtoInventory(inv, dragonLoot)
displayInventory(inv)


    
