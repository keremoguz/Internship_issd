def num_of_islands(grid):
    """
    finds the number of island by going through matrix by using DFS
    """
    visited_locations = set() # it prevents infinite traverse by storing the visited locations
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid,r,c,visited_locations):
                """
                if it is a new island increment the count by 1
                """
                count += 1
    return count
def explore(grid,r,c,visited_locations):
    """
    goes through all possible ways(up,down,right,left) from the current location 
    until reaches to the border or "0"(water)
    """
    border_check = 0 <= r <len(grid) and 0<= c< len(grid[0]) # if border is exceeded assign it to False otherwise True
    location = str(r) + "," + str(c) 
    if not border_check:
        """
        if border is exceeded exit the function
        """
        return False
    if grid[r][c] == '0':
        """
        if the location is water exit the function
        """
        return False
    if location in visited_locations:
        """
        prevents the infinite recursive calls
        """
        return False
    visited_locations.add(location)

    explore(grid,r,c-1,visited_locations) # goes through left 
    explore(grid,r,c+1,visited_locations) # goes through right
    explore(grid,r+1,c,visited_locations) # goes through down
    explore(grid,r-1,c,visited_locations) # goes through up

    return True




grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]
]
print(num_of_islands(grid))

grid2 = [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]
]
print(num_of_islands(grid2))
