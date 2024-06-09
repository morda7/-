def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        a = []
        for j in range(m):
            a.append(value)
            matrix.append(a)
        return matrix

result1 = get_matrix(2, 4, 5)
result2 = get_matrix(1, 1, 1,)
result3 = get_matrix(10, 11, 2)
print(result1)
print(result2)
print(result3)





