#print out a grid. Lesson in using nested lists

grid = [['.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.'],
        ['.','.','.','.','.','.','.','.','.'],
        ['X','.','.','.','.','.','.','.','.']]

print(grid)

for x in range(6):
    for y in range(8):
            print(grid[x][y],end='')

    print('') #prints a new line
    
            
        
    
    
