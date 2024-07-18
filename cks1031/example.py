products = {'쌀': 9900, '상추': 1900, '고추': 2900, '마늘': 8900,
            '통닭': 5600, '햄': 6900, '치즈': 3900}

# 단위 환산
# (convertUnit/readUnit/printUnits)

def readUnit():
    mm = int(input('길이(mm)를 입력하세요: '))
    return mm

def convertUnit(mm):
    units = [mm]
    units.append(mm * 0.1)
    units.append(mm * 0.001)
    units.append(mm * 0.03937)
    units.append(mm * 0.003281)
    return units

def printUnits(untis):
    print(f'''
    {untis[0]} mm --> {untis[1]} cm  
    {untis[0]} mm --> {untis[2]} m
    {untis[0]} mm --> {untis[3]} inch  
    {untis[0]} mm --> {untis[4]} ft
    ''')

# 할인된 상품 가격표 출력
# (discountPrice/readDiscount/printPrices)

def readDiscount():
    print('''
    ----------------------------------
    -- 한빛 마트 오늘의 할인 가격표 출력 --
     ----------------------------------
     ''', end='')
    rate = int(input('오늘의 할인율은?'))
    return rate


def discountPrice(rate):
    dcprice = []
    dc = ( 1- (rate / 100))
    for v in products.values():
        dcprice.append( v * dc )
    return dcprice

def printPrices(dcpirce, rate):
    result = ''
    for idx, k in enumerate(products):
        result += f'{k:4s} : {products[k]:,d} 원 {rate} % DC -> {dcpirce[idx]:,.0f} 원\n'
    print(result)

def checkJumin(jumin):
    result = '주민번호 불일치'
    sum = 0
    weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    for i in range(12):
        sum += int(jumin[i]) * weight[i]

    checker = (11 - (sum % 11)) % 10
    if checker == int(jumin[12]): result = '주민번호 유효!'

    return result