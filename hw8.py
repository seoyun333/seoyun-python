shopping_bag = {}

while True:
    print("[구입]")
    item = input("상품명? ")
    
    if item == "":
        break

    count = int(input("수량은? "))

    if item in shopping_bag:
        shopping_bag[item] += count
    else:
        shopping_bag[item] = count


    print(f"장바구니에 {item} {count}개가 담겼습니다.\n")

print("\n>>> 장바구니 보기:", end=" ")
print(shopping_bag)


print("\n[검색]")
search = input("장바구니에서 확인하고자 하는 상품은? ")

if search in shopping_bag:
    print(f"{search}은(는) {shopping_bag[search]}개 담겨 있습니다.")
else:
    print(f"{search}은(는) 장바구니에 없습니다.")
