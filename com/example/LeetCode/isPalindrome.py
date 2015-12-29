__author__ = 'summer'
def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """

    if x < 0:
        return False
    if x < 10:
        return True

    for n in xrange(11):
        if (x / 10 ** n) >= (10 ** n) and (x / 10 ** (n+1)) < (10 ** (n+1)):
            if (x / 10 ** n)/(10 ** n) >= 10:   #digits is even number
                num_1 = x / (10 ** (n+1))
                num_2 = x % (10 ** (n+1))

            else:
                num_1 = x / (10 ** n)
                num_2 = x % (10 ** (n+1))
            break


    while n >= 0:
        cmp_1 = num_1 / 10 ** n
        cmp_2 = num_2 % 10
        if cmp_1 != cmp_2:
            return False
        num_1 = num_1 % 10 ** n
        num_2 = num_2 / 10
        n -= 1

    return True


print isPalindrome(-2147447412)