def is_window_valid(counts, k): #Longest Repeating Character Replacement
    total = sum(counts)
    max_count = max(counts)
    return (total - max_count) <= k


def characterReplacement(s, k):
    if not s:
        return 0

    i = j = 0
    counts = [0] * 26
    counts[ord(s[0]) - ord('A')] = 1
    max_window = 0

    while j < len(s):
        if is_window_valid(counts, k):
            max_window = max(max_window, j - i + 1)
            j += 1

            if j < len(s):
                counts[ord(s[j]) - ord('A')] += 1
        else:
            counts[ord(s[i]) - ord('A')] -= 1
            i += 1

    return max_window


# Example test
s = "AABABBA"
k = 1

print(characterReplacement(s, k))