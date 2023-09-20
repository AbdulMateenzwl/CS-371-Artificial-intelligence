def longest_common_substring(s1, s2):
    len_s1 = len(s1)
    len_s2 = len(s2)
    dp = [[0] * (len_s2 + 1) for i in range(len_s1 + 1)]
    max_length = 0  

    for i in range(1, len_s1 + 1):
        for j in range(1, len_s2 + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
            else:
                dp[i][j] = 0  
    return max_length

s1 = "abcdef"
s2 = "bcdf"
result = longest_common_substring(s1, s2)
print("Length of the Longest Common Substring :", result)
