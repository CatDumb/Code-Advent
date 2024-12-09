import re

def main():
    with open('day2_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    # Regex pattern to match the game number and sets of quantities and colors
    pattern = r'Game (\d+): ((?:\d+ \w+(?:, )?)+(?:; )?)+'
    
    # Regex pattern to match the color and its quantity
    quantity_pattern = r'(\d+) (\w+)'
    
    for line in data:
        # Initialize counters for red, green, and blue cubes
        red = 0
        green = 0
        blue = 0
        
        # Find the game number and sets of quantities and colors
        game_match = re.match(pattern, line)
        print(game_match)
        # for i in range(0, 5):
        #     print(game_match.group(i))

if __name__ == '__main__':
    main()