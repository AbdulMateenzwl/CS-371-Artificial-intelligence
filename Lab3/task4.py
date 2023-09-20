def min_coins_required(target, denominations):
    min_coins = [float('inf')] * (target + 1)

    min_coins[0] = 0

    for i in range(1, target + 1):
        for coin in denominations:
            if i >= coin:
                min_coins[i] = min(min_coins[i], 1 + min_coins[i - coin])

    return min_coins[target]

denominations = [1, 5, 10, 25] 
target_price = 63  

result = min_coins_required(target_price, denominations)
print(f"The minimum number of coins to make {target_price} cents is {result}")
