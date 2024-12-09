def gen_array(string):
    genereated_list = []
    for i in range(0, len(string), 2):
        id = i // 2
        for j in range(int(string[i])):
            genereated_list.append(id)
        
        if (i + 1) < len(string):
            for k in range(int(string[i + 1])):
                genereated_list.append('.')
    return genereated_list

def compact_array(list):
    left = 0
    right = len(list) - 1
    
    while left < right:
        while list[left] != '.':
            left += 1
            
        while list[right] == '.':
            right -= 1
            
        if left >= right:
            break
        
        list[left], list[right] = list[right], list[left]
    return list

def checksum(list):
    res = 0
    
    for i in range(0, len(list)):
        if list[i] != '.':
            res += int(list[i]) * i
    
    return res    
                 
def main():
    with open('day9_input.txt') as file:
        data = file.read().strip()
    
    generated = gen_array(data)
    print(generated)
    compacted = compact_array(generated)
    print(compacted)
    res = checksum(compacted)
    print("Res:", res)

if __name__ == '__main__':
    main()