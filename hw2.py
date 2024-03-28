def get_integer(a):
    return int(input(a))

def exchange(amount):
    c500 = amount // 500
    amount %= 500

    c100 = amount // 100
    amount %= 100

    c50 = amount // 50
    amount %= 50

    c10 = amount // 10
    amount %= 10

    print("500원 동전의 개수:", c500)
    print("100원 동전의 개수:", c100)
    print("50원 동전의 개수:", c50)
    print("10원 동전의 개수:", c10)

coin = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(coin)
