# 조건문
# 주어진 상황에 따라 적절한 명령문을 수행하는 문장
# 프로그래밍에서 조건을 판단하여
# 해당 조건에 맞는 상황을 수행하는데 사용됨
# 파이썬에서 조건문 작성 시 반드시 들여쓰기를 사용함을 명심

# 파이썬의 코드 블록
# 특정한 동작을 위해 관련된 코드를 한 곳에 모아둔 것
# 이러한 코드들은 반드시 같은 들여쓰기 내에 존재해야 함!

# if 문
# if 조건식:
#    조건 참일때 수행할 문장(들)

# 짝수 판별하기
num = int(input('숫자는?'))

if num % 2 == 0:
    print('짝수입니다.')
# if num % 2 == 0: print('짝수입니다.') # 코드 간략화

# if ~ else
# if문은 조건이 참일 경우에만 지정한 코드를 실행하는데
# if ~ else문은 조건이 참일 때와 거짓일 때 각각 지정한 코드를
# 실행한다는 것이 다름
# if 조건식:
#   수행 할 문장1
# else:
#   수행 할 문장2

# 짝수/홀수 출력프로그램
num = int(input('숫자는?'))

if num % 2 == 0:
    print('짝수입니다.')
else:
    [print('홀수입니다.')]

# pass
# 조건문/반복문/함수/클래스나 다른 문 등등에서
# 실행문이 정해지지 않은 경우 임시로 작성하는 명령문

if num % 2 == 0:
    pass
else:
    pass

# 마일리지 사용하기
mileage = 1200
#
# if mileage >=1000:
#         print('마일리지 사용가능')
# else:
#         print('마일리지 사용불가')

# result = ''
# if mileage >=1000:
#         result = '마일리지 사용가능'
# else:
#         result = '마일리지 사용불가'
# print(result)

result = '마일리지 사용불가'
if mileage >=1000:
    result = '마일리지 사용가능'
print(result)

# 중첩 if 문
# if문 속에 또 다른 if 문을 포함시켜 작성하는 조건문
# 조건문을 중첩할 떄는 들여쓰기에 유의해야 함
# 다양한 조건에 따라 결과를 처리하고 싶을 때 사용 - 복잡함

# 평균 점수에 따라 ABCDF 학절을 처리하는 조건문 작성
avg = 73.5

grade = 'F'
if avg >= 90:
    grade = 'A'
else:
    if avg >= 80:
        grade = 'B'
    else:
        if avg >= 70:
            grade = 'C'
        else:
            if avg >= 60:
                grade = 'D'
print(grade)

# 다중 if 문
# 중첩 if문을 작성하는 경우 조건이 많으면 다소 복잡함
# 이런한 중첩 if문을 단순하게 작성할 수 있는 조건문
# if 조건1:
#   실행 할 코드1
# elif 조건2:
#   실행 할 코드2
# elif 조건3:
#   실행 할 코드3
# else:
#   실행 할 코드 4

avg = 85.5

grade = 'F'
if avg >= 90:
    grade = 'A'
elif avg >= 80:
    grade = 'B'
elif avg >= 70:
    grade = 'C'
elif avg >= 60:
    grade = 'D'

print(grade)

# if 조건문 대체 1 - switch 모방
# 조건이 많아지는 경우, 다중 조건문 역시 복잡해 짐
# 이럴 경우, dict 자료 구조를 이용하면 간단하게 작성 가능

# if 조건문 대체 2
# py 3.10부터 switch와 비슷한 match ~ case 문 도입
# match 값:
#   case 값범위1: 실행문1
#   case 값범위2: 실행문2
#   default: 실행문3

# 주민번호 성별코드에 따른 성별 출력
# 1: 남자 (2000년 이전 출생)
# 2: 여자 (2000년 이전 출생)
# 3: 남자 (2000년 이후 출생)
# 4: 여자 (2000년 이후 출생)

code = int(input('성별 코드는?'))

result = ''
match code:
    case 1: result = '남자 (2000년 이전 출생)'
    case 2: result = '여자 (2000년 이전 출생)'
    case 3: result = '남자 (2000년 이후 출생)'
    case 4: result = '여자 (2000년 이후 출생)'
    case _: result = '외국인이군요!'
print(result)

# 다중 if 문으로 작성한 학점계산 코드를
# match case로 바꿔 작성해보세요
# avg = int(input('점수?'))
# match avg:
#     case 90|91|92|93|94|95|96|97|98|99|100: result = 'A'
#     case 89|88|87|86|85|84|83|82|81|80: result = 'B'
#     case 79|78|77|76|75|74|73|72|71|70: result = 'C'
#     case 69|68|67|66|65|64|63|62|61|60: result = 'D'
#     case _: result = 'F'
# print(result)

avg = int(input('점수?'))
match int(avg/10):
    case 10 | 9: result = 'A'
    case 8: result = 'B'
    case 7: result = 'C'
    case 6: result = 'D'
    case _: result = 'F'
print(result)

# 속도 위반 경고

# speed = int(input('속도'))
#
# warn = ''
# if speed > 50:
#     warn = '속도위반!!'
# print(warn)
#

speed = int(input('속도'))

result = '속도위반'
if speed < 50:
    result = '>>>'
print(result)

# 자동온도 조절 장치
temp = int(input('기계 온도'))
result = '팬(Fan) 중지'
if temp >= 40:
    result = '팬(Fan) 가동'
print(f'''
기계 온도를 입력하세요. {temp}
{result}
''')

