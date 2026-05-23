import numpy as np

def main():
    n = int(input())
    matrix = np.zeros((n, n), dtype=int)

    for i in range(n):
        line = input().strip()
        if line == "":
            continue
        
        vertices = line.split()
        for v in vertices:
            j = int(v)
            matrix[i, j] = 1
        
    for i in range(n):
        print(*matrix[i])

if __name__ == '__main__':
    main()
