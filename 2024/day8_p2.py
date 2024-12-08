def main():
    with open('day8_input.txt') as file:
        lines = file.readlines()
    
    max_x = len(lines[0].strip())
    max_y = len(lines)

    symbol_set = []
    antenna_set = {}

    for i in range(max_y):
        for j in range(max_x):
            symbol = lines[i][j]
            if symbol == '.':
                continue
            if symbol not in symbol_set:
                symbol_set.append(symbol)
            index = symbol_set.index(symbol)
            if index not in antenna_set:
                antenna_set[index] = set()
            antenna_set[index].add((i, j))
                
    print("Symbol Set:", symbol_set)
    print("Antenna Set:")
    for index, positions in antenna_set.items():
        print(f"Symbol index {index} ({symbol_set[index]}):")
        for position in positions:
            print(position)

    antinodes = set()

    # Example of working with positions
    for index, positions in antenna_set.items():
        # Pair up coordinates within each group and do some work
        positions_list = list(positions)
        for i in range(len(positions_list)):
            for j in range(i + 1, len(positions_list)):
                pos1 = positions_list[i]
                pos2 = positions_list[j]
                
                # Calculate the direction vector
                direction_x = pos2[0] - pos1[0]
                direction_y = pos2[1] - pos1[1]
                
                # Calculate new coordinates based on the direction vector
                new_x1, new_y1 = pos1[0], pos1[1]
                new_x2, new_y2 = pos2[0], pos2[1]
                
                # Add antinode points extending in the positive direction
                while 0 <= new_x1 < max_y and 0 <= new_y1 < max_x:
                    new_x1 += direction_x
                    new_y1 += direction_y
                    if 0 <= new_x1 < max_y and 0 <= new_y1 < max_x:
                        antinodes.add((new_x1, new_y1))
                
                # Add antinode points extending in the negative direction
                while 0 <= new_x2 < max_y and 0 <= new_y2 < max_x:
                    new_x2 -= direction_x
                    new_y2 -= direction_y
                    if 0 <= new_x2 < max_y and 0 <= new_y2 < max_x:
                        antinodes.add((new_x2, new_y2))
                
    res = len(antinodes)
    print("Total unique antinode locations:", res)

if __name__ == '__main__':
    main()