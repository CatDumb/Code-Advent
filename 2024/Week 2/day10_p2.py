def find_next_node(grid, current_x, current_y, target_height):
    if grid[current_x][current_y] == target_height:
        return 1
    else:
        moved = False
        res = 0
        # Check all four adjacent nodes and traverse if they are 1 unit higher
        if current_x-1 >= 0 and grid[current_x-1][current_y] == grid[current_x][current_y] + 1:
            res += find_next_node(grid, current_x-1, current_y, target_height)
            moved = True
        if current_x+1 < len(grid) and grid[current_x+1][current_y] == grid[current_x][current_y] + 1:
            res += find_next_node(grid, current_x+1, current_y, target_height)
            moved = True
        if current_y-1 >= 0 and grid[current_x][current_y-1] == grid[current_x][current_y] + 1:
            res += find_next_node(grid, current_x, current_y-1, target_height)
            moved = True
        if current_y+1 < len(grid[0]) and grid[current_x][current_y+1] == grid[current_x][current_y] + 1:
            res += find_next_node(grid, current_x, current_y+1, target_height)
            moved = True
        
        if not moved:
            print(f"No available node to move to from ({current_x}, {current_y})")
        
    return res

def main():
    with open('day10_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    # Convert the input data to a grid of integers
    grid = [list(map(int, list(line))) for line in data]
    
    total_score = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 0:
                score = find_next_node(grid, i, j, 9)
                total_score += score
                print(f"Trailhead at ({i}, {j}) has a score of {score}")
                
    print("Total score of all trailheads:", total_score)

if __name__ == '__main__':
    main()