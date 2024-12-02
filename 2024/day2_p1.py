def process_line(line):
    return list(map(int, line.split()))

def safe_sequence(first, second, third):
    if (first >= second and second <= third) or (first <= second and second >= third) or abs(first - second) > 3 or abs(second - third) > 3:
        return False
    return True

def main():
    res = 0
    
    with open('day2_input.txt', 'r') as file:
        for line in file:
            safe = True
            array = process_line(line)
            for i in range(0, len(array) - 2):
                if not safe_sequence(array[i], array[i + 1], array[i + 2]):
                    safe = False
                    break
            if safe:
                res += 1
    
    print(res)

if __name__ == "__main__":
    main()