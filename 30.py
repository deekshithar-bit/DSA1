def isPalindrome(s: str) -> bool: #Valid Palindrome | Approach 2 Two Pointers
    i, j = 0, len(s) - 1
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i].lower() == s[j].lower():
            i += 1
            j -= 1
        else:
            return False
    return True


# Example usage
test_string = " a man a plan a canal panama"
result = isPalindrome(test_string)

print("Input:", test_string)
print("Is Palindrome:", result)