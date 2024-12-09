import re

def main():
    with open('day5_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    # Split the data into two parts based on the empty line
    part1 = []
    part2 = []
    is_part2 = False
    
    for line in data:
        if line.strip() == "":
            is_part2 = True
            continue
        
        if is_part2:
            part2.append(line)
        else:
            part1.append(line)
    
    # Parse the ordering rules
    ordering_rules = []
    part1_pattern = r'(\d+)\|(\d+)'
    
    for line in part1:
        match = re.match(part1_pattern, line)
        if match:
            first = int(match.group(1))
            second = int(match.group(2))
            ordering_rules.append((first, second))
    
    print("Ordering Rules:", ordering_rules)
    
    # Check if each array in part2 has elements in the same order as the reference array
    def is_in_order(rules, test):
        for first, second in rules:
            if first in test and second in test:
                first_index = test.index(first)
                second_index = test.index(second)
                if first_index > second_index:
                    return False
        return True
    
    res = 0
    print("\nPart 2:")
    for line in part2:
        test_array = list(map(int, line.split(',')))
        if is_in_order(ordering_rules, test_array):
            middle_index = len(test_array) // 2
            middle_element = test_array[middle_index]
            res += middle_element
            print(f"{test_array} is in order, middle element {middle_element} added to res")
        else:
            print(f"{test_array} is not in order")
    
    print("Total res:", res)

if __name__ == '__main__':
    main()