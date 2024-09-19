import math
from array import *
def main():
    grid = input()
    print(type(grid))
    index = 0
    row = [[]]
    col = [[]]
    matrix = []
    k=0
    for i in grid:
        if i == "1" or i == "0":
            matrix.append(int(i))
    j=0
    lnt = math.sqrt(len(matrix))
    while index<lnt:
        while j<lnt:
            row[index][j] = matrix[k]
            col[j][index] = matrix[k]
            k+=1

    print(row)
    print(col)


main()