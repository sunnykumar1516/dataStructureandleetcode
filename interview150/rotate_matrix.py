#question number 48

def rotate(matrix):
    matrix2 = list(zip(*matrix))
    print(matrix)
    matrix = [list(reversed(item)) for item in matrix2]
    
    print(matrix)
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotate(mat)