import copy

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
    
    direction = "Up"
    res = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(f"Trying obstacle in position ({i}, {j})")
            if grid[i][j] != '#':
                temp_grid = copy.deepcopy(grid)
                temp_grid[i][j] = '#'
                visited = set()
                exit = False
                temp_x, temp_y = current_x, current_y
                temp_direction = direction
                while not exit:
                    if (temp_x, temp_y, temp_direction) in visited:
                        print(f"Loop detected at position: ({temp_x}, {temp_y}) with direction: {temp_direction}")
                        res += 1
                        break
                    visited.add((temp_x, temp_y, temp_direction))
                    temp_x, temp_y, temp_direction, exit = travel(temp_x, temp_y, temp_direction, max_x, max_y, temp_grid)
                if exit:
                    print(f"No loop detected with obstacle at position ({i}, {j})")
            else:
                print("Existing obstacle")
                continue

    print("Res:", res)

if __name__ == '__main__':
    main()