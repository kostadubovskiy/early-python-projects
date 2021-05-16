def get_base_number(num, base):
    '''get_base_number(num,base) -> int
    returns value of num as a base number in the given base'''
    # you have to fill in the rest
    num = list(num)
    num.reverse()

    for e in range(0, len(num)):
        num[e] = int(num[e])

    result = 0
    for ind in range(len(num)):
        i = num[ind]
        result = result + i * (base ** ind)

    return result


# test cases
print(get_base_number('10011', 2))  # should be 19
print(get_base_number('3202', 5))   # should be 427
print(get_base_number('22', 3))  # should be 19
print(get_base_number('611023', 7))