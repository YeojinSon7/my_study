# 모듈
# 함수, 변수, 클래스 모아놓은 파이썬 파일
# 다른 파이썬 프로그램에서 불러와서 사용
# import 명령어로 부러옴
"""
import 모듈이름
"""
# import my_module
# my_module.add(1,2)
# my_module.sub(1,2) # 객체의 멤버에 접근 -> . 즉 모듈도 파이썬에서는 객체다

"""
from 모듈이름 import 모듈함수
from 모듈이름 import 모듈함수1. 모듈함수2
from 모듈이름 import *                      # * 전체를 의미
"""
# from my_module import(add,sub)
# add(1,2)
# sub(1,2)

# from my_module import *
# add(1,2)
# sub(1,2)

# import my_module
# 실행하면 my_module의 내용이 나옴

from my_calculator import MyCalculator
# ide 활용법

class ZeroCalculator(MyCalculator):
    def div(self, n1, n2):
        if n2 == 0:
            print("0으로 나눌 수 없습니다.")
        else:
            print(f"{n1}/{n2}={n1/n2}")
zero_calculator = ZeroCalculator()
zero_calculator.div(10,0)

my_calculator = MyCalculator()
my_calculator.div(10,0) # 마우스 올려놓고 ctrl누르면서 클릭
# 에러가 나지 않도록 그 즉시 방지하는게 중요하다

# 위의 코드 에러난다 왜???