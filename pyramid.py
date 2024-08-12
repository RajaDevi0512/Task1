n = 20
num = 1
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(int(num), end=" ")
        num += 1
    num = 1
    print()
