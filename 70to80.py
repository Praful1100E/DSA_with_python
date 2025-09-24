# dsa_questions.py
# ---------------------------------------------
# This file contains 10 DSA questions in Python
# Each problem includes a function, explanation,
# and test cases to demonstrate its working.
# ---------------------------------------------

# 1. Reverse a String using Stack
def reverse_string(s: str) -> str:
    stack = list(s)  # push characters into stack
    reversed_str = ""
    while stack:  # pop until empty
        reversed_str += stack.pop()
    return reversed_str


# 2. Find Maximum Element in an Array
def find_max(arr: list) -> int:
    max_val = arr[0]
    for num in arr:
        if num > max_val:
            max_val = num
    return max_val


# 3. Check if a String is Palindrome
def is_palindrome(s: str) -> bool:
    return s == s[::-1]


# 4. Implement Binary Search
def binary_search(arr: list, target: int) -> int:
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  # not found


# 5. Find Factorial using Recursion
def factorial(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# 6. Find Fibonacci Number using Dynamic Programming
def fibonacci(n: int) -> int:
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        dp.append(dp[i - 1] + dp[i - 2])
    return dp[n]


# 7. Find Intersection of Two Arrays
def intersection(arr1: list, arr2: list) -> list:
    return list(set(arr1) & set(arr2))


# 8. Implement Queue using List
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # add to rear

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)  # remove from front
        return None

    def is_empty(self):
        return len(self.items) == 0


# 9. Sort an Array using Bubble Sort
def bubble_sort(arr: list) -> list:
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # last i elements are sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# 10. Find First Non-Repeating Character in a String
def first_non_repeating_char(s: str) -> str:
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None


# ---------------------------------------------
# Testing All Functions
# ---------------------------------------------
if __name__ == "__main__":
    print("1. Reverse String:", reverse_string("hello"))
    print("2. Max Element:", find_max([3, 7, 2, 9, 5]))
    print("3. Palindrome Check (madam):", is_palindrome("madam"))
    print("4. Binary Search (9 in [1,3,5,7,9,11]):", binary_search([1, 3, 5, 7, 9, 11], 9))
    print("5. Factorial of 5:", factorial(5))
    print("6. Fibonacci(10):", fibonacci(10))
    print("7. Intersection:", intersection([1, 2, 3, 4], [3, 4, 5, 6]))
    
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("8. Queue Dequeue:", q.dequeue())
    
    print("9. Bubble Sort:", bubble_sort([64, 25, 12, 22, 11]))
    print("10. First Non-Repeating Character:", first_non_repeating_char("swiss"))
