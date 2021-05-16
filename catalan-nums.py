catalanNums = [1, 1]


def catalan(n):
    '''
    cn = c0cn-1 + c1cn-2 + c2cn-3 + ... + cn-1c0
    '''
    while len(catalanNums) != n:
        next = 0

        for i in range(0, len(catalanNums)):
            next += catalanNums[i]*catalanNums[len(catalanNums)-i-1]
        print(next)

        catalanNums.append(next)


catalan(31)
print(catalanNums[30])

