class Solution: #Minimum number of bracket reversals needed to make an expression balanced
    # Function to calculate the minimum number of reversals to balance the expression
    def minReversalsToBalance(self, expression: str) -> int:
        # Count of unmatched '(' brackets
        open_brackets = 0

        # Count of unmatched ')' brackets
        close_brackets = 0

        # Traverse the string
        for ch in expression:
            if ch == '(':
                # Consider '(' as unmatched for now
                open_brackets += 1
            else:
                if open_brackets > 0:
                    # Match this ')' with a previous '('
                    open_brackets -= 1
                else:
                    # No matching '(' exists, so this ')' is unmatched
                    close_brackets += 1

        # If total number of unmatched brackets is odd, return -1
        if (open_brackets + close_brackets) % 2 != 0:
            return -1

        # Return minimum reversals required
        return (open_brackets + 1) // 2 + (close_brackets + 1) // 2


# Input expression
expression = "(()))("

# Create object of Solution
solver = Solution()

# Get result from function
result = solver.minReversalsToBalance(expression)

# Print the result
print("Minimum reversals required:", result)