def main():
    sample_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    
    with open('day1_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    res = 0
    for line in data:
        first, second = 0, 0
        for i in range(len(line)):
            if line[i] in sample_digit:  # Check if the character is a digit
                first = int(line[i])
                break
        
        j = len(line)
        while j > 0:
            j -= 1
            if line[j] in sample_digit:
                second = int(line[j])
                break
            
        print (first * 10 + second)
        res += first * 10 + second
        
    print(res)
            
        
if __name__ == '__main__':
    main()