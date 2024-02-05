def getPrimeNumbers(n):
    primeList = []
    for x in range (2, n+1):
        check = True
        for j in range(2, int(x**0.5) + 1):
            if x % j == 0:
               check = False
        if check == True:
            primeList.append(x)
    
    return primeList


print(getPrimeNumbers(99))