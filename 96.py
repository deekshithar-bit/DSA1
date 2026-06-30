def twoCitySchedCost(costs): #Two City Scheduling
    # sort descending by (cost[1] - cost[0])
    costs.sort(key=lambda x: x[1] - x[0], reverse=True)
    n = len(costs) // 2
    ans = sum(cost[0] for cost in costs[:n]) + sum(cost[1] for cost in costs[n:])
    return ans

if __name__ == "__main__":
    costs = [[10,20],[30,200],[400,50],[30,20]]
    print(twoCitySchedCost(costs))  # prints result