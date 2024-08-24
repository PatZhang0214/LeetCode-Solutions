
cache = {1: 1, 2: 2}

def climbStairs(n: int) -> int:
    # We know that
    '''
    for n = 1:
    1. 1 step

    for n = 2:
    1. 1 + 1 step
    2. 2 step

    for n = 3:
    1. 1 + 1 + 1 step
    2. 2 + 1 step
    3. 1 + 2 step

    for n = 4:
    1. 1 + 1 + 1 + 1 step
    2. 2 + 1 + 1 step
    3. 1 + 2 + 1 step
    4. 1 + 1 + 2 step
    5. 2 + 2 step

    we see that n = 3
    FOR ALL x in (n = 2), (n = 2) + 1
    FOR ALL y in (n = 1), (n = 1) + 2

    we see that n = 4
    FOR ALL x in (n = 3), (n = 3) + 1
    FOR ALL y in (n = 2), (n = 2) + 2

    general formula in induction notation:

    Wait this is literally fibonacci
    '''

    if n == 1:
        return cache[1]
    elif n == 2:
        return cache[2]
    else:
        # first check if cache contains n - 1 and n - 2
        # only call recursively if cache doesn't contain them
        if n-1 in cache:
            cache[n] = cache[n-1] + cache[n-2]
            return cache[n]
        else:
            # if n-1 is not in cache
            # normal recursion
            return climbStairs(n - 1) + climbStairs(n - 2)

print(climbStairs(35))