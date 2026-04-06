import heapq

# Heuristic function: Manhattan distance for grid movement
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    
    # Priority queue to store (f_score, current_node)
    open_list = []
    heapq.heappush(open_list, (0, start))
    
    # Tracking the path and costs
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}

    while open_list:
        # Pop node with the lowest f_score
        current = heapq.heappop(open_list)[1]

        # Check if goal reached
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1] # Return reversed path

        x, y = current
        # Define 4-way connectivity (up, down, left, right)
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]

        for nx, ny in neighbors:
            # Boundary check
            if 0 <= nx < rows and 0 <= ny < cols:
                # Obstacle check ('#' represents walls)
                if grid[nx][ny] == '#':
                    continue
                
                # Calculate tentative g_score
                tentative_g = g_score[current] + 1
                
                # If path to neighbor is better, record it
                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    came_from[(nx, ny)] = current
                    g_score[(nx, ny)] = tentative_g
                    f_score[(nx, ny)] = tentative_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_list, (f_score[(nx, ny)], (nx, ny)))
    
    return None # Path not found
