# 1. Find Second Largest Element in Array
print("\n1. Find Second Largest Element in Array")
arr = [12, 35, 1, 10, 34, 1]
unique_arr = list(set(arr))  # Remove duplicates
unique_arr.sort()
print("Array:", arr)
print("Second Largest Element:", unique_arr[-2])


# 2. Check if Two Strings are Anagrams
print("\n2. Check if Two Strings are Anagrams")
s1, s2 = "listen", "silent"
if sorted(s1) == sorted(s2):
    print(s1, "and", s2, "are Anagrams")
else:
    print(s1, "and", s2, "are NOT Anagrams")


# 3. Remove Duplicates from Array
print("\n3. Remove Duplicates from Array")
arr = [1, 2, 2, 3, 4, 4, 5]
unique_arr = list(set(arr))  # Convert to set and back to list
print("Original Array:", arr)
print("Array without duplicates:", unique_arr)


# 4. Count Frequency of Each Element in Array
print("\n4. Count Frequency of Each Element in Array")
arr = [1, 2, 2, 3, 4, 3, 1, 5]
freq = {}
for num in arr:
    freq[num] = freq.get(num, 0) + 1
print("Array:", arr)
print("Frequencies:", freq)


# 5. Find Missing Number in 1 to N
print("\n5. Find Missing Number in 1 to N")
arr = [1, 2, 4, 5, 6]  # Missing number is 3
n = 6
expected_sum = n * (n + 1) // 2
actual_sum = sum(arr)
print("Missing Number:", expected_sum - actual_sum)


# 6. Find Intersection of Two Arrays
print("\n6. Find Intersection of Two Arrays")
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
intersection = list(set(arr1) & set(arr2))
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Intersection:", intersection)


# 7. Find Union of Two Arrays
print("\n7. Find Union of Two Arrays")
arr1 = [1, 2, 3, 4, 5]
arr2 = [4, 5, 6, 7, 8]
union = list(set(arr1) | set(arr2))
print("Union:", union)


# 8. Find Pair with Given Sum
print("\n8. Find Pair with Given Sum")
arr = [8, 7, 2, 5, 3, 1]
target = 10
pairs = []
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] + arr[j] == target:
            pairs.append((arr[i], arr[j]))
print("Array:", arr)
print("Target Sum:", target)
print("Pairs with sum:", pairs)


# 9. Move All Zeros to End of Array
print("\n9. Move All Zeros to End of Array")
arr = [0, 1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
result = [x for x in arr if x != 0] + [0] * arr.count(0)
print("Original Array:", arr)
print("After Moving Zeros:", result)


# 10. Check Balanced Parentheses
print("\n10. Check Balanced Parentheses")
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}
    for char in s:
        if char in mapping.values():  # opening brackets
            stack.append(char)
        elif char in mapping.keys():  # closing brackets
            if stack and stack[-1] == mapping[char]:
                stack.pop()
            else:
                return False
    return len(stack) == 0

expr = "{[()()]}"
print("Expression:", expr)
print("Is Balanced:", is_balanced(expr))
