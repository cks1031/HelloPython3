# 4
x = 1; y = 2; z = 3

s0 = 1; v0 = 2; t = 3; g = 9.8

a = 3 * x
b = 3 * x + y
c = (x + y) / 7
d = ( 3 * x + y ) / (z + 2)
e = s0 + v0 * t + (1/2 * g * t ** 2) # 등가속도 공식

print(a,b,c,d,e)

# 5 ~ 10

# 12
# 만나이 : 현재년도 - 태어난년도, 생일 안지남 (-1) (민법상, 2023-06부터)

currentYear = int(input('현재 년도는?'))
birthTear = int(input('생일의 년도'))
isPass = bool(input('생일 지남 여부는? (True/False)'))
myAge = currentYear - birthTear
# myAge = myAge if (isPass == True) else (myAge - 1)
myAge if isPass else (myAge - 1)

print(f'''현재년도는 {currentYear}이고,
생일의 년도가 {birthTear}일 때,
나이는 {myAge}세 입니다.''')


# 14
day = 86400 # 하루 - 초
hour = 3600 # 시간 - 초
minute = 60 # 분 -초
days = 1234567890 /day
hours = 98765 / hour
minutes = 12345 / minute

print(f'''
{int(days):,} 일
{int(hours):,} 시간
{int(minutes):,} 분
''')


# 16 (!!)

# money = int(input('잔돈'))
price = 34_560
paid = 50_000
charge = paid - price

w50000 = charge / 50000         # 결과는 float
# w50000 = int(charge // 50000)   # 결과를 정수형으로 변환
w50000 = charge // 50000        # 파이썬의 몫 연산자
w10000 = charge // 10000
w10000 = charge - (10000 * w10000)
# charge %= 10000
charge = charge - (10000 * w10000)
w5000 = charge // 5000
charge = charge - (5000 * w5000)
w1000 = charge // 1000
charge = charge - (1000 * w1000)
w500 = charge // 500
charge = charge - (500 * w500)
w100 = charge // 100
charge = charge - (100 * w100)
w50 = charge // 50
charge = charge - (50 * w50)
w10 = charge // 10
charge = charge - (10 * w10)

# charge %= 50000
# charge %= 10000
# charge %= 5000
# charge %= 1000
# charge %= 500
# charge %= 100
# charge %= 50
# charge %= 10

print(f'''
금액 : {price:,} 원
지불금액 : {paid:,} 원
잔돈 : {paid - price:,} 원
----------------
50000원 : {w50000} 장
10000원 : {w10000} 장
5000원 : {w5000} 장
1000원 : {w1000} 장
500원 : {w500} 개
100원 : {w100} 개
50원 : {w50} 개
10원 : {w10} 개
''')