def process_line(line):
    return list(map(int, line.split()))

def safe_sequence(first, second):
    return abs(first - second) <= 3

def is_increasing_or_decreasing(array):
    is_increasing = all(array[i] < array[i + 1] for i in range(len(array) - 1))
    is_decreasing = all(array[i] > array[i + 1] for i in range(len(array) - 1))
    return is_increasing or is_decreasing

def is_safe(array):
    for i in range(len(array) - 1):
        if not safe_sequence(array[i], array[i + 1]):
            return False
    return True

def main():
    res = 0
    
    with open('day2_input.txt', 'r') as file:
        for line in file:
            array = process_line(line)
            
            if is_safe(array) and is_increasing_or_decreasing(array):
                res += 1
                continue
            
            safe = False
            for i in range(len(array)):
                new_array = array[:i] + array[i + 1:]
                if is_safe(new_array) and is_increasing_or_decreasing(new_array):
                    safe = True
                    break
            
            if safe:
                res += 1
    
    print(res)

if __name__ == "__main__":
    main()