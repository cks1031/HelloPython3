#----------------------------------------------------------------
def displayMenu():
    main_menu =f'''
===========================
    성적 프로그램 v6
===========================
    1. 성적 데이터 추가
    2. 성적 데이터 조회
    3. 성적 데이터 상세조회
    4. 성적 데이터 수정
    5. 성적 데이터 삭제
    0. 성적 프로그램 조회
===========================
'''
    print(main_menu, end='')
    menu = input('=> 메뉴를 선택하세요 : ')
    return menu

#  성적 데이터 관련 변수 선언
sjs = []

# 성적 데이터를 입력 받는 함수
def readSungJuk():
    sj = []
    cnt = len(sjs)
    sj.append(input(f'{cnt}학생 이름은?'))
    sj.append(int(input(f'{cnt}국어 점수는?')))
    sj.append(int(input(f'{cnt}영어 점수는?')))
    sj.append(int(input(f'{cnt}수학 점수는?')))
    return sj

# 입력받은 성적 데이터를 처리하고 리스트에 저장
def addSungJuk(sj):
    sj.append(sj[1] + sj[2] + sj[3])
    sj.append(sj[4] / 3)
    grd = '수' if (sj[5] >= 90) else \
        '우' if (sj[5]  >= 80) else \
        '미' if (sj[5]  >= 70) else \
        '양' if (sj[5] >= 70) else '가'
    sj.append(grd)
    sjs.append(sj)

# 리스트에 저장된 성적 데이터들 중 기본 데이터만 모아서 출력
def showSungJuk():
    result = ''
    for sj in sjs:
        result += f'이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}\n'
    print(result)

def showDtSungJuk():
    result = ''
    for sj in sjs:
        result += f'''이름: {sj[0]}, 국어: {sj[1]}, 영어: {sj[2]}, 수학: {sj[3]}
        총점: {sj[4]}, 평균: {sj[5]:.1f}, 학점: {sj[6]}'''
        print(result)

# sungjuk.dat에 저장된 성적데이터를 읽어서
# sjs 변수에 초기화
def loadSungJuk():
    with open('./cks1031/sungjuk.dat', encoding='UTF-8') as f:
        rows = f.readlines()

    for row in rows:
        data = row.split(',')
        sj = [d for d in data ]
        sjs.append(sj)

    # for row in rows:
    #     sj = []
    #     data = row.split(',')
    #     sj.append((data[0]))
    #     sj.append((data[1]))
    #     sj.append((data[2]))
    #     sj.append((data[3]))
    #     sj.append((data[4]))
    #     sj.append((data[5]))
    #     sj.append((data[6]))
    #     sjs.append(sj)

# 메모리에 생성된 sjs변수의 모든 성적데이터를
# sungjuk.dat에 저장
# def saveSungJuk(sjs):
#     with open('sungjuk.dat', 'a' ,encoding='UTF-8') as f:
#         sj ={sj[0]},{sj[1]},{sj[2]},{sj[3]},{sj[4]}, 평균: {sj[5]:.1f}, 학점: {sj[6]}
#         sjs
#         f.write()

# 데이터 초기화 함수 호출
loadSungJuk()


