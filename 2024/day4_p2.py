def main():
    with open('day4_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    # Map the input into a 2D array
    grid = [list(line) for line in data]
    
    res = 0
    
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] != "A":
                continue
            
            # Check the four corners of the 3x3 square around the element
            top_left = grid[i-1][j-1]
            top_right = grid[i-1][j+1]
            bottom_left = grid[i+1][j-1]
            bottom_right = grid[i+1][j+1]
            
            # Check sides for 2 M's and 2 S's
            top_side = top_left + top_right
            bottom_side = bottom_left + bottom_right
            left_side = top_left + bottom_left
            right_side = top_right + bottom_right
            
            sides = [top_side, bottom_side, left_side, right_side]
            
            m_count = sum(side.count('M') == 2 for side in sides)
            s_count = sum(side.count('S') == 2 for side in sides)
            
            if m_count == 1 and s_count == 1:
                res += 1
    
    print(res)
                
if __name__ == '__main__':
    main()