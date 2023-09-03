# Create a game to be solved

board = [[0,0,8,0,0,0,2,3,0],
         [0,0,0,5,0,4,0,0,0],
         [7,0,9,0,0,0,5,8,1],
         [0,0,0,0,5,0,0,0,0],
         [0,2,7,0,0,1,0,0,6],
         [0,0,0,0,6,2,0,0,0],
         [9,3,2,0,0,6,0,0,0],
         [0,0,6,0,0,8,3,0,0],
         [0,0,0,0,0,0,0,0,0]]

# Looping methods

for i in board:
    print(i)

print("New version")
    
for a in range(9):
    print("[",end="")
    for b in range(9):
        # This line prints without newline at end
        print(str(board[a][b]) + ", ",end="")
    print("]")


# Define which quadrant the slots belong to, defined as such:
#  A, B, C    =   0, 1, 2
#  D, E, F    =   3, 4, 5
#  G, H, I    =   6, 7, 8

for a in range(9):
    for b in range(9):
        row = int(a/3)*3
        col = int(b/3)
        print(row+col,end="")
    print()



# Create a 3 level list, potential numbers in each position
# Level 1: All positions can have 1 to 9

potentialNumbers = []

for a in range(9):
    level2List = []
    for b in range(9):
        level3List = []
        for c in range(9):
            level3List.append(c+1)
        level2List.append(level3List)
    potentialNumbers.append(level2List)
    
# Level 2: Remove all elements where we in our gamesetup have selected numbers
# Loop through board, if number is != 0, then the potential number is the actual number

for a in range(9):
    for b in range(9):
        currentValueBoard = board[a][b]
        if currentValueBoard != 0:
            potentialNumbers[a][b] = currentValueBoard

# Level 3: Remove numbers which are in the row

for i in potentialNumbers:
    for j in i:
        if type(j) == list:
            for k in i:
                if type(k) == int:
                    j.remove(k)

# Level 4: Remove numbers which are in columns
for b in range(9):
    columnList = []
    for a in range(9):
        currentValue = potentialNumbers[a][b]
        if type(currentValue) == int:
            columnList.append(currentValue)
    for a in range(9):
        currentValue = potentialNumbers[a][b]
        if type(currentValue) == list:
            potentialNumbers[a][b] = [i for i in currentValue if i not in columnList]


# Level 5: Remove numbers which are in 3x3 square
miniBoard = [[[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9],8],
             [[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9],[1, 2, 3, 4, 5, 6, 7, 8, 9]],
             [7,[1, 2, 3, 4, 5, 6, 7, 8, 9],9]]

print("miniBoard")
print(miniBoard)

print("inside for loops")
for b in range(3):
    columnList = []
    for a in range(3):
        currentValue = miniBoard[a][b]
        if type(currentValue) == int:
            columnList.append(currentValue)
    for a in range(3):
        currentValue = miniBoard[a][b]
        if type(currentValue) == list:
            miniBoard[a][b] = [i for i in currentValue if i not in columnList]

print(miniBoard)



print("new testStuff")
list1 = [1,2,3,4,5,6,7]
list2 = [3,5,6]

removedList = [i for i in list1 if i not in list2]
print(removedList)
