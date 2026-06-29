def solveNQueens(n): #N Queens
    result = []
    board = [["."] * n for _ in range(n)]

    def backtrack(row, colSet, digSet, antiDigSet):
        if row == n:
            result.append(["".join(r) for r in board])
            return

        for col in range(n):
            if col in colSet or (row - col) in digSet or (row + col) in antiDigSet:
                continue

            board[row][col] = "Q"
            colSet.add(col)
            digSet.add(row - col)
            antiDigSet.add(row + col)

            backtrack(row + 1, colSet, digSet, antiDigSet)

            board[row][col] = "."
            colSet.remove(col)
            digSet.remove(row - col)
            antiDigSet.remove(row + col)

    backtrack(0, set(), set(), set())
    return result


# Test the function
n = 4
solutions = solveNQueens(n)

print("Number of solutions:", len(solutions))

for solution in solutions:
    for row in solution:
        print(row)
    print()