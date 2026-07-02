def lemonadeChange(bills): #Lemonade Change 
    wallet = [0, 0]  # wallet[0] = count of $5 bills, wallet[1] = count of $10 bills

    for b in bills:
        if b == 5:
            wallet[0] += 1
        elif b == 10:
            wallet[1] += 1
            wallet[0] -= 1
        else:  # b == 20
            if wallet[1] > 0:
                wallet[1] -= 1
                wallet[0] -= 1
            else:
                wallet[0] -= 3

        if wallet[0] < 0:
            return False

    return True


# Test cases
print(lemonadeChange([5, 5, 5, 10, 20]))
print(lemonadeChange([5, 5, 10, 10, 20]))
print(lemonadeChange([5, 10, 20]))