# 1
n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i * i
print(s)

# 2
n = int(input())
for i in range(1, n + 1):
    print(i, i + 1, i + 2)

# 3
n = int(input())
p = 1
for i in range(1, n + 1):
    if i % 2 != 0:
        p *= i
print(p)

# 4
n = int(input())
c = 0
for i in range(1, n + 1):
    if i % 7 == 0:
        c += 1
print(c)

# 5
n = int(input())
for i in range(1, n + 1):
    print(i * 5)
