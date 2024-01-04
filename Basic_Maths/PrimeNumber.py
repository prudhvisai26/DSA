def isPrime(n):
    for i in range(2,int(n**1/2)):
        if n % i == 0:
            return False
    return True