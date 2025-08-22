# -----------------------------
# Beginner Level DSA in Python
# -----------------------------

# 1. Reverse an Array
print("\n1. Reverse an Array")
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print("Original:", arr)
print("Reversed:", reversed_arr)


# 2. Find Maximum and Minimum in an Array
print("\n2. Find Maximum and Minimum in an Array")
arr = [12, 3, 45, 7, 9, 1]
print("Array:", arr)
print("Maximum:", max(arr))
print("Minimum:", min(arr))


# 3. Check Palindrome String
print("\n3. Check Palindrome String")
s = "madam"
if s == s[::-1]:
    print(s, "is a Palindrome")
else:
    print(s, "is NOT a Palindrome")


# 4. Find Duplicate Elements in an Array
print("\n4. Find Duplicate Elements in an Array")
arr = [1, 2, 3, 2, 4, 5, 1]
duplicates = []
for i in arr:
    if arr.count(i) > 1 and i not in duplicates:
        duplicates.append(i)
print("Array:", arr)
print("Duplicate Elements:", duplicates)


# 5. Linear Search
print("\n5. Linear Search")
arr = [10, 20, 30, 40, 50]
x = 30
found = False
for i in range(len(arr)):
    if arr[i] == x:
        print(f"Element {x} found at index {i}")
        found = True
        break
if not found:
    print(f"Element {x} not found")


# 6. Binary Search (on Sorted Array)
print("\n6. Binary Search (on Sorted Array)")
def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

arr = [10, 20, 30, 40, 50]
x = 40
result = binary_search(arr, x)
if result != -1:
    print(f"Element {x} found at index {result}")
else:
    print("Element not found")


# 7. Sum of Elements in an Array
print("\n7. Sum of Elements in an Array")
arr = [1, 2, 3, 4, 5]
print("Array:", arr)
print("Sum of elements:", sum(arr))


# 8. Count Vowels in a String
print("\n8. Count Vowels in a String")
s = "Hello World"
vowels = "aeiouAEIOU"
count = 0
for ch in s:
    if ch in vowels:
        count += 1
print("String:", s)
print("Number of vowels:", count)


# 9. Fibonacci Series (using Recursion)
print("\n9. Fibonacci Series (using Recursion)")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 7  # First 7 numbers
print("Fibonacci Series:", end=" ")
for i in range(n):
    print(fibonacci(i), end=" ")
print()


# 10. Factorial of a Number
print("\n10. Factorial of a Number")

# Iterative method
def factorial_iterative(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

# Recursive method
def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n-1)

num = 5
print(f"Factorial of {num} (Iterative):", factorial_iterative(num))
print(f"Factorial of {num} (Recursive):", factorial_recursive(num))

# -----------------------------
# END OF FILE
# -----------------------------
