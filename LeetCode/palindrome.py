
def isPalindrome(s: str) -> bool:
    # strip and lower the string
    # [::-1] to see if it's the same.

    # do a 2 pointer, ignoring spaces/punctuation and .lower()

    # clean_s = [letter.lower() for letter in s if letter.isalpha() or letter.isnumeric()]

    # if not clean_s:
    #     return True

    # while len(clean_s) > 1:
    #     if clean_s[0] == clean_s[-1]:
    #         clean_s.pop(0)
    #         clean_s.pop()
    #     else:
    #         return False
    # return True

    clean_s = [letter.lower() for letter in s if letter.isalpha() or letter.isnumeric()]

    first = 0
    last = len(clean_s) - 1
    while first <= last:
        if clean_s[first] == clean_s[last]:
            first += 1
            last -= 1
        else:
            return False
    return True