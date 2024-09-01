def summ(num1, num2):
    return num1 + num2


def div(num1, num2):
    if num2 == 0:
        return "can not div by 0"
    else:
        return num1 / num2


if __name__ == '__main__':
    print(summ(17, 18))
    print(div(5, 6))
