n = int(input())
count = 0
for i in range(1, n + 1):
    for j in range(1, n + 1):
        cond = i % j == 0 or j % i == 0
        count += cond
        print('*' if cond else '-', end='')
    print()
print(count)
