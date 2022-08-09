def calculator(n, m, li):
    newLi = []

    counter = 0
    sumOfItem = 0
    while (counter < n):
        if (m >= len(li)):
            m = len(li)
        for i in range(0, m):
            sumOfItem += li[i]
            counter += 1
        newLi.append(sumOfItem)
        sumOfItem = 0
        del li[:m]
    
    result = 0
    for i in range(0, len(newLi)):
        if (i % 2 == 0):
            number = newLi[i]
        else:
            number = -newLi[i]
        result += number
    
    return result
    

print(calculator(8, 1, [1, 2, 3, 4, 5, 6, 7, 8]))
