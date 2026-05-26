#Three Sum
def twoSum(arr, x, ans): 
    i = x + 1
    j = len(arr) - 1

    while i < j:
        s = arr[i] + arr[j] + arr[x]

        if s > 0:
            j -= 1
        elif s < 0:
            i += 1
        else:
            ans.append([arr[x], arr[i], arr[j]])

            i += 1
            j -= 1

            # Skip duplicate elements
            while i < j and arr[i] == arr[i - 1]:
                i += 1

            while i < j and arr[j] == arr[j + 1]:
                j -= 1


def threeSum(nums):
    nums.sort()
    ans = []

    for i in range(len(nums)):
        # Skip duplicates
        if i == 0 or nums[i] != nums[i - 1]:
            twoSum(nums, i, ans)

    return ans


# Example input
nums = [-1, 0, 1, 2, -1, -4]

# Function call
result = threeSum(nums)

# Output
print("Triplets whose sum is 0:")
print(result)