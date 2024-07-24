# 사원 등록 프로그램

import sys
from cks1031.oop.services import EmpService as empsrv

# 메뉴 출력 및 메뉴 별 처리
while True:
    # 메뉴 입력받음
    menu = empsrv.display_menu()

    if menu == '1':
        print('사원 데이터 추가')
        empsrv.add_Emp()
    elif menu == '2':
        print('사원 데이터 조회')
        empsrv.show_Emp()
    elif menu == '3':
        print('사원 데이터 상세조회')
        empsrv.showOne_Emp()
    elif menu == '4':
        print('사원 데이터 수정')
        empsrv.modify_Emp()
    elif menu == '5':
        print('사원 데이터 삭제')
        empsrv.remove_Emp()
    elif menu == '0':
        print('프로그램 종료')
        sys.exit(0)
    else:
        print('메뉴를 잘못 선택하셨습니다!!')