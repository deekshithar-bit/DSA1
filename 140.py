def longest_complete_string(nums): #Longest Word with All Prefixes
    words = set(nums)
    answer = "None"

    for word in nums:
        complete = True

        # Check every prefix
        for i in range(1, len(word) + 1):
            if word[:i] not in words:
                complete = False
                break

        if complete:
            # Longer word is better.
            # If same length, lexicographically smaller is better.
            if answer == "None" or len(word) > len(answer) or (
                len(word) == len(answer) and word < answer
            ):
                answer = word

    return answer


# Example
nums = ["n", "ni", "nin", "ninj", "ninja", "nil"]

print(longest_complete_string(nums))