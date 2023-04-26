# function 함수
# 입력 -> 처리 -> 출력
# input을 받아서 특정 작업을 수행하고 output(출력)을 반환한다

# 내장 함수(built-in)
# 파이썬이 기본적으로 제공해주는 함수
# print(), len(), zip(), int(), float(), str(), list(), range()
# abs() (absolute) (절대값 반환)
# 입력한 숫자형 데이터의 절대값을 반환
# print(abs(100))
# print(abs(-100))
# print(abs(3.15))
# print(abs(-3.15))

# sum(리스트)
# 리스트 안의 숫자를 더한 값을 반환
# print(sum([1, 2, 3, 4, 5]))

# max(리스트)
# 리스트 안에서 최대값을 랒아 반환
# print(max([1, 2, 3, 4, 5]))

# min(리스트)
# 리스트에서 최소값을 찾아 반환
# print(min([1, 2, 3, 4, 5]))

# chr(정수)
# 정수 1개를 입력받고 해당하는 유니코드 문자를 반환
# print(chr(65)) # A

# # ord(문자)
# # 문자 1개를 입력받고 해당하는 정수를 반환
# print(ord('A')) # 65

# round(값)
# round(값, 소수 자릿수) # parameter 기본값쓰임
# 반올림 함수
# print(round(1,234)) #1
# print(round(1.234, 2)) # 1.23
# print(round(1.369,1)) # 1.4

# 함수 정의(define)
# 함수 이름
# 함수 입력값 (parameter)
# 함수 결과값 9return value)

"""
def 함수이름(함수입력값):
    함수기능코드
    return 함수 결과값
"""
# def 함수를 정의하는 명령어
# 함수이름도 변수 이름처럼 규칙을 지켜서 지어야한다
# 영어, 숫자, _만 사용
# 숫자로 시작하면 안된다
# 띄어쓰기하면 안된다
# 키워드 사용하면 안된다 (이미 있는 함수이름 쓰지마라)
# 만약 기존에 있는 함수이름 쓰면 python에서는 사용자가 정의한 함수 먼저 부른다

# def print_names():
#     print("손흥민")
#     print("황희찬")
#     print("김민재")
#     print("이강인")
# return 값이 없는 함수

# print_names()

# def get_name():
#     return "손여진" # 출력값이 있는 함수
# def print_my_name():
#     print(get_name())

# print_my_name()

# 함수 호출했을 때 리턴값이 있으면 변수에 할당 가능

# def add(a, b): # parameter, 매개변수, argument 혼용
#     return a + b

# def print_add(a, b):
#     print(a + b)

# add(1, 2) # 아무것도 안나옴 반환만 하느거라

# result = print_add(2,3) # 이 함수는 출력만 하는거라 반환값이 없어서 result 변수에 아무것도 안들어간다
# print(result) # result가 None이 나온다 
# 정의한 함수를 쓰면 그것이 함수를 호출한 것

# print_add("안녕","하세요") # 위치로 구분
# prnit_add("안녕",1) # 오류난다

# print_add(b = "하세요", a= "안녕") # 이런식으로 매개변수를 지정해서 쓸 수 있다

# def swap_number(a, b):
#     temp = a
#     a = b
#     b = temp
#     print(a, b)
#     return a, b

# swap_number(1,2)

# a = 1
# b = 2
# print("함수 호출 전", a, b)
# swap_number(a, b) / a, b = swap_number(a, b) # 함수 리턴값을 전역변수에 준다
# print("함수 호출 후", a, b)
# 함수 안에서 쓰는 a,b와 함수 바깥에서 쓰는 a,b는 다르다
# 함수에 전달 될 때는 변수의 값이 전달되어 함수 내에서 완전히 새롭게 쓰인다
# 함수 밖 변수 전역 변수/ 함수,for,if 등등 ( )안에 있는 건 지역변수

# 다음 함수 정의하세요
# 함수 이름: mul
# 함수 입력값: 정수 2개
# 함수 출력값: 정수 2개의 곱

# def mul(a, b):
#     return a*b

# print(mul(7,7))

# 에러가 나면 함수가 정의된 부분에 가서 확인한다

# a, b, c = 1, 2, 3
# d, e, f = [4, 5, 6]
# g, h, i = (7, 8, 9)
# python에서는 위의 방법이 가능하다

# def mul(n1, n2=1): # default value/default parameter  기본 값 매개변수
#     return n1*n2
# # 함수 호출 시 n2에 입력된 값이 없으면 기본 값 사용

# mul(1) # 1이 나온다

# def test_func(x, test=[]):
#     test.append(x)
#     print(x, test)

