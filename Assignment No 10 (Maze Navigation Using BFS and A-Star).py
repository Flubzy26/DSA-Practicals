from collections import deque
import heapq

# Directions (up, down, left, right)
DIRS = [(0,1),(0,-1),(1,0),(-1,0)]

# Utility function: print maze with path
def print_maze(maze, path):
    maze_copy = [row[:] for row in maze]
    for (x,y) in path:
        if maze_copy[x][y] not in ('S','G'):
            maze_copy[x][y] = '*'
    for row in maze_copy:
        print(' '.join(row))
    print()

# BFS Algorithm
def bfs(maze, start, goal):
    n, m = len(maze), len(maze[0])
    queue = deque([start])
    visited = set([start])
    parent = {}

    while queue:
        x,y = queue.popleft()
        if (x,y) == goal:
            path = []
            while (x,y) != start:
                path.append((x,y))
                x,y = parent[(x,y)]
            path.append(start)
            return path[::-1]
        for dx,dy in DIRS:
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<m and maze[nx][ny] != '#' and (nx,ny) not in visited:
                visited.add((nx,ny))
                parent[(nx,ny)] = (x,y)
                queue.append((nx,ny))
    return None

# Heuristic for A*
def heuristic(a,b):
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

# A* Algorithm
def astar(maze, start, goal):
    n, m = len(maze), len(maze[0])
    open_list = []
    heapq.heappush(open_list, (0+heuristic(start,goal), 0, start))
    parent = {}
    g_score = {start: 0}

    while open_list:
        _, g, current = heapq.heappop(open_list)
        if current == goal:
            path = []
            while current != start:
                path.append(current)
                current = parent[current]
            path.append(start)
            return path[::-1]

        for dx,dy in DIRS:
            nx, ny = current[0]+dx, current[1]+dy
            if 0<=nx<n and 0<=ny<m and maze[nx][ny] != '#':
                neighbor = (nx,ny)
                tentative_g = g + 1
                if tentative_g < g_score.get(neighbor, float('inf')):
                    g_score[neighbor] = tentative_g
                    f = tentative_g + heuristic(neighbor,goal)
                    heapq.heappush(open_list, (f, tentative_g, neighbor))
                    parent[neighbor] = current
    return None

# ----------------- MAIN DRIVER -----------------
def main():
    print("Maze Navigation System (Static & Dynamic)")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    print("\nEnter maze row by row without space:")
    print("Use S for Start, G for Goal, # for Wall, . for Free Path")
    maze = []
    start = goal = None

    for i in range(rows):
        row = list(input(f"Row {i+1}: ").strip())
        maze.append(row)
        for j in range(cols):
            if row[j] == 'S':
                start = (i,j)
            if row[j] == 'G':
                goal = (i,j)

    if not start or not goal:
        print("Error: Maze must contain Start (S) and Goal (G).")
        return

    while True:
        print("\nMenu:")
        print("1. Solve using BFS")
        print("2. Solve using A*")
        print("3. Modify Maze (Dynamic)")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            print("\nSolving with BFS...")
            path = bfs(maze, start, goal)
            if path:
                print_maze(maze, path)
            else:
                print("No path found by BFS.")

        elif choice == '2':
            print("\nSolving with A* Search...")
            path = astar(maze, start, goal)
            if path:
                print_maze(maze, path)
            else:
                print("No path found by A*.")

        elif choice == '3':
            print("\nModify Maze:")
            r = int(input("Enter row index (0-based): "))
            c = int(input("Enter col index (0-based): "))
            val = input("Enter new value (# for wall, . for free): ").strip()
            if maze[r][c] not in ('S','G'):
                maze[r][c] = val
            print("Updated Maze:")
            print_maze(maze, [])

        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
