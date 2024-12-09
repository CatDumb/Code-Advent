import re

def main():
    with open('day3_input.txt', 'r') as file:
        data = file.read()
    
    # Regex pattern to match mul(x,x) with x being 1-3 digit long numbers
    pattern = r'mul\((\d{1,3}),(\d{1,3})\)'
    
    # Find all matches
    matches = re.findall(pattern, data)
    
    res = 0
    # Multiply the numbers and print the results
    for match in matches:
        num1, num2 = map(int, match)  # Convert the captured groups to integers
        temp = num1 * num2
        res += temp
    print(res)
    
if __name__ == "__main__":
    main()