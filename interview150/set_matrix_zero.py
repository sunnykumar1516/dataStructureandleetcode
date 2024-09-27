# question number 73

def solve(mat):
    rows,cols = set(),set()
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if mat[row][col] == 0:
                rows.add(row)
                cols.add(col)
    for row in range(len(mat)):
        for col in range(len(mat[0])):
            if row in rows or col in cols:
                mat[row][col] = 0
    print(mat)

matrix = [[1,1,1],[1,0,1],[1,1,1]]
solve(matrix)
