rows = 5
# 11. Pyramid of stars
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print()

# 12. Pyramid of numbers
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(1, 2 * i):
        print(j, end="")
    print()
print()

# 13. Pyramid of alphabets
for i in range(1, rows + 1):
    print(" " * (rows - i), end="")
    for j in range(65, 65 + (2 * i - 1)):
        print(chr(j), end="")
    print()
print()

# 14. Inverted pyramid of stars
for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print()

# 15. Diamond of stars
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))
print()

# 16. Diamond of numbers
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

# 17. Floyd’s triangle
num = 1
for i in range(1, rows + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()
print()

# 18. Pascal’s triangle
def factorial(n):
    f = 1
    for k in range(1, n + 1):
        f *= k
    return f

for i in range(rows):
    print(" " * (rows - i), end="")
    for j in range(i + 1):
        print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
    print()
print()

# 19. Checkerboard pattern
for i in range(rows):
    for j in range(rows):
        print("*" if (i + j) % 2 == 0 else " ", end="")
    print()
print()

# 20. X pattern of stars
for i in range(rows):
    for j in range(rows):
        if j == i or j == rows - i - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()
