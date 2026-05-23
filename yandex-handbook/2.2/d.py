import numpy as np
from collections import deque

def bfs(matrix, start, end, n):
    visited = [False] * n
    distance = [-1] * n 
    
    queue = deque()
    queue.append(start)
    visited[start] = True
    distance[start] = 0
    
    while queue:
        current = queue.popleft()
        
        if current == end:
            return distance[current]

        for neighbor in range(n):
            if matrix[current][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)
    
    return -1

def main():
    n = int(input())
    matrix = np.zeros((n, n), dtype=int)
    
    for i in range(n):
        matrix[i] = list(map(int, input().split()))

    start, end = map(int, input().split())
    
    result = bfs(matrix, start, end, n)
    print(result)


if __name__ == '__main__':
    main()
