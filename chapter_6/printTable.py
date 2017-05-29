#! Python3

# program takes a list of strings and displays it in a table with each column
# right-justified

tableData = [['apples','oranges','cherries','banana'],
            ['Alice','Bob','Caroline','David'],
            ['dogs','cats','moose','goose']]
            
print(tableData)

maximumWidth = [0] * len(tableData)
#this creates a list that looks like this: [0,0,0]

#Determine the longest string in the list so we know how big the margins have to be

print(len(tableData))

i = 0

while i < len(tableData):
    t = 0
    while t < len(tableData[i]):
        print('Word and length:')
        print(str(tableData[i][t]) + ' ' + str(len(tableData[i][t])))
        
        if len(tableData[i][t]) > maximumWidth[i]:
            maximumWidth[i] = len(tableData[i][t])
            print('MAX WIDTH: ' + str(maximumWidth[i]))
        #print(tableData[i][t])
        t += 1
    i +=1


for each in maximumWidth:
    print(each)
# so now maximumWidth[i] is the maximum width in each group

#now print out the table so that it's justified etc
## this part below is wrong, have to clean up the output

x = 0
while x < len(tableData):
    y = 0
    while y < len(tableData[x]):
        print('   ' + str(tableData[x][y]).rjust(maximumWidth[x] + 2, "-"))
        y +=1
    x+= 1


    


    

    
    
    
        
