primes = [2]
num = 3
curPrime = 2
counter = 1
while curPrime < 2000000:
    primeFlag = True
    for prime in primes:
        if num % prime == 0:
            primeFlag = False
            break
    if primeFlag:
        primes.append(num)
        counter += 1
        curPrime = num
    num += 1
primes.pop()
print(sum(primes))