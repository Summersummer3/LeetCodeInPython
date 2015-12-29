__author__ = 'summer'
import string

def myAtoi(str):
    """
    :type str: str
    :rtype: int
    """
    if str == "":
        return 0

    INT_MAX = 2147483647
    INT_MIN = -2147483648
    i = 0
    flag = 0
    number = None
    number_list = ["0","1","2","3","4","5","6","7","8","9"]

    while str[0] == " ":
        str = str[1:]


    if str[0] == "-" or str[0] == "+":
        if str[0] == "-":
            flag = -1
        str = str[1:]
        if len(str) == 0:
            return 0


    while i < len(str):
        if str[i] in number_list:
            i += 1
        else:
            if i == 0:
                return 0
            number = int(str[0:i])
            break

    if number == 0:
        return 0

    if not number:
        number = int(str)

    if number >= -INT_MIN:
        if flag == -1:
            return INT_MIN
        return INT_MAX
    if flag == -1:
        return -number
    return number


print myAtoi("     +0a32")
print string.atoi(" 023a", )  # not useful!
