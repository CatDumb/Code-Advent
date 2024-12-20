def find_trailheads(map_data):
    trailheads = []
    for i in range(len(map_data)):
        for j in range(len(map_data[0])):
            if map_data[i][j] == 0:
                trailheads.append((i, j))
    return trailheads

def bfs(map_data, start):
    from collections import deque
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([start])
    visited = set([start])
    score = 0
    
    while queue:
        x, y = queue.popleft()
        if map_data[x][y] == 9:
            score += 1
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map_data) and 0 <= ny < len(map_data[0]) and (nx, ny) not in visited:
                if map_data[nx][ny] == map_data[x][y] + 1:
                    queue.append((nx, ny))
                    visited.add((nx, ny))
    return score

def calculate_total_score(map_data):
    trailheads = find_trailheads(map_data)
    total_score = 0
    for trailhead in trailheads:
        total_score += bfs(map_data, trailhead)
    return total_score

def main():
    with open('day10_input.txt', 'r') as file:
        data = file.readlines()

    map_data = [list(map(int, line.strip())) for line in data]
    print(calculate_total_score(map_data))

if __name__ == '__main__':
    main()