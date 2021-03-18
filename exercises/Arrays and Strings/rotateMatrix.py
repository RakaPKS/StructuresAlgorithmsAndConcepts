# Rotate a matrix 90 degrees

def rotate(matrix):
    return list(zip(*matrix[::-1]))


matrix = [[1, 2], [3, 4]]
print(rotate(matrix))
