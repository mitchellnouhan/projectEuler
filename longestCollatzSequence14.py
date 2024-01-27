from collections import defaultdict
# we are going to use a hash map to contain collatz sequence lengths to help us calculate this faster
collatz = defaultdict(lambda: 0)

# start with one and increment up
# for each number n, calculate the collatz seq length
# while calculating the collatz seq len for n, any intermediate number in the collatz seq len of n can be added to the hash map:)
# 1, 1
# 2 -> 1(1), 2
# 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 (2), 8
# 4, 3
# 8, 4
# 16, 5
# 5, 6
# 10, 7
# 6 -> 3(8), 9
# 7 -> 22 -> 11 -> 34 -> 17 -> 52 -> 26 -> 13 -> 40 -> 20 -> 10(7), 17
# etc


def calcCollatz(num):
    #print(num)
    #this is a recursive function
    #base case, num is 1
    #if num is already in hashmap, return its length from the hashmap
    if collatz[num]:
        return collatz[num]
    if num == 1:
        return 1
    #if num is eve/odd, call the function on itself
    if num % 2:
        collatz[num] = 1 + calcCollatz(int(3*num + 1))
    else:
        collatz[num] = 1 + calcCollatz(int(num / 2))
    return collatz[num]


# Main block
if __name__ == "__main__":
    startNumMax = 1000000
    maxCollatzNum = 0
    maxCollatzNumLen = 0
    for i in range(1, startNumMax):
        collatz[i] = calcCollatz(i)
        if collatz[i] > maxCollatzNumLen:
            maxCollatzNumLen = collatz[i]
            maxCollatzNum = i
    print(maxCollatzNum, maxCollatzNumLen)