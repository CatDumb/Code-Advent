def gen_array(string):
    generated_list = []
    block_id = -1
    for i in range(0, len(string)):
        if i % 2 == 0:
            block_id += 1
            for j in range(int(string[i])):
                generated_list.append(block_id)
        else:
            for j in range(int(string[i])):
                generated_list.append('.')
    return generated_list, block_id

def identify_blocks(list):
    free_blocks = []
    taken_blocks = []
    
    free_start = 0
    while free_start < len(list):
        # Find the start of the free block
        while free_start < len(list) and list[free_start] != '.':
            free_start += 1
        
        if free_start >= len(list):
            break
        
        # Find the end of the free block
        free_end = free_start
        while free_end < len(list) and list[free_end] == '.':
            free_end += 1
        
        free_length = free_end - free_start
        free_blocks.append((free_start, free_length))
        
        free_start = free_end
    
    taken_start = 0
    while taken_start < len(list):
        # Find the start of the taken block
        while taken_start < len(list) and list[taken_start] == '.':
            taken_start += 1
        
        if taken_start >= len(list):
            break
        
        # Find the end of the taken block
        taken_end = taken_start
        while taken_end < len(list) and list[taken_end] == list[taken_start]:
            taken_end += 1
        
        taken_length = taken_end - taken_start
        taken_blocks.append((taken_start, taken_length))
        
        taken_start = taken_end
    
    return free_blocks, taken_blocks

def swap_blocks(list, free_start, length, taken_start, free_blocks, taken_blocks):
    # Swap the blocks
    list[free_start:free_start + length] = list[taken_start:taken_start + length]
    list[taken_start:taken_start + length] = ['.'] * length

    # Update free_blocks
    free_blocks.append((taken_start, length))
    free_blocks.sort()

    # Update the free block that was used
    for i in range(len(free_blocks)):
        if free_blocks[i][0] == free_start:
            free_blocks[i] = (free_start + length, free_blocks[i][1] - length)
            if free_blocks[i][1] == 0:
                free_blocks.pop(i)
            break

def modify_list(list, free_blocks, taken_blocks, max_block):
    # Iterate over taken_blocks in reverse order
    for taken_start, length in reversed(taken_blocks):
        for i in range(len(free_blocks)):
            if free_blocks[i][1] >= length and free_blocks[i][0] < taken_start:
                free_start = free_blocks[i][0]
                swap_blocks(list, free_start, length, taken_start, free_blocks, taken_blocks)
                break

def checksum(list):
    res = 0
    for i in range(len(list)):
        if list[i] != '.':
            res += int(list[i]) * i
    return res

def main():
    with open('day9_input.txt') as file:
        data = file.read().strip()
    
    generated_list, max_block = gen_array(data)
    
    free_blocks, taken_blocks = identify_blocks(generated_list)
    
    modify_list(generated_list, free_blocks, taken_blocks, max_block)
    
    compacted_string = ''.join(map(str, generated_list))
    print("Compacted List:", compacted_string)
    
    res = checksum(generated_list)
    print("Res:", res)

if __name__ == '__main__':
    main()