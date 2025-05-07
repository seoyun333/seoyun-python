shopping_bag = {}

print("[구입]")
while True:
    item = input("상품명? ")
    
    if item == "":
        break

    count = int(input("수량은? "))

    if item in shopping_bag:
        shopping_bag[item] += count
    else:
        shopping_bag[item] = count


    print(f"장바구니에 {item} {count}개가 담겼습니다.\n")

print(">>> 장바구니 보기:")
for item, count in shopping_bag.items():
    print(f"{item}: {count}개")


print("\n[검색]")
search = input("장바구니에서 확인하고자 하는 상품은? ")
print()

if search in shopping_bag:
    print(f"{search}는(은) {shopping_bag[search]}개 담겨 있습니다.")
else:
    print(f"{search}는(은) 장바구니에 없습니다.")
