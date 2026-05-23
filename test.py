import sys
import numpy as np


def main():
    matrix = np.array([
        [0, 1, 0, 1],
        [0, 0, 0, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0]
    ])

    for i in range(matrix.shape[0]):
        row = matrix[i]
        found = False
        for j in range(matrix.shape[1]):
            if row[j] == 1:
                print(j, end=" ")
                found = True
        if not found:
            print()
        else:
            print()

if __name__ == '__main__':
    main()
