def get_fixed_price(price, rate):
    regular_price = int(price*100/(100-rate))
    return regular_price

rate = int(input("할인율은? "))
A_price = int(input("A 상품의 할인된 가격은? "))
B_price = int(input("B 상품의 할인된 가격은? "))
print("A 상품의 정가는",get_fixed_price(A_price, rate),"원")
print("B 상품의 정가는",get_fixed_price(B_price, rate),"원")

