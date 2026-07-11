def carPooling(trips, capacity): #car pooling
    loc = [0] * 1001

    for passengers, frm, to in trips:
        loc[frm] += passengers
        loc[to] -= passengers

    used_capacity = 0
    for x in loc:
        used_capacity += x
        if used_capacity > capacity:
            return False

    return True


# Example input
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4

# Output
print("Can complete all trips:", carPooling(trips, capacity))