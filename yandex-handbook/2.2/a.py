import sys
import numpy as np

def main():
    matrix = np.loadtxt(sys.stdin, dtype=int)
    found = False

    for i in range(matrix.shape[0]):
        if (matrix[i, i] == 1):
            print(i)
            found = True

    if not found:
        print("NO LOOPS")

if __name__ == '__main__':
    main()
