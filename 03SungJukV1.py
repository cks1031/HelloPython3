# 성적 처리 프로그램 v1
# 이름, 국어, 영어, 수학을 입력 받으면
# 총점, 평균, 학점을 계산하고 출력함
# 학점 : 수우미양가
# 결과 출력
# 이름 : 홍길동, 국어: 99, 영어: 98, 수학: 99
# 총점 : 296, 평균 99.9, 학점: 수
# 90 > 수 or 80 > 우 or 70 > 미 or 60 > 양

# 성적데이터 입렵받음
name = input('이름')
kor = int(input('국어 점수'))
eng = int(input('영어 점수'))
math = int(input('수학 점수'))

# 성적 처리
sumSubject = kor + eng + math # 총점
avgSubject = sumSubject / 3 # 평균
grade = '수' if (avgSubject >= 90) else \
        '우' if (avgSubject >= 80) else\
        '미' if (avgSubject >= 70) else\
        '양' if (avgSubject >= 70) else '가'

# 결과 출력
print(f'''
이름: {name}, 국어: {kor}, 영어: {eng}, 수학: {math}
# 총점: {sumSubject} 평균: {avgSubject:.1f} 학점 :{grade}
''')


# 성적데이터 입렵받음
name = input('이름')
kor = int(input('국어 점수'))
eng = int(input('영어 점수'))
math = int(input('수학 점수'))

# 성적 처리
sumSubject = kor + eng + math # 총점
avgSubject = sumSubject / 3 # 평균
if grade >= 90 : print('수')
elif (grade < 90) and (grade >= 80) : print('우')
elif (grade < 80) and (grade >= 70) : print('미')
elif (grade < 70) and (grade >= 60) : print('양')
else : print('가')

# 결과 출력
print(f'''
이름 : {name}
국어 : {kor} 영어 : {eng} 수학 : {math}
총점 : {sumSubject} 평균 : {avgSubject:.1f} 학점 :{grade}
''')