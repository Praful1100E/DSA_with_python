# -----------------------------
# DSA in Python (Set 3 - Intermediate)
# -----------------------------

# 1. Bubble Sort
print("\n1. Bubble Sort")
arr = [64, 34, 25, 12, 22, 11, 90]
n = len(arr)
for i in range(n):
    for j in range(0, n-i-1):
        if arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
print("Sorted Array:", arr)


# 2. Selection Sort
print("\n2. Selection Sort")
arr = [29, 10, 14, 37, 13]
for i in range(len(arr)):
    min_index = i
    for j in range(i+1, len(arr)):
        if arr[j] < arr[min_index]:
            min_index = j
    arr[i], arr[min_index] = arr[min_index], arr[i]
print("Sorted Array:", arr)


# 3. Insertion Sort
print("\n3. Insertion Sort")
arr = [12, 11, 13, 5, 6]
for i in range(1, len(arr)):
    key = arr[i]
    j = i - 1
    while j >= 0 and key < arr[j]:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
print("Sorted Array:", arr)


# 4. Merge Sort
print("\n4. Merge Sort")
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
arr = [38, 27, 43, 3, 9, 82, 10]
merge_sort(arr)
print("Sorted Array:", arr)


# 5. Quick Sort
print("\n5. Quick Sort")
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x <= pivot]
    right = [x for x in arr[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)
arr = [10, 7, 8, 9, 1, 5]
print("Sorted Array:", quick_sort(arr))


# 6. Find Kth Largest Element
print("\n6. Find Kth Largest Element")
arr = [3, 2, 1, 5, 6, 4]
k = 2
arr.sort(reverse=True)
print(f"{k}th Largest Element:", arr[k-1])


# 7. Stack Implementation using List
print("\n7. Stack Implementation using List")
stack = []
stack.append(10)  # push
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)
print("Popped Element:", stack.pop())  # pop
print("Stack after pop:", stack)


# 8. Queue Implementation using List
print("\n8. Queue Implementation using List")
from collections import deque
queue = deque()
queue.append(10)  # enqueue
queue.append(20)
queue.append(30)
print("Queue after enqueues:", queue)
print("Dequeued Element:", queue.popleft())  # dequeue
print("Queue after dequeue:", queue)


# 9. Find First Non-Repeating Character in String
print("\n9. First Non-Repeating Character in String")
s = "aabbcdeff"
for char in s:
    if s.count(char) == 1:
        print("First non-repeating character:", char)
        break


# 10. Find Longest Word in a Sentence
print("\n10. Find Longest Word in a Sentence")
sentence = "Data Structures and Algorithms are important for coding"
words = sentence.split()
longest = max(words, key=len)
print("Sentence:", sentence)
print("Longest Word:", longest)

# -----------------------------
# END OF FILE
# -----------------------------
