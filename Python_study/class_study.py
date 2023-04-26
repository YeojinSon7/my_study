# 객체지향(oop, object oriented programming)
# 자바, c++, c#
# 객체와 객체 사이의 상호작용으로 프로그램을 구성하는 프로그래밍 패러다임

# 객체지향의 특징
# 추상화 : 공통된 속성이나 기능 도출
# 캡슐화 : 데이터의 구조와 연산을 결합
# 상속 : 상위 개념의 특징이 하위 개념에 전달
# 다형성 : 유사 객체의 사용성을 그대로 유지

# 객체는 추상화와 캡슐화의 결과
# 객체는 데이터 필드와 메소드를 가진다

# 클래스는 객체를 정의한 것(객체의 설계도)
# 데이터 필드(멤버 변수, 속성) 객체가 가지고 있는 변수
# 메소드는 객체가 가지고 있는 함수
"""
class 클래스이름:
    클래스 멤버 변수
    메소드
"""
# 클래스 이름도 변수 이름 규칙 지켜야 함
# 클래스 이름 컨벤션(관용) (안지킨다고 에러는 안나지만 대부분은 다 지킨다)
# 첫 글자 대문자
# 언더바(_) 안쓰기
# 단어 구분될 때 대문자

# class Car:
#     def move(self): # 클래스 안에 있는 함수는 메소드, 멤버 함수 라고 한다
#         print("move")

# class SportsCar:
#     pass

# move() 클래스 안에 정의해놔서 밖에서 쓰면 에러난다

# 인스턴스
# 클래스를 통해 생성된 객체
# my_car = Car()
# my_car.move() 
# . -------------> 객체 멤버 접근 연산자 즉 객체을 통해서~

# 객체랑 객체를 가지고 프로그래밍을 한다
# 추상화 캡슐화먄 기억해도 좋다 즉 똑같은거 또 안만들어도 된다
# 객체는 클래스에 정해진대로 만들어진다

# li= [1, 2, 3, 4, 5]
# li.append(6)
# 사실 파이썬에서는 모든게 객체다!
# 내장함수 type() 데이터의 자료형을 반환한다.
# print(type(li))
# n = 10
# print(type(n))
# print(type("Hello"))
# str(문자열) 메소드
# upper() 
# 모두 대문자로 변경
# s = "Hello"
# print(s.upper())
# lower()
# 모두 소문자로 변경
# print(s.lower())
# strip()
# 문자열 양쪽 끝의 공백을 제거
# s1 = "     Hello      "
# print(s1.strip())
# lstrip(), rstrip() 
# 왼쪽, 오른쪽 끝의 특정 문자 제거
# print(s1.lstrip())
# print(s1.rstrip())
# split()
# 구분자로 분할하여 리스트로 반환
# s2 = "Hello,World,Python"
# print(s2.split(','))
# replace()
# 문자열의 특정 부분을 대체
# print(s2.replace(","," "))
# 문자열은 수정이 불가하기때문에 함수써서 바뀐것 같아도 원본이 바뀌지 않고 새로운 문자열을 만든다
# s2 = s2.replace(","," ")
# print(s2) # 이건 수정이 아니라 재할당한 것이다

# "Hello"를 "hello"로 바꿔보자
# s2 = "Hello"
# print(s2)
# s2 = s2.replace("H","h")
# print(s2)

# s2[0] = h 이거쓰면 에러난다 왜냐면 문자열은 immutable이니까