# test_func(1)
# test_func(2)
# list는 지역변수임에도 전역변수로 이용되고 있다 그래서 기본값으로 리스트를 쓰면 안된다
# 따라서 위에 2줄에서 list 같은 애가 된다

# def test_func1(x, test=5):
#     test= test
#     print(x, test)

# test_func1(1)
# test_func1(2)

# def test_func2(x, test=None):
#     if test == None:
#         test = []
#     test.append(x)
#     print(x,test)
# test_func2(1)
# test_func2(2)

# 기본값이 있는 매개변수는 기본값이 없는 매개변수 뒤에 위치해야한다
# def sub(n1, n2, n3=0):
#     print(n1 - n2- n3)

# # 1~10까지 더한다
# # *를 사용한 매개변수
# # 입력값이 몇개가 될지 모를 때(안 정해졌을 때) 사용한다
# def add_many(*args):
#     # 튜플처럼 사용
#     # 인덱싱, 슬라이싱 가능
#     result = 0
#     for i in args:
#         result += i
#     return result

# result1 = add_many(1, 2, 3, 4, 5)
# print(result1)
# result2 = add_many(3, 2, 5, 9, 1)
# print(result2)
# result3 = add_many(1, 2)
# print(result3)

# def calc_many(n1, *args): # calc_many(*args, n1) 이런식으로 순서 바꿔도 된다
#     result = n1
#     for i in args:
#         result += i
#     return n1

# 키워드 매개변수
# **kwargs
# keyword arguments
# 딕셔너리로 사용
# def print_kwargs(**kwargs):
#     print(kwargs)
# print_kwargs(a=1, b=2)
# print_kwargs(name = "이름", age=10)
# 뒤에오는게 유동적일때

# 함수의 반환
# return 반환값
# return을 만나면 반환값을 반환함과 동시에 함수가 종료된다
# 함수의 반환값은 무조건 1개이다.
# def test_func6(a,b):
#     return a+b,a*b # 이런식으로 한줄로 써줘야함 가능한 이유는 튜플형태인 (a+b, a*b)로 반환하라는 뜻이어서
# result = test_func6(1,2)
# res_add,res_mul = test_func6(1,2)
# #res_add, res_mul = (a+b, a*b)
# print(result)
# print(res_add,res_mul)

# 홀수 판별 함수
# 함수 이름: is_odd_number
# 파라미터: n
# 반환값 : 홀수면 True, 짝수면 False

# def is_odd_number(n):
#     if n % 2 != 0: # if문 이중은 복잡하니까 잘 안쓰려고한다 
#         return True 
#     return False
# print(is_odd_number(77))

# def is_odd_number(n):
#     return n % 2 == 1 

# 테두리를 출력하는 함수
# 문자열을 입력받고 print 함수를 이용해 테두리와 함게 문자를 출력한다
# 함수 이름 : get_bordered_str
# 파라미터 : message
# 반환값 : None
# print 예시
"""
*****
hello
*****
"""

# def get_bordered_str(message):
#     n = len(message) # len함수에서는 연결형 sequnce형을 쓴다
#     print("*" * n) # 문자 반복
#     print(message)
#     print("*" * n)
# get_bordered_str("안녕하세요")

# get_bordered_str(str(12345))

# 속도를 변환하는 함수
# m/s 단위의 속도가 입력되면  -> km/h 단위의 속도로 변환한다
# 함수 이름: convert_velocity
# 파라미터 : velocity
# 반환값: km/h로 변환된 속도

# def convert_velocity (velocity):
# 1초에 1m -> 1m/s
# 1m/s * 3500(1시간)
# 3600m/h
# 1km는 몇 m? 1000m
# 3600/h 는 몇 km/h?
# 3600m/h / 1000(1km)
# 1m/s --> 3.6km/h
# 1m/s * 3600 / 1000 ---> 3.6km/h
# 초속 * 3600/ 1000 ---> 시속
# 초속 * 3.6 = 시속
#     result = velocity * 3.6
#     return result
# print(convert_velocity(10))

"""
n -> 4
*
**
***
****
"""
# 별 찍기 함수
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다

# 함수 이름: print_stars
# 파라미터 : n
# 반환값 : Nome

# def print_stars(n):
#     for i in range(1,n+1):
#        print("*" * i)

# print_stars(8)

# def print_stars(n):
#     for i in range(n):
#         for j in range(i+1):
#             print("*", end="")
#         print()

# def print_stars(n):
#     i = 0
#     while i < n:
#         j = 0
#         while j < i+1:
#             print("*", end = "")
#             j += 1
#         print()
#         i += 1

# for문 while문 같이써서 해보기


