# 연산자
# 수식/표현식 expression
# 숫자, 변수, 연산자를 이용해서 수학적 관계를 나타내는 것
# 연산의 결과로 하나의 값이 되거나
# 특정 기능의 수행을 나타내는 표현들
# 수식 -> 피연산자와 연산자로 구성
# 연산자 : 연산의 의미를 지닌 기호
# 피연산자 : 연산의 대상들을 의미

# 산술연산자

# 자료형 승격(promotion)

# 매출액 입력 시 총합을 출력

sale1 = int(input('1월 매출'))
sale2 = int(input('2월 매출'))
sale3 = int(input('3월 매출'))
totalsale = sale1 + sale2 + sale3

# pay1 = input('1월 매출')
# pay2 = input('2월 매출')
# pay3 = input('3월 매출')
# value = int(pay1) + int(pay2) + int(pay3)

print(f'''
 1월 매출 : {sale1}
 2월 매출 : {sale2}
 3월 매출 : {sale3}
 1분기 매출 : {totalsale}
 ''')
#
# 1분기 수익 계산
pay1 = int(input('1월 매출'))
pay2 = int(input('1월 매입'))
value = pay1 - pay2

print(f'''
1분기 매출 : {pay1}
1분기 매입 : {pay2}
1분기 수익 : {value}
''')

# 방의 넓이 구하기

width = int(input('가로 길이'))
length = int(input('세로 길이'))
area = width * length

print(f'''
가로 길이 : {width}
세로 길이 : {length}
넓이 : {area}c㎠
''')

# 신체지량지수BMI 구하기
weight = float(input('몸무게'))
tall = float(input('신장'))
bmi = weight / (tall * tall)
print(f'''
몸무게(kg) : {weight}
신장(m) : {tall}
BMI : {int(bmi)}
''')

# 홀짝 게임

coin = input('동전 개수')
result = int(coin) % 2

print(f'''
손 안에 동전 수를 입력하세요. {coin}
{result}  
''')
# 빵 나누기

breads = 97
divsor = 3
studs = 97 // 3
mods = 97 % 3

print(f'''
빵을 나누어 줄 수 있는 학생 수 : {studs}
남는 빵 개수 {mods}  
''')

# 전영병 예상 감염자 구하기
# 1일차 -> 2명 / 2일차 -> 4명 / 3일차 -> 8명 / 4일차 -> 16명 / n일차 -> 2 ** n명

infectors = 2 ** 30

print(f'30일 이후 예상 감염자 수 : {infectors}')


