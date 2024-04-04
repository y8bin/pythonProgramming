def get_fixed_price(rate, price):
    before_price = price / (1 - rate / 100)
    return before_price
    
def main():
    discount_rate = int(input("할인율은? "))
    after_priceA = int(input("A 상품의 할인된 가격은? "))
    after_priceB = int(input("B 상품의 할인된 가격은? "))

    before_priceA = get_fixed_price(discount_rate, after_priceA)
    before_priceB = get_fixed_price(discount_rate, after_priceB)

    print("A 상품의 정가는", before_priceA, "원")
    print("B 상품의 정가는", before_priceB, "원")

if __name__ == '__main__':
    main()
