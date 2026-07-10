def canCompleteCircuit(gas, cost): #Gas station 
    currGain = 0
    totalGain = 0
    ans = 0

    for i in range(len(gas)):
        gain = gas[i] - cost[i]
        currGain += gain
        totalGain += gain

        if currGain < 0:
            ans = i + 1
            currGain = 0

    return -1 if totalGain < 0 else ans


# Example input
gas = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

# Output
print("Starting gas station index:", canCompleteCircuit(gas, cost))