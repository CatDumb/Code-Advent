def gen_array(string):
    generated_string = ''
    block = 0
    for i in range(len(string)):
        if i % 2 == 0:
            for j in range(int(string[i])):
                generated_string += str(block)
            block += 1
        else:
            for j in range(int(string[i])):
                generated_string += '.'
    return generated_string

def checksum(string):
    res = 0
    for i in range(len(string)):
        if string[i] != '.':
            res += int(string[i]) * i
    return res

def main():
    with open('day9_input.txt') as file:
        data = file.read().strip()
    
    parsed_string = gen_array(data)
    print("Parsed String:", parsed_string)
    
    free_index = []
    taken_index = []
    
    for i in range(len(parsed_string)):
        if parsed_string[i] != '.':
            taken_index.append(i)
        else:
            free_index.append(i)
    
    print("Initial Free Index:", free_index)
    print("Initial Taken Index:", taken_index)
    
    parsed_list = list(parsed_string)  # Convert string to list for swapping
    
    while free_index and taken_index:
        if free_index[0] < taken_index[-1]:
            # Swap elements
            parsed_list[free_index[0]], parsed_list[taken_index[-1]] = parsed_list[taken_index[-1]], parsed_list[free_index[0]]
            free_index.pop(0)
            taken_index.pop(-1)
        else:
            break

    parsed_string = ''.join(parsed_list)  # Convert list back to string
    print("Compacted String:", parsed_string)
    print("Res:", checksum(parsed_string))

if __name__ == '__main__':
    main()