from A_star_algorithm import astar

grid = [
['S', '.', '.', '.', '.'],
['#', '#', '.', '#', '.'],
['.', '.', '.', '#', '.'],
['.', '#', '#', '#', '.'],
['.', '.', '.', '.', 'E']
]

Origin = 'S'
Barrier = '#'
Space = '.'
The_path_found_by_the_algorithm = '*'
Destination = 'E'         


start = (0,0)
goal = (4,4)

path = astar(grid, start, goal)

print("Path:", path)

for i in range(len(grid)):
    for j in range(len(grid[0])):

        if (i,j) == start:
            print("S", end=" ")

        elif (i,j) == goal:
            print("E", end=" ")

        elif path and (i,j) in path:
            print("*", end=" ")

        else:
            print(grid[i][j], end=" ")

    print()
