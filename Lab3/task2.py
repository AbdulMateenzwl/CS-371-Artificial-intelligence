def balance_brackets(input_str):
    n = len(input_str)
    
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if input_str[i - 1] == '(':
                dp[i][j] = dp[i - 1][j - 1]
            elif input_str[i - 1] == ')':
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j] + 1, dp[i][j - 1] + 1)
    
    min_open = dp[n][n]
    min_close = dp[n][n]
    
    balanced_str = '(' * min_open + input_str + ')' * min_close
    
    return balanced_str

input_str = "(a+b(c)"
balanced_sequence = balance_brackets(input_str)
print("Input:", input_str)
print("Output:", balanced_sequence)
