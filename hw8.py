def buy(dic):
    
    print("[구입]")
    while True:
        name = input("상품명? ")
        if name == '':
            return 0
        num = int(input("수량은? "))
        dic[name] = num
        print(f"장바구니에 {name} {num}개가 담겼습니다.")

def show(dic):
    print(f">>> 장바구니 보기: {dic}")

def find(dic):
    print("\n[검색]")
    search = input("장바구니에서 확인하고자 하는 상품은? ")
    print(f"{search}은(는) {dic[search]}개 담겨 있습니다.")

shopping_bag = {}
while True:
    if buy(shopping_bag) == False:
        break

show(shopping_bag)
find(shopping_bag)
