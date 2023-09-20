def cutRod(n, price):
    max_values = [0] * (n + 1)
    for i in range(1, n + 1):
        max_value = -1  
        for j in range(i):
            max_value = max(max_value, price[j] + max_values[i - j - 1])
        max_values[i] = max_value
    return max_values[n]

lengths = [1, 2, 3, 4, 5, 6, 7, 8]
prices = [1, 5, 8, 9, 10, 17, 17, 20]
n = 8
result = cutRod(n, prices)
print("Maximum obtainable value:", result)
