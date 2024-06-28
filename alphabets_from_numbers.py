"""
num = 1123

possible word combination: aabc, kbc, kw, alc, aaw
"""
def num_to_words(num):
    num_str = str(num)
    n = len(num_str)

    if n == 0 or num_str[0] == '0':
        return []

    # Initialize dp arrays
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1 if num_str[0] != '0' else 0

    decode_ways = [[] for _ in range(n + 1)]
    decode_ways[0] = [""]
    if num_str[0] != '0':
        decode_ways[1] = [chr(int(num_str[0]) - 1 + ord('a'))]

    for i in range(2, n + 1):
        one_digit = int(num_str[i-1:i])
        two_digits = int(num_str[i-2:i])

        if 1 <= one_digit <= 9:
            dp[i] += dp[i-1]
            for way in decode_ways[i-1]:
                decode_ways[i].append(way + chr(one_digit - 1 + ord('a')))

        if 10 <= two_digits <= 26:
            dp[i] += dp[i-2]
            for way in decode_ways[i-2]:
                decode_ways[i].append(way + chr(two_digits - 1 + ord('a')))
        #print(decode_ways)

    return decode_ways[n]

num = 1123

word_combinations = num_to_words(num)
print(word_combinations)

