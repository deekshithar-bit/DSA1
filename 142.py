class TrieNode: #Maximum Xor with an element from an array
    def __init__(self):
        self.children = [None, None]


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root

        for bit in range(30, -1, -1):
            b = (num >> bit) & 1

            if node.children[b] is None:
                node.children[b] = TrieNode()

            node = node.children[b]

    def max_xor(self, num):
        node = self.root
        result = 0

        for bit in range(30, -1, -1):
            b = (num >> bit) & 1
            opposite = 1 - b

            # Prefer opposite bit to maximize XOR
            if node.children[opposite] is not None:
                result |= (1 << bit)
                node = node.children[opposite]
            else:
                node = node.children[b]

        return result


def maximizeXor(nums, queries):
    nums.sort()

    # Store (mi, xi, original_index)
    queries_sorted = [
        (m, x, i) for i, (x, m) in enumerate(queries)
    ]
    queries_sorted.sort()

    trie = Trie()
    answer = [-1] * len(queries)

    j = 0

    for m, x, index in queries_sorted:

        # Insert all numbers <= m
        while j < len(nums) and nums[j] <= m:
            trie.insert(nums[j])
            j += 1

        # If at least one number is <= m
        if j > 0:
            answer[index] = trie.max_xor(x)

    return answer


# Example
nums = [4, 9, 2, 5, 0, 1]
queries = [[3, 0], [3, 10], [7, 5], [7, 9]]

print(maximizeXor(nums, queries))