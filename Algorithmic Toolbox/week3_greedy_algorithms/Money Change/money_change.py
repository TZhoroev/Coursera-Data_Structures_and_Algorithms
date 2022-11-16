# python3
def money_change(money):
    q1, money = divmod(money, 10)
    q2, money = divmod(money, 5)
    return q1 + q2 + money


if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
