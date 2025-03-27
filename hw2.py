def exchange(coin):
    five_hundred = coin//500
    coin %= 500

    one_hundred = coin//100
    coin %= 100

    fifty = coin // 50
    coin %= 50

    ten = coin // 10
        
    print("500원 동전의 개수: %d" %five_hundred)
    print("100원 동전의 개수: %d" %one_hundred)
    print("50원 동전의 개수: %d" %fifty)
    print("10원 동전의 개수: %d" %ten)
    
def get_integer(prompt):
    r = int(input(prompt))
    return r

amount = get_integer("동전으로 교환하고자 하는 금액은? ")
exchange(amount)
