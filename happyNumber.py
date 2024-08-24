def squareHelper(n: int) -> int:
    # replace all digits
    s = str(n)
    sum = 0
    for c in s:
        sum += int(c)*int(c)
    return sum

def isHappy(n: int) -> bool:
    s = set()
    while True:
        if n == 1:
            return True
        else:
            n = squareHelper(n)
            if n in s:
                return False
            s.add(n)

print(isHappy(2))