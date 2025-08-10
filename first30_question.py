# 1. Reverse an array
def reverse_array(arr):
    # Your code here: reverse the array without using reverse() or slicing
    pass

# 2. Find the maximum element in an array
def find_max(arr):
    # Loop through and find the largest value
    pass

# 3. Check if a string is a palindrome
def is_palindrome(s):
    # Ignore case and spaces
    pass

# 4. Find the factorial of a number (recursion)
def factorial(n):
    # Base case: n == 0 or n == 1 → return 1
    pass

# 5. Find the nth Fibonacci number (recursion)
def fibonacci(n):
    # F(n) = F(n-1) + F(n-2)
    pass

# 6. Linear search in an array
def linear_search(arr, target):
    # Check each element one by one
    pass

# 7. Binary search in a sorted array
def binary_search(arr, target):
    # Divide and conquer method
    pass

# 8. Bubble sort
def bubble_sort(arr):
    # Compare adjacent elements and swap
    pass

# 9. Selection sort
def selection_sort(arr):
    # Find the smallest element and place it in front
    pass

# 10. Insertion sort
def insertion_sort(arr):
    # Insert each element into the sorted portion
    pass

# 11. Merge sort
def merge_sort(arr):
    # Divide array, sort halves, and merge
    pass

# 12. Quick sort
def quick_sort(arr):
    # Partition array around a pivot
    pass

# 13. Find duplicate elements in an array
def find_duplicates(arr):
    # Use set or dictionary to track seen elements
    pass

# 14. Rotate an array by k positions
def rotate_array(arr, k):
    # Shift elements to the right k times
    pass

# 15. Check if two strings are anagrams
def are_anagrams(s1, s2):
    # Compare sorted characters
    pass

# 16. Count vowels in a string
def count_vowels(s):
    # Check each character if it’s a vowel
    pass

# 17. Find the intersection of two arrays
def array_intersection(arr1, arr2):
    # Elements present in both arrays
    pass

# 18. Find the missing number in 1 to n
def find_missing_number(arr, n):
    # Use sum formula: n*(n+1)/2
    pass

# 19. Check if array is sorted
def is_sorted(arr):
    # Compare each element with the next
    pass

# 20. Stack implementation using list
class Stack:
    def __init__(self):
        self.stack = []
    def push(self, item):
        pass
    def pop(self):
        pass
    def peek(self):
        pass
    def is_empty(self):
        pass

# 21. Queue implementation using list
class Queue:
    def __init__(self):
        self.queue = []
    def enqueue(self, item):
        pass
    def dequeue(self):
        pass
    def is_empty(self):
        pass

# 22. Find GCD of two numbers (Euclidean algorithm)
def gcd(a, b):
    # Keep replacing a with b and b with a % b
    pass

# 23. Check if number is prime
def is_prime(n):
    # Check divisibility from 2 to sqrt(n)
    pass

# 24. Reverse a linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def reverse_linked_list(head):
    # Use three pointers: prev, curr, next
    pass

# 25. BFS in a graph
from collections import deque
def bfs(graph, start):
    # Use queue to explore neighbors
    pass

# 26. DFS in a graph
def dfs(graph, start, visited=None):
    # Recursively visit nodes
    pass

# 27. Find shortest path in unweighted graph (BFS)
def shortest_path(graph, start, end):
    # Track distance using BFS
    pass

# 28. Find all permutations of a string
def string_permutations(s):
    # Use recursion + swapping
    pass

# 29. Knapsack Problem (0/1) - DP
def knapsack(weights, values, capacity):
    # DP table solution
    pass

# 30. Longest Common Subsequence (LCS) - DP
def lcs(s1, s2):
    # Create 2D DP table
    pass
