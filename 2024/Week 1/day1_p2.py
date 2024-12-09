import math

def main():
    left_array = []
    right_array = []
    res = 0

    with open('day1_input.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_array.append(left)
            right_array.append(right)
    
    left_array.sort()
    right_array.sort()

    max_value = max(right_array)  # Find the maximum value in right_array
    right_array_count = [0] * (max_value + 1)  # Initialize right_array_count with zeros

    for i in range(len(right_array)):
        right_array_count[right_array[i]] += 1
        
    for i in range(len(left_array)):
        if left_array[i] < len(right_array_count):
            res += left_array[i] * right_array_count[left_array[i]]

    print("Result:", res)

if __name__ == "__main__":
    main()