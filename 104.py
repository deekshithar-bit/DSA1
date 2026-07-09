def leastInterval(tasks, n): #Task Scheduler 
    freq = [0] * 26
    maxFreq = 0

    for t in tasks:
        c = t[0]  # in case it's a string
        idx = ord(c) - ord('A')
        freq[idx] += 1
        if freq[idx] > maxFreq:
            maxFreq = freq[idx]

    countOfMax = sum(1 for f in freq if f == maxFreq)
    cycles = (n + 1) * (maxFreq - 1) + countOfMax

    return max(len(tasks), cycles)


# Example input
tasks = ["A", "A", "A", "B", "B", "B"]
n = 2

# Function call
result = leastInterval(tasks, n)

# Output
print("Minimum intervals required:", result)