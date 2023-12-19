def calculatorTotalPrice(goods):

    if len(goods) <= 0:
        print('구매 상품이 없습니다.')
        return

    rate = 25
    totalPrice = 0

    # 구매 개수에 따른 할인율을 담은 Dictionary
    rates = {1:5, 2:10, 3:15, 4:20}

    # 5개 미만인 경우
    if len(goods) in rates:
        rate = rates[len(goods)]

    # 5개 이상인 경우
    for g in goods:
        totalPrice += g * (1 - rate * 0.01)

    return [rate, int(totalPrice)]


def formatedNumber(n):
    return format(n, ',')