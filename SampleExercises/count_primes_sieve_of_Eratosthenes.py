def countPrimes(n):
    if n<=2: return 0
    composites= [False]*(n+1)
    limit = int(n**0.5)

    for i in range(2, limit+1):
        if not composites[i]:
            for j in range(i*i, n+1, i):
                composites[j] = True

    count = 0
    for i in range(2, n+1):
        if not composites[i]:
            count+=1

    for i in range(n-1, 1, -1):
        if not composites[i]:
            print("Largest Prime number: ", i)
            break

    return count



n=1000000
print("Count of Primes: ",countPrimes(n))