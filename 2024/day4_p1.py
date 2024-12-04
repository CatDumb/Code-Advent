def main():
    with open('day4_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    # Map the input into a 2D array
    grid = [list(line) for line in data]
    
    find = ["XMAS", "SAMX"]
    res = 0
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # Check horizontal string
            if j <= len(grid[0]) - 4:
                horizontal_string = grid[i][j] + grid[i][j+1] + grid[i][j+2] + grid[i][j+3]
                if horizontal_string in find:
                    res += 1
            
            # Check vertical string
            if i <= len(grid) - 4:
                vertical_string = grid[i][j] + grid[i+1][j] + grid[i+2][j] + grid[i+3][j]
                if vertical_string in find:
                    res += 1
            
            # Check diagonal (top-left to bottom-right)
            if i <= len(grid) - 4 and j <= len(grid[0]) - 4:
                diagonal_string1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] + grid[i+3][j+3]
                if diagonal_string1 in find:
                    res += 1
            
            # Check diagonal (bottom-left to top-right)
            if i >= 3 and j <= len(grid[0]) - 4:
                diagonal_string2 = grid[i][j] + grid[i-1][j+1] + grid[i-2][j+2] + grid[i-3][j+3]
                if diagonal_string2 in find:
                    res += 1
    
    print(res)
                
if __name__ == '__main__':
    main()