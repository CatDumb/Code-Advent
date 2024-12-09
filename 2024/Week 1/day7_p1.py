import re

def can_make(array, target):
    if len(array) == 0:
        return False
    if len(array) == 1:
        return target == array[0]
    
    last_element = array[-1]
    return (can_make(array[:-1], target - last_element) or
            (can_make(array[:-1], target / last_element) if target % last_element == 0 else False))

def main():
    with open('day7_input.txt') as file:
        lines = file.read().splitlines()

    res = 0
    match_pattern = r'(\d+):'
    
    for line in lines:
        array = line.split(' ')
        
        # Extract and convert the target to an integer
        target = int(re.findall(match_pattern, array[0])[0])
        
        # Convert the rest of the array elements to integers
        array = [int(x) for x in array[1:]]
        
        # Call the can_make function with the correct arguments
        result = can_make(array, target)
        if result:
            res += target
            
    print(res)

if __name__ == '__main__':
    main()