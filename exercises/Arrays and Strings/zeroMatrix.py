# Given Matrix m  if an element in matrix M is 0 then its entire row and column is zeroed

def zeroMatrix(m):
    columns = set()
    for y, row in enumerate(m):
        emptyRow = False
        for x, val in enumerate(row):
            if val == 0:
                columns.add(x)
                emptyRow = True
        m[y] = [0] * len(row) if emptyRow else row

    for y, row in enumerate(m):
        for col in columns:
            m[y][col] = 0
    return m


matrix = [[1, 2], [3, 0]]
print(zeroMatrix(matrix))
