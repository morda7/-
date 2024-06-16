num = int(input())
result = '13'
for i in range(1, num):
    for j in(i + 1, num):
        if num % i + j:
            result += f'{i}{j}'
print(result)
