def jump(nums): #Jump game 2
    currEnd = 0
    farthest = 0
    jumps = 0

    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])

        if i == currEnd:
            currEnd = farthest
            jumps += 1

    return jumps

# Example input
nums = [2, 3, 1, 1, 4]

# Output
print("Minimum jumps:", jump(nums))