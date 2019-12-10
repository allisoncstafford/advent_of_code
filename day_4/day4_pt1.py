
def main():
    """How many different passwords within the range 372304-847060 meet these 
    criteria:
    It is a six-digit number.
    + The value is within the range given in your puzzle input.
    + Two adjacent digits are the same (like 22 in 122345).
    + Going from left to right, the digits never decrease; they only ever 
      increase or stay the same (like 111123 or 135679).
    """
    meet_criteria = [meets_criteria(x) for x in range(372304, 847061)]
    print (sum(meet_criteria))


def meets_criteria(num):
    """boolean test for meeting the password criteria.
    + Two adjacent digits are the same (like 22 in 122345).
    + Going from left to right, the digits never decrease; they only ever 
       increase or stay the same (like 111123 or 135679)

    Arg:
        num: number to be tested

    Return:
        boolean
    """
    output = True
    if not two_same_digits(num):
        output = False
    if not digits_increase(num):
        output = False
    return output


def two_same_digits(num):
    """boolean test for numbers with at least two adjacent digits that are the 
    same.

    Arg:
        num: the number to test.

    Returns:
        boolean
    """
    output = False
    digits = [int(i) for i in str(num)]
    for i, dig in enumerate(digits[:-1]):
        if dig == digits[i + 1]:
            output = True
    return output


def digits_increase(num):
    """boolean test for number whose digits increase from left to right.

    Arg:
        num: the number to test. expecting a six-digit number.

    Returns:
        boolean
    """
    output = True
    digits = [int(i) for i in str(num)]
    for i, dig in enumerate(digits[:-1]):
        if dig > digits[i + 1]:
            output = False
    return output


if __name__ == "__main__":
    main()