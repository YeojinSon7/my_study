"""
if 조건: /식, 값이 들어감 
    실행하려는 코드 (구분하기위해서 tab으로 뛰어쓴다)(python에서는 tab으로 구별)
구분된 영역 = 코드블록
if문은 조건이 True(참)일 때만 안쪽 코드블록 실행
else:
    실행하려는 코드
else문은 False(거짓)일 때만 안쪽 코드블록 실행

if 조건1:
    조건1이 참일 때 실행
elif 조건2:
    조건1은 False, 조건2는 True일때 실행
else:
    조건 1,조건 2 False일때 실행
"""

# bool 
# True, False  즉 참, 거짓

number1 = 7
number2 = 7
if number1 > number2: #조건식 결과는 True False
    print("number1이 더 크다.")
elif number1 == number2:
    print("같다")
else:
    print("number2가 더 크다")

#비교 연산자
# >
# >=
# <
# <=
# ==
# != 같지 않다

print(2 > 3) #F
print(2 >= 3) #F
print(2 < 3) #T
print(2 <= 3) #T
print(2 == 3) # F
print(2 != 3) #T

# 문자는 사전순으로 되어있다/ a먼저 오는게 더 작다

print("a" < "b") #T
print("CAT" < "DOG") #T 
print("COW" > "CAT") #T
print("DOG" == "dog") #F
print("DOG" > "dog") #F #대문자가 더 먼저 오게 되어있어서

# 논리 연산자 T,F 사용
# and a and b a와 b가 모두 True일 때만 True 아니면 False
# or a or b a와 b중 하나라도 True면 True 둘다 False면 False
# not True면 False로 False면 Truefh

print(True and True) #T
print(True and False) #F
print(False and True) #F
print(False and False) #F


print(True or True) #T
print(True or False) #T
print(False or True) #T
print(False or False) #F

print(not True) #F
print(not False) #T
#피연산자가 1개라 단항연산자

age = 27
money = 10000
if age >= 20 and money >= 10000:
    print("성인이고 부자입니다")

if "안녕":
    print("안녕하세요")
#문자열에 값이 있으면 True 값이 없으면 False
if 0:
    print(0)
#숫자에서 0이면 False 다른숫자는 True











