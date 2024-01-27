import math

counter = 1
triNum = 0
factorsLen = 0
while factorsLen <= 500:
    factorsLen = 0
    triNum += counter
    counter += 1
    start = 1
    end = int(math.ceil(math.sqrt(triNum)))
    for i in range(start, end):
        if triNum % i == 0:
            factorsLen += 2
print(triNum)