# 자동 주문 시스템
menuIntro = '''
Good morning. Nice to meet you.
Where are you from?
Please select a number
1.대한민국 2.USA 3.中國
'''
msg = 'Would you like to order?'
menu = int(input(menuIntro))

if menu == 1:
    msg = '주문하시겠어요?'
elif menu == 3:
    msg = '중국어??'
print(msg)


order = int(input('다국어 번호입력'))
match order:
    case 1: lang = '주문하시겠어요?'
    case 2: lang = 'Would you like to order?'
    case 3: lang = '중국어!!'
    case _: lang = 'Would you like to order?'
print(f'''
Good morning. Nice to meet you.
Where are you from?
Please select a number
1.대한민국 2.USA 3.中國 {order}
{lang}
''')

# 국가 재난지원금 수령액 조회
family = int(input('가구 인원수를 입력하세요 : '))
result = ''

result = '1,000,000 원 지원'
if family == 1:
    result = '400,000원 지원'
elif family == 2:
    result = '600,000원 지원'
elif family == 3:
    result = '800,000원 지원'
print(result)

people = int(input('가구 인원수'))
match people:
    case 1: money = '400,000'
    case 2: money = '600,000'
    case 3: money = '800,000'
    case _: money = '1,000,000'
print(f'''
인원수를 입력하세요. {people}
{money}원 지원
''')

# 개선 BMI 지수 출력
bmi = float(input('BMI 지수 입력'))
result = '저체중'
if bmi > 140: result = '고도비만'
elif bmi > 120: result = '비만'
elif bmi > 110: result = '과체중'
elif bmi > 90: result = '정상체중'
print(f'BMI 지수 : {bmi}, 진단결과 : {result} 입니다.')

bmi = float(input('BMI 지수 입력'))
result = '고도비만'
if bmi <= 90: result = '저체중'
elif bmi <= 110: result = '정상 체중'
elif bmi <= 120: result = '과체중'
elif bmi <= 140: result = '비만'
print(result)

# 버스 전용차로 단속
msg1 = '''1. 월~금, 2.토요일, 3.공휴일
요일을 선택하세요 : '''
msg2 = '''
버스 전용차로 단속 중입니다
1.버스 2.승용차
차종을 선택하세요 : '''
msg3 = '버스 전용차로 위반!'
msg4 = '버스입니다.'
msg5 = '토요일 및 공휴일은 단속하지 않습니다'

dayweek = int(input(msg1))
result = ''
if dayweek == 1: # 평일여부 확인
    cartype = int(input(msg2))
    if cartype != 1:
        result = msg3
    else:
        result = msg4
else:
    result = msg5
print(result)

# 마스크 구매 가능 요일
endBirthYear =int(input('출생연도 끝자리 입력 : '))
age = int(input('만 나이 입력 : '))
result = '언제든지 구매 가능합니다.'

# if age < 65:
# if endBirthYear == 1 or endBirthYear == 6:
#     result = '월요일 구매 가능합니다.'
# elif endBirthYear == 2 or endBirthYear == 7:
#     result = '화요일 구매 가능합니다.'
# elif endBirthYear == 3 or endBirthYear == 8:
#     result = '수요일 구매 가능합니다.'
# elif endBirthYear == 4 or endBirthYear == 9:
#     result = '목요일 구매 가능합니다.'
# elif endBirthYear == 5 or endBirthYear == 0:
#     result = '금요일 구매 가능합니다.'
if age < 65:
    match endBirthYear:
        case 1 | 6:
            result = '월요일 구매 가능합니다.'
        case 2 | 7:
            result = '화요일 구매 가능합니다.'
        case 3 | 8:
            result = '수요일 구매 가능합니다.'
        case 4 | 9:
            result = '목요일 구매 가능합니다.'
        case 5 | 0:
            result = '금요일 구매 가능합니다.'
print(result)

# 차량 2부제
from datetime import datetime
# day = int(input('오늘은 몇 일? '))
day = datetime.today().day
carNum = int(input('차량번호 4자리는? '))

msg1 = '오늘 입차 : 번호가 홀수인 차량'
msg2 = '귀하의 차량은 입차 불가합니다.'
if day % 2 == 0:
    msg1 = '오늘 입차 : 번호가 짝수인 차량'

if day % 2 == carNum % 2:
    msg2 = '귀하의 차량은 입차 가능합니다.'

print(f'''오늘 날짜 : {day}
{msg1}
{msg2}''')

# 생존율 출력
msg = ('최초 장비를 사용하기까지 걸린 시간(초)을 입력하세요.')
time = int(input(msg))

result = '25%'
if time <= 60: result = '85%'
elif time <= 120: result = '76%'
elif time <= 180: result = '66%'
elif time <= 240: result = '57%'
elif time <= 300: result = '47%'
elif time <= 360: result = '35%'

print(result)

# 전기 요금 계산기
basePrice = 910  # 기본요금
unitPrice = 99.3  # 단가
powerPrice = 0 # 전기요금

powerAmount = int(input('전기 사용량은은?'))

if powerAmount > 400:
    basePrice = 7300
    unitPrice = 280.6
elif powerAmount > 200:
    basePrice = 1600
    unitPrice = 187.9

powerPrice = basePrice + (unitPrice * powerAmount)

print(f'''
사용량 : {powerAmount} kwh
기본요금 : {basePrice:,} 원
단가 : {unitPrice:,} 원
전기 요금 : {powerPrice}원''')