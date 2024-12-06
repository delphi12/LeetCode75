def maxSum(inputArr):
    num_jars = len(inputArr)
    if num_jars == 0:
        return 0
    if num_jars == 1:
        return inputArr[0]

    # Initialize the dp array
    dp = [0] * (num_jars + 1)
    dp[1] = inputArr[0]

    for i in range(2, num_jars + 1):
        dp[i] = max(dp[i-1], inputArr[i-1] + dp[i-2])

    return dp[num_jars]

def main():
    inputArr = []
    inputArr_size = 8
    inputArr = [1,7,3,91,12,66,54,60]
    result = maxSum(inputArr)
    print(result)

if __name__ == "__main__":
    main()