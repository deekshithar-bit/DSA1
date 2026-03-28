def count_negative_numbers(arr): #Count Negative Numbers in an Array
    count = 0
    for num in arr:
        if num < 0:
            count += 1
    return count

arr = [3, -7, 5, 9, -2, -10]
result = count_negative_numbers(arr)
print("Result:", result)

def find_smallest(arr): # smallest number in array
    smallest = float('inf')
    for num in arr:
        if num < smallest:
            smallest = num
    return smallest

arr1 = [2, -6, 4, 8, 1, -9]
result = find_smallest(arr1)
print("Result:", result) 

def find_largest(arr): #largest number in array
        largest = float('-inf')
        for num in arr:
         if num > largest:
          largest = num
        return largest
arr2 = [2, -6, 5, 8, 7, -9]
result = find_largest(arr2)
print("Result:", result) 