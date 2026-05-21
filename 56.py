from typing import List #Two Sum ( Input Array Is Sorted)

def twoSum(numbers: List[int], target: int) -> List[int]:
    i = 0
    j = len(numbers) - 1

    while i < j:
        current_sum = numbers[i] + numbers[j]

        if current_sum > target:
            j -= 1
        elif current_sum < target:
            i += 1
        else:
            return [i + 1, j + 1]   # 1-based indexing

    return []


# Example usage
numbers = [2, 7, 11, 15]
target = 9

result = twoSum(numbers, target)
print("Output:", result)