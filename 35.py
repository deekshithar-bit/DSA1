from collections import defaultdict

def groupAnagrams(strs): #Group Anagrams
    anagrams = defaultdict(list)

    for word in strs:
        key = ''.join(sorted(word))
        anagrams[key].append(word)

    return list(anagrams.values())

# Example input
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

# Function call
result = groupAnagrams(words)

# Print output
print(result)