def maxArea(height): #Container With Most Water
    i, j = 0, len(height) - 1
    max_water = 0

    while i < j:
        area = min(height[i], height[j]) * (j - i)
        max_water = max(max_water, area)

        if height[i] > height[j]:
            j -= 1
        else:
            i += 1

    return max_water


# Example input
height = [1,8,6,2,5,4,8,3,7]

# Function call
result = maxArea(height)

# Output
print("Maximum water contained:", result)