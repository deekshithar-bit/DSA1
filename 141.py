def maximum_xor(nums): #Maximum XOR of two numbers in an array
    max_xor = 0

    for i in range(len(nums)):
        for j in range(i, len(nums)):
            max_xor = max(max_xor, nums[i] ^ nums[j])

    return max_xor


nums = [3, 9, 10, 5, 1]
print(maximum_xor(nums))