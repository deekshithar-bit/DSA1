def maxFreqSum(s): #Find Most Frequent Vowel and Consonant
    from collections import Counter
    freq = Counter(s)
    vowels = set('aeiou')

    maxV = max((freq[ch] for ch in freq if ch in vowels), default=0)
    maxC = max((freq[ch] for ch in freq if ch not in vowels), default=0)

    return maxV + maxC


# Example usage
s = "Deekshitha"
result = maxFreqSum(s)
print("Output:", result)