def num_of_islands(grid):
    visited_locations = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid,r,c,visited_locations):
                count += 1

    return count
def explore(grid,r,c,visited_locations):
    border_check = 0 <= r <len(grid) and 0<= c< len(grid[0])
    location = str(r) + "," + str(c)
    if not border_check:
        return False
    if grid[r][c] == '0':
        return False
    if location in visited_locations:
        return False
    visited_locations.add(location)

    explore(grid,r,c-1,visited_locations)
    explore(grid,r,c+1,visited_locations)
    explore(grid,r+1,c,visited_locations)
    explore(grid,r-1,c,visited_locations)

    return True




grid = [ ["1","1","1","1","0"], ["1","1","0","1","0"], ["1","1","0","0","0"], ["0","0","0","0","0"]
]
print(num_of_islands(grid))

grid2 = [ ["1","1","0","0","0"], ["1","1","0","0","0"], ["0","0","1","0","0"], ["0","0","0","1","1"]
]
print(num_of_islands(grid2))