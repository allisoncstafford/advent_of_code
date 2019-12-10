from day4_pt1 import digits_increase

def main():
    """How many different passwords within the range 372304-847060 meet these 
    criteria:
    It is a six-digit number.
    + The value is within the range given in your puzzle input.
    + Two adjacent digits are the same (like 22 in 122345) but not part of a 
      larger set of matching digits
    + Going from left to right, the digits never decrease; they only ever 
      increase or stay the same (like 111123 or 135679).
    """
    for num in range(372304, 847061):
        if meets_criteria2(num):
            print (num)

    meet_criteria = [meets_criteria2(x) for x in range(372304, 847061)]
    print (sum(meet_criteria))


def meets_criteria2(num):
    """boolean test for meeting the password criteria.
    + Two adjacent digits are the same (like 22 in 122345), but not part of a 
      larger set of digits
    + Going from left to right, the digits never decrease; they only ever 
       increase or stay the same (like 111123 or 135679)

    Arg:
        num: number to be tested

    Return:
        boolean
    """
    output = True
    if not exactly_two_same_digits(num):
        output = False
    if not digits_increase(num):
        output = False
    return output


def exactly_two_same_digits(num):
    """boolean test for numbers with two adjacent digits that are the same
    and not part of a larger set of repeated digits

    Arg:
        num: the number to test.

    Returns:
        boolean
    """
    output = False
    digits = [int(i) for i in str(num)]
    for i, dig in enumerate(digits[:-2]):
        if i == 0:
            if dig == digits[i + 1] and dig != digits[i + 2]:
                output = True
        else:
            if (dig != digits[i - 1] 
                and dig == digits[i + 1] 
                and dig != digits[i + 2]):
                output = True
            if i == len(digits) - 3:
                if dig != digits[i + 1] and digits[i + 1] == digits[i + 2]:
                    output = True
    return output

if __name__ == "__main__":
    main()