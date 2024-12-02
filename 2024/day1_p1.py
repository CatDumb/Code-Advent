import math

def main():
    left_array = []
    right_array = []
    res = 0

    with open('input.txt', 'r') as file:
        for line in file:
            left, right = map(int, line.split())
            left_array.append(left)
            right_array.append(right)
    
    left_array.sort()
    right_array.sort()

    for i in range(len(left_array)):
        res += abs(left_array[i] - right_array[i])

    print("Result:", res)

if __name__ == "__main__":
    main()