def isHappy(n: int) -> bool:
    seen = []
    return isHappyHelper(n, seen)

def isHappyHelper(n, seen):
    if n == 1:
        return True
    
    str_n = str(n)
    new_n = 0
    for number in str_n:
        new_n += int(number) ** 2
    if new_n in seen:
        return False
    seen.append(new_n)
    return isHappyHelper(new_n, seen)

# second solution after looking at others
def is_happy(n):
    seen = set()
    while n != 1:
        if n in seen:
            return False
        seen.add(n)
        str_n = str(n)
        new_n = sum([int(number)**2 for number in str_n])
        n = new_n
    return True

print(is_happy(2))
        
