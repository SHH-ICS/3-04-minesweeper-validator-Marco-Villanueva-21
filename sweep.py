# Validate a minesweeper interior block
# block_data is a two dimensional array containing the data from a 3 x 3 grid of squares
# We are assuming that we are only checking interior blocks for now
# Return value should be a string that says either Valid or Invalid (with some hints as to why it's invlaid)

def validate( block_data ):
# Check whether the centre block is a bomb, a number, or an invalid input  
  bomb_count=0
  for i in range(0,3):
    for j in range(0,3):
      if i != 1 or j != 1:
        print (block_data[i][j],"at", i, j)
        if block_data [i][j] == -1:
          bomb_count=bomb_count+1  
          print(bomb_count)    
#  Skip bombs, send an error on invalid input, verify numbers
  if type(block_data [1][1]) == str:
    return "invalid input (letter)"
  elif block_data [1][1] == -1:
    return "invalid input (bomb)" 
  elif bomb_count != block_data [1][1]:
    return "invalid input (invalid number of bombs)"
  if bomb_count == block_data [1][1]:
    return "valid input"

def edge_validate(block_data): 

  #Loop for each row and column
  for r in range(0,3):
    for c in range(0,3):
      bomb_count2 = 0
        
      #Ignore numbers outside of the grid
      if r < 2:
        #Check surrounding numbers for bombs
        if block_data [r+1][c] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r+1, c)

      if r < 2 and c < 2:
        if block_data [r+1][c+1] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r+1, c+1)

      if c < 2:
        if block_data [r][c+1] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r, c+1)

      if r > 0 and c < 2:
        if block_data [r-1][c+1] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r-1, c+1)

      if r > 0:
        if block_data [r-1][c] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r-1, c)

      if r > 0 and c > 0:
        if block_data [r-1][c-1] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r-1, c-1)

      if c > 0:
        if block_data [r][c-1] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r, c-1)

      if r < 2 and c > 0:
        if block_data [r+1][c-1] == -1:
          bomb_count2=bomb_count2+1
          print("coordinates ", r, ",", c, " found a bomb at ", r+1, c-1)

      if block_data [r][c] != bomb_count2 and block_data [r][c] != -1:
        print ("the stated bomb count at", r, ",", c, "is", block_data[r][c], ". The number of bombs detected is", bomb_count2, ".")
        r = 10
        c = 10
        return "invalid input"
  return "valid input"

grid = [
  [1,2,2],
  [2,-1,-1],
  [2,-1,3]
]

print (edge_validate(grid))
