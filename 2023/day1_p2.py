import re

def main():
    sample_digit = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    sample_word = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    reverse_sample_word = ["orez", "eno", "owt", "eerht", "ruof", "evif", "xis", "neves", "thgie", "enin"]
    
    with open('day1_input.txt', 'r') as file:
        data = file.read().splitlines()
    
    res = 0
    for line in data:
        first, second = None, None
        reverse_line = line[::-1]
        
        # Find all matches for digits and words
        matches = re.findall(r'\d|zero|one|two|three|four|five|six|seven|eight|nine', line)
        reverse_match = re.findall(r'\d|orez|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin', reverse_line)
        if matches:
            # Get the first match
            first_match = matches[0]
            if first_match in sample_digit:
                first = int(first_match)
            elif first_match in sample_word:
                first = sample_word.index(first_match)
        
        if reverse_match:
            # Get the last match
            last_match = reverse_match[0]
            if last_match in sample_digit:
                second = int(last_match)
            elif last_match in reverse_sample_word:
                second = reverse_sample_word.index(last_match)
        
        if first is not None and second is not None:
            print(line," = ",first * 10 + second)
            res += first * 10 + second
        
    print("Total:", res)

if __name__ == '__main__':
    main()