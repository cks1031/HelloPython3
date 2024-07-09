# 실전예제 1


# usermail = input('사용자이메일')
# username = input('사용자이름')
# userid = input('사용자아이디')
# passwd = input('사용자비밀번호')

# print(f'To. {usermail}')
# print('▶ 아이디 및 비밀번호 확인')
# print(f'{username} 고객님 안녕하세요.')
# print(f'{username} 고객님의 아이디와 비밀번호는 아래과 같습니다')
# print(f'아이디 : {userid}')
# print(f'비밀번호 : {passwd}')

usermail = 'gildong@abc.co.kr'
username = '홍길동'
userid = 'gildong'
passwd = 1234

print(f'''To. {usermail}
    ▶ 아이디 및 비밀번호 확인
    {username} 고객님 안녕하세요.
    {username} 고객님의 아이디와 비밀번호는 아래과 같습니다
    아이디 : {userid}
    비밀번호 : {passwd}''')

# 실전예제 2

# day1 = input('요일')
# day2 = input('일자')
# temp1 = input('최저기온')
# temp2 = input('최고기온')
# var1 = input('강수 확률')
# var2 = input('미세먼지')
# am = input('일출시간')
# pm = input('일몰시간')
# var3 = input('남해물결')
# vav4 = input('동해물결')
# var5 = input('서해물결')
#
# print('내일 날씨 예보입니다.')
# print(f'{day1}요일인 {day2}의 아침 최저 기온은 {temp1}도, 낮 최고 기온은 {temp2}도로 예보됐습니다.')
# print(f'비올 확률은 {var1}이고, 미세먼지는 {var2} 수준일 것으로 예상됩니다.')
# print(f'일출 시간은 {am}이고, 일몰 시간은 {pm}입니다.')
# print(f'바다의 물결은 남해 앞바다 {var3}m, 동해 앞바다{vav4}m, 서해 앞바다 {var5}m 높이로 일겠습니다.')
# print(f'지금까지 {day2} {day1}요일 날씨 예보였습니다.')

day = input('요일은?')
date = input('날짜(월일)는? ')
minTemp = input('최저 기온은')
maxTemp = input('최고 기온은')
rain = input('비 올 확률은')
dusty = input('미세먼지는?')
riseSun = input('일출시간은?')
downSun = input('일몰시간은?')
southWave = input('남해 물결 높이는?')
eastWave = input('동해 물결 높이는')
westWave = input('서해 물결 높이는')

print(f'''내일 날씨 예보입니다.
{day}요일인 {date}의 아침 최저 기온은 {minTemp}도, 낮 최고 기온은 {maxTemp}도로 예보됐습니다.
비올 확률은 {rain}이고, 미세먼지는 {dusty} 수준일 것으로 예상됩니다.
일출 시간은 {riseSun}이고, 일몰 시간은 {downSun}입니다.
바다의 물결은 남해 앞바다 {southWave}m, 동해 앞바다{eastWave}m, 서해 앞바다 {westWave}m 높이로 일겠습니다.
지금까지 {date} {day}요일 날씨 예보였습니다.''')

# 영수증 예제

# exvar1 = input('술') # 술
# exvar2 = input('안주') # 안주
# exvar1a = input('술가격') # 술 가격
# exvar2a = input('안주가격') # 안주 가격
# exvar3 = (int(exvar1a) + int(exvar2a)) * 0.9 # 과세합계
# exvar4 = (int(exvar1a) + int(exvar2a)) * 0.1 # 부가세
# exvar5 = int(exvar1a) + int(exvar2a) # 총합계
# exvar6 = input("받은금액") # 받은 금액
# exvar7 = int(exvar6)-int(exvar5) # 잔돈
# date = input('날짜') # 날짜1
#
# print('[ 음식나라 ]')
# print('---------------------------')
# print(f'  {exvar1}    2    {exvar1a}')
# print(f'{exvar2}    1    {exvar2a}')
# print('---------------------------')
# print(f'과세합계            {exvar3}')
# print(f'부가세              {exvar4}')
# print('---------------------------')
# print(f'총합계              {exvar5}')
# print(f'받은금액             {exvar6}')
# print(f'잔돈                {exvar7}')
# print('---------------------------')
print(date)
# 3
rate1 = 123
# 1stPlayer =456
# myprograming.jave = 789
long = 987
# except = 654
TimeLimit = 321
numberOfWindows = 10000

# 11 - 이름, 몸무게, 나이를 변수로 선언하고 초기화
name = '일지매'
weight = 45.5
age = 35

print(name,weight,age)

# 12 - 생년월일 계산
# 년나이 계산 : 현재년도 - 태어난년도 ( 병역법, 교육법, 민방위)
# 만나이 : 현재년도 - 태어난년도 , 생일안지남 (-1) (민법상, 2023-06부터)
# 한국식 나이 : 현재년도 - 태어난녀도 + 1
currentYear = int(input('현재 년도는?'))
birthTear = int(input('생일의 년도'))
myAge = currentYear - birthTear

print(f'''현재년도는 {currentYear}이고, 
생일의 년도가 {birthTear}일 때,
나이는 {myAge} 입니다.''')

# 13 구구단 출력

# print('7 x 1 = 7')
# print('7 x 2 = 14')
# print('7 x 3 = 21')
# print('7 x 4 = 28')
# print('7 x 5 = 35')
# print('7 x 6 = 42')
# print('7 x 7 = 49')
# print('7 x 8 = 56')
# print('7 x 9 = 63')

dan = 7
print(f'''{dan} x 1 = {dan * 1}
{dan} x 2 = {dan * 2}
{dan} x 3 = {dan * 3}
{dan} x 4 = {dan * 4}
{dan} x 5 = {dan * 5}
{dan} x 6 = {dan * 6}
{dan} x 7 = {dan * 7}
{dan} x 8 = {dan * 8}
{dan} x 9 = {dan * 9}''')

dan = int(input('단수'))
for i in range(1,10):
print(dan, '*', i,'=' , dan*i)

