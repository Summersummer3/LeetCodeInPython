__author__ = 'summer'
def calculate(s):
    """
    :type s: str
    :rtype: int
    """
    arr = []
    cal_stack = []
    num = 0
    flag = 0
    j = 0

    for i in s:
        if i != "+" and i != "-" and i != "*" and i != "/":
            if i == " ":
                continue

            if num == 0:
                num = int(i)
            else:
                num = num * 10 + int(i)
        else:
            arr.append(str(num))
            arr.append(i)
            num = 0

    arr.append(str(num))

    print arr

    while j<len(arr):
        cal_stack.append(arr[j])

        if arr[j] == "*":
            cal_stack.pop()
            num1 = int(cal_stack.pop())
            j += 1
            num2 = int(arr[j])
            num3 = num1 * num2
            cal_stack.append(str(num3))

        if arr[j] == "/":
            cal_stack.pop()
            num1 = int(cal_stack.pop())
            j += 1
            num2 = int(arr[j])
            num3 = num1 / num2
            cal_stack.append(str(num3))

        j += 1
        print cal_stack

    cal_stack.reverse()

    while len(cal_stack)!= 1:
        num1 = int(cal_stack.pop())
        symbol = cal_stack.pop()
        num2 = int(cal_stack.pop())
        if symbol == "+":
            num3 = num1 + num2
        else:
            num3 = num1 - num2
        cal_stack.append(str(num3))

    return int(cal_stack[0])

s = "0-1+1"

print calculate(s)







