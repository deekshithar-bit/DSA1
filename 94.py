class Solution: #Word search 
    def exist(self, board, word: str) -> bool:
        if not board or not word:
            return False

        m, n = len(board), len(board[0])

        def backtrack(x, y, index):
            # Word completely matched
            if index == len(word):
                return True

            # Boundary check
            if x < 0 or x >= m or y < 0 or y >= n:
                return False

            # Character mismatch
            if board[x][y] != word[index]:
                return False

            # Mark visited
            temp = board[x][y]
            board[x][y] = "#"

            # Explore four directions
            found = (
                backtrack(x + 1, y, index + 1) or
                backtrack(x - 1, y, index + 1) or
                backtrack(x, y + 1, index + 1) or
                backtrack(x, y - 1, index + 1)
            )

            # Restore character
            board[x][y] = temp

            return found

        for i in range(m):
            for j in range(n):
                if backtrack(i, j, 0):
                    return True

        return False


# Test case
board = [
    ["A","B","C","E"],
    ["S","F","C","S"],
    ["A","D","E","E"]
]

word = "ABCCED"

solution = Solution()
print(solution.exist(board, word))