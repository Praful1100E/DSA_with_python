# ============================================
# 30 Python Pattern Solutions with Comments
# ============================================

rows = 5  # You can change this for bigger patterns

# 1. Right-angled triangle of stars
# *
# **
# ***
# ****
# *****
for i in range(1, rows + 1):
    print("*" * i)
print()

# 2. Right-angled triangle of numbers
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

# 3. Right-angled triangle of alphabets
for i in range(1, rows + 1):
    for j in range(65, 65 + i):  # 65 = ASCII for 'A'
        print(chr(j), end="")
    print()
print()

# 4. Inverted right-angled triangle of stars
for i in range(rows, 0, -1):
    print("*" * i)
print()

# 5. Inverted right-angled triangle of numbers
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
print()

# 6. Square pattern of stars
for i in range(rows):
    print("*" * rows)
print()

# 7. Square pattern of numbers
for i in range(1, rows + 1):
    print(str(i) * rows)
print()

# 8. Hollow square of stars
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()

# 9. Hollow square with numbers
for i in range(rows):
    for j in range(rows):
        if i == 0 or i == rows - 1 or j == 0 or j == rows - 1:
            print("1", end="")
        else:
            print(" ", end="")
    print()
print()

# 10. Rotated half pyramid of stars
for i in range(1, rows + 1):
    print(" " * (rows - i) + "*" * i)
print()