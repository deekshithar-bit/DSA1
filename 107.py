def candy(arr): #candy 
    n = len(arr)

    if n == 0:
        return 0

    ltr = [1] * n
    rtl = [1] * n

    # Left to right pass
    for i in range(1, n):
        if arr[i] > arr[i - 1]:
            ltr[i] = ltr[i - 1] + 1

    # Right to left pass
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1]:
            rtl[i] = rtl[i + 1] + 1

    ans = 0
    for i in range(n):
        ans += max(ltr[i], rtl[i])

    return ans


if __name__ == "__main__":
    ratings = [1, 0, 2]
    print("Ratings:", ratings)
    print("Minimum candies required:", candy(ratings))