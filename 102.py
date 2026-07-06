def partition_labels(s: str): #Partition Labels
    last = [-1] * 26

    # Store the last occurrence of each character
    for i, ch in enumerate(s):
        last[ord(ch) - ord('a')] = i

    ans = []
    start = end = 0

    # Find partitions
    for i, ch in enumerate(s):
        end = max(end, last[ord(ch) - ord('a')])
        if i == end:
            ans.append(end - start + 1)
            start = i + 1

    return ans


if __name__ == "__main__":
    s = input().strip()
    result = partition_labels(s)
    print(" ".join(map(str, result)))