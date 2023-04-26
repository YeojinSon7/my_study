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

# self 매개변수
# 모든 메소드의 첫번째 매개변수 (무조건 써줘야한다)
# 메소드의 정의에는 사용되지만, 호출에는 사용되지 않음
# 객체 자신을 참조하여 클래스에 정의된 멤버에 접근할 때 사용
# class Person:
#     def say(self):
#         self.name = "사람1"
#         print("Hello")
#     def move(self):
#         pass
#     def eat(self,food):
#         self.sleep() # 함수도 불러와서 쓸 수있다
#         print(f"{self.name}이 {food}를 먹었습니다") # 위에서 self.name 정해줘서 밑에서 쓸 수 있다
#     def sleep(self):
#         print(f"{self.name}이 잠을 잤습니다.")    

# person1 = Person()
# person1.say() # self는 호출에는 안쓰지만 여기서 self는 person1을 가리킨다
# person1.eat("밥")

# initializer
# 초기자
# initialize 초기화 ex) person1 = Person() person1을 생성할 때 (인스턴스 생성) initialize한다
# initializer 는 초기화할때 어떤걸 할지 정하는거

# class Person:
#     def __init__(self, name, age, gender, phone):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.phone = phone
#         print("initialize")
#     def say_name(self): 
#         print(self.name) # name 쓰면 에러난다 name이 정의된 함수 밖으로 나가면 없어져서
#     def introduce(self):
#         print(self.name)
#         print(self.age)
#         print(self.gender)
#         print(f"안녕하세요 저는 {self.name}입니다")
#         print(f"나이는 {self.age}살이고, 성별은 {self.gender}입니다")
# print("before")
# person2 = Person("손여진", 20, "여자", "010-7777-7777")
# print("after")
# person2.say_name()
# person2.introduce()
# # Person 클래스에 introduce 메소드르 추가
# 이름, 나이, 성별을 print하는 메소드

# 상속 inheritance
# 부모 클래스를 물려받아 자식클래스를 만든다
# class Animal:
#     def __init__(self,name):
#         self.name = name # 매개변수로 받은 name을 멤버변수 self.name에 저장한다 name과 self.name은 값이 같은 다른개쳬이다
#         print(f"{self,name}이 생성되었습니다.")

#     def say(self):
#         print("")

# class Dog(Animal):
#     def say(self): #메소드 재정의 method overriding
#         print("멍멍")

# my_dog = Dog("백구")
# my_dog.say()

# class Cat(Animal):
#     def say(self):
#         print("야옹")
# my_cat = Cat("토토")
# my_cat.say()

# class Student:
#     def __init__(self, name, age, school, grade) :
#         self.name = name
#         self.age = age
#         self.school = school
#         self.grade = grade
        
#     def introduce(self):
#         print(f"제 이름은 {self.name}입니다, 나이는 {self.age}이구요 학교는 {self.school}이며 학년은 {self.grade}학년입니다.")

# student = Student("손여진", 20, "대박대학교", 1)
# student2 = Student("손흥민", 30, "배드대학교", 1)
# student.introduce()
# student2.introduce()
# stu_list = [student, student2]
# for stu in stu_list:
#     stu.introduce()













