def turn(direction):
    if direction == 'Up':
        return 'Right'
    elif direction == 'Right':
        return 'Down'
    elif direction == 'Down':
        return 'Left'
    elif direction == 'Left':
        return 'Up'

def travel(current_x, current_y, direction, max_x, max_y, grid):
    exit = False
    if direction == 'Up':
        if current_x - 1 >= 0:
            if grid[current_x - 1][current_y] == '#':
                direction = turn(direction)
                print(f"Turning right. New direction: {direction}")
            else:
                grid[current_x][current_y] = 'X'
                grid[current_x - 1][current_y] = '^'
                current_x -= 1
        else:
            grid[current_x][current_y] = 'O'
            exit = True
    elif direction == 'Down':
        if current_x + 1 <= max_x:
            if grid[current_x + 1][current_y] == '#':
                direction = turn(direction)
                print(f"Turning right. New direction: {direction}")
            else:
                grid[current_x][current_y] = 'X'
                grid[current_x + 1][current_y] = '^'
                current_x += 1
        else:
            grid[current_x][current_y] = 'O'
            exit = True
    elif direction == 'Left':
        if current_y - 1 >= 0:
            if grid[current_x][current_y - 1] == '#':
                direction = turn(direction)
                print(f"Turning right. New direction: {direction}")
            else:
                grid[current_x][current_y] = 'X'
                grid[current_x][current_y - 1] = '^'
                current_y -= 1
        else:
            grid[current_x][current_y] = 'O'
            exit = True
    elif direction == 'Right':
        if current_y + 1 <= max_y:
            if grid[current_x][current_y + 1] == '#':
                direction = turn(direction)
                print(f"Turning right. New direction: {direction}")
            else:
                grid[current_x][current_y] = 'X'
                grid[current_x][current_y + 1] = '^'
                current_y += 1
        else:
            grid[current_x][current_y] = 'O'
            exit = True
    
    return current_x, current_y, direction, exit

def main():
    with open('day6_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    grid = [list(line) for line in data]
    
    current_x = 0
    current_y = 0

    max_x = len(grid) - 1
    max_y = len(grid[0]) - 1
    
    found = False
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '^':
                current_x = i
                current_y = j
                found = True
                break
        if found:
            break
    
    print(f"Starting position: {current_x}, {current_y}")
    
    exit = False
    direction = "Up"
    visited = set()
    while not exit:
        if (current_x, current_y, direction) in visited:
            print(f"Loop detected at position: ({current_x}, {current_y}) with direction: {direction}")
            break
        visited.add((current_x, current_y, direction))
        current_x, current_y, direction, exit = travel(current_x, current_y, direction, max_x, max_y, grid)
    
    print("Final grid:")
    for row in grid:
        print(''.join(row))
    
    res = 0   
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'X' or grid[i][j] == 'O':
                res += 1
                
    print("Res:", res)

if __name__ == '__main__':
    main()