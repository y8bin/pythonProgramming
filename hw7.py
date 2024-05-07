bag = {}

print("[구입]")
while True:
    name = input("상품명? ")
    if name == '':
        break
    
    num = input("수량은? ")

    bag[name] = num
    print(f"장바구니에 {name} {num}개가 담겼습니다.")

print(f">>> 장바구니 보기: {bag}")

print("\n[검색]")
search = input("장바구니에서 확인하고자 하는 상품은? ")
if search in bag:
    print(f"{search}은(는) {bag[search]}개 담겨 있습니다.")
else:
    print(f"{search}은(는) 장바구니에 없습니다.")
