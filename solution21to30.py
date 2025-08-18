rows = 5
# 20. X pattern of stars
for i in range(rows):
    for j in range(rows):
        if j == i or j == rows - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# 21. Hollow diamond of stars
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    else:
        print("" + " " * (2 * i - 3) + "")
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    else:
        print("" + " " * (2 * i - 3) + "")
print()

# 22. Butterfly pattern
for i in range(1, rows + 1):
    print("" * i + " " * (2 * (rows - i)) + "" * i)
for i in range(rows, 0, -1):
    print("" * i + " " * (2 * (rows - i)) + "" * i)
print()

# 23. Number pyramid (centered)
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, i + 1):
        print(j, end="")
    for j in range(i - 1, 0, -1):
        print(j, end="")
    print()
print()

# 24. Hourglass of stars
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(2, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print()

# 25. Hollow pyramid of stars
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    if i == 1:
        print("*")
    elif i == rows:
        print("*" * (2 * i - 1))
    else:
        print("" + " " * (2 * i - 3) + "")
print()

# 26. Spiral matrix NxN
n = 4
matrix = [[0] * n for _ in range(n)]
num = 1
left, right, top, bottom = 0, n - 1, 0, n - 1
while left <= right and top <= bottom:
    for i in range(left, right + 1):
        matrix[top][i] = num
        num += 1
    top += 1
    for i in range(top, bottom + 1):
        matrix[i][right] = num
        num += 1
    right -= 1
    for i in range(right, left - 1, -1):
        matrix[bottom][i] = num
        num += 1
    bottom -= 1
    for i in range(bottom, top - 1, -1):
        matrix[i][left] = num
        num += 1
    left += 1
for row in matrix:
    print(" ".join(f"{x:2}" for x in row))
print()

# 27. Zig-zag pattern
n = 9
for i in range(3):
    for j in range(1, n + 1):
        if ((i + j) % 4 == 0) or (i == 1 and j % 4 == 0):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# 28. Hollow butterfly
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print(" " * (2 * (rows - i)), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print(" " * (2 * (rows - i)), end="")
    for j in range(1, i + 1):
        if j == 1 or j == i:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# 29. Diamond with numbers
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
print()

# 30. Sandglass pattern
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(2, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))