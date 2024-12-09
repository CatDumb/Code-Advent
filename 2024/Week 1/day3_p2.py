import re

def main():
    with open('day3_input.txt', 'r') as file:
        data = file.read()
    
    # Regex pattern to match mul(x,x), do(), and don't()
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)'
    
    # Find all matches
    matches = re.finditer(pattern, data)
    
    res = 0
    DO = True
    # Multiply the numbers and print the results
    for match in matches:
        if match.group(1) and match.group(2):  # Check if the match is for mul(x,x)
            if DO:
                num1, num2 = int(match.group(1)), int(match.group(2))  # Convert the captured groups to integers
                temp_res = num1 * num2
                res += temp_res
                print(f"mul({num1},{num2}) = {temp_res}")
        elif match.group(0) == 'do()':  # Check if the match is for do()
            DO = True
        elif match.group(0) == "don't()":  # Check if the match is for don't()
            DO = False
        
    print("Total:", res)

if __name__ == "__main__":
    main()