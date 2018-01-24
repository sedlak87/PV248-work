import numpy as np


def parse(line):
    p = line.split('=')
    left = p[0].split(' ')
    print(p)
    x = left[left.index('x') - 1]
    y = left[left.index('x') - 1]
    right = p[1].strip()
    row = [x, y, right]
    return row


matrix = np.array([[1, 2], [3, 4]])
print('Determinant: ', np.linalg.det(matrix))
print('Inversion: ', np.linalg.inv(matrix))
print('Solution: (x, y) = ', np.linalg.solve(matrix, np.array([1, 2])))

firstLine = input('Enter first line:')
secondLine = input('Enter second line:')

firstRow = parse(firstLine)
secondRow = parse(secondLine)
matrix = np.array([firstRow, secondRow])

print('Solution: (x, y) = ', np.linalg.solve(matrix, np.array([1, 2])))
