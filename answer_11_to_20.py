# 11. Merge Sort
def merge_sort(arr):
    # Base case: if array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
    # Split the array into two halves
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    # Merge the two sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    i = j = 0
    # Compare elements and merge in sorted order
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # Append remaining elements
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


# 12. Quick Sort
def quick_sort(arr):
    # Base case: arrays of length 0 or 1 are sorted
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]  # Choose middle element as pivot
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


# 13. Find duplicate elements in an array
def find_duplicates(arr):
    seen = set()
    duplicates = set()
    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    return list(duplicates)


# 14. Rotate an array by k positions
def rotate_array(arr, k):
    k = k % len(arr)  # Handle cases where k > len(arr)
    return arr[-k:] + arr[:-k]  # Slice and join


# 15. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


# 16. Count vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# 17. Find the intersection of two arrays
def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))


# 18. Find the missing number in 1 to n
def find_missing_number(arr, n):
    expected_sum = n * (n + 1) // 2
    return expected_sum - sum(arr)


# 19. Check if array is sorted
def is_sorted(arr):
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))


# 20. Stack implementation using list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)  # Add to top

    def pop(self):
        return self.stack.pop() if not self.is_empty() else None

    def peek(self):
        return self.stack[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.stack) == 0



