def max_product(arr): #Maximum Product Subarray Approach 1 
    if not arr:
        return 0  # defensive
    max_prod_so_far = arr[0]
    min_prod_so_far = arr[0]
    total_max = arr[0]

    for i in range(1, len(arr)):
        current = arr[i]
        prev_max = max_prod_so_far

        max_prod_so_far = max(current, prev_max * current, min_prod_so_far * current)
        min_prod_so_far = min(current, prev_max * current, min_prod_so_far * current)

        total_max = max(total_max, max_prod_so_far)

    return total_max

# Example usage
arr = [2, 3, -2, 4]
result = max_product(arr)
print("Maximum product subarray:", result)