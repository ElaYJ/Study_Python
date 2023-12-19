g1price = 1200; g2price = 1000; g3price = 800
g4price = 2000; g5price = 900

def formatedNumber(n):
    return format(n, ',')

def calculate(*gcs): # *gcs(goods counts) : 반복이 가능한 자료형

    gcsDic = {} # 정상 입력된 상품
    againCntInput = {} # 미결제 상품

    for idx, gc in enumerate(gcs):
        try:
            gcsDic[f'g{idx+1}'] = int(gc)
        except Exception as e:
            againCntInput[f'g{idx+1}'] = gc
            print(e)

    totalPrice = 0
    for g in gcsDic.keys():
        # globals() 함수를 통해 g1price, g2price, g3price, g4price, g5price 변수를 사용할 수 있다.
        # f'{g}price'가 변수명으로 치환된다.
        print(f'globals()[{g}price]: {globals()[f'{g}price']}')
        totalPrice += globals()[f'{g}price'] * gcsDic[g]

    print('-----------------------------')
    print(f' 총 구매 금액: {formatedNumber(totalPrice)}원')
    print('-------- 미결제 항목 --------')
    for g in againCntInput.keys():
        print(f' 상품: {g},\t 구매 개수: {againCntInput[g]}')
    print('-----------------------------')


def myCalculate(*goods_cnts):
    print(type(goods_cnts))

    goods_cnt_dic = {} # 정상 입력된 상품
    wrong_cnt_dic = {} # 미결제 상품

    for idx, gc in enumerate(goods_cnts):
        try:
            goods_cnt_dic[f'g{idx + 1}'] = int(gc)
        except Exception as e:
            wrong_cnt_dic[f'g{idx + 1}'] = gc
            print(e)

    totalPrice = 0
    for g_no, g_cnt in goods_cnt_dic.items():
        print(g_no, type(g_no), g_cnt, type(g_cnt))
        totalPrice += globals()[f'{g_no}price'] * g_cnt

    print('-----------------------------')
    print(f' 총 구매 금액: {formatedNumber(totalPrice)}원')
    print('-------- 미결제 항목 --------')
    for g, wcnt in wrong_cnt_dic.items():
        print(f' 상품: {g},\t 구매 개수: {wcnt}')
    print('-----------------------------')
