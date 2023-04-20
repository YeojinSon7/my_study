# while 반복문
"""

while 조건: 
    반복할 코드

"""
# 조건이 참인 경우에 코드를 계속 반복
# n =  1
# while n <= 10:
#     print(n)
#     n += 1 # n = n+1

# += 연산자
# 대입 연산자의 일종
# 더하기 연산 후 할당
# n += 1은 n = n+1이라는 의미
# 다른 산술 연산자 사용 가능

# s1 = "안녕"
# s1 += "하세요"
# 문자열도 가능 s1,s2가 연결된다

# while 반복문 활용, 10부토 1까지 순서대로

# j= 10
# while j >= 1: # j > 0 도 쓸 수 있다
#     print(j)
#     j -= 1

# money = 10000
# price = 1000
# coffee = 5
# while money >= price: # money - price >= 0 도 쓸 수 있다
#     print("커피를 구매했습니다.")
#     money -= price
#     coffee -= 1
#     print("남은 커피: ", coffee)
#     if coffee == 0:
#         break
#break는 반복문 안에서 사용 반복문에서 break를 만난다면 그 즉시 반목문 빠져나간다(종료한다)


# num = 1
# while num <= 100:
#     if num%2 == 0:
#         print(num)
#     num += 1

# num2 = 100
# while num2 >= 100:
#     if num2 % 23 == 0:
#         print(num2)
#         break
#     num2 += 1

# while 반복문 활용 1 부터 10까지 홀수만 출력
# num = 1
# while num <= 10:
#     if num % 2 == 1:
#         print(num)
#     num += 1

# continue
# 반복문의 제일 처음으로 돌아감

# b = 1             b = 0 이면  while 조건에 b <= 9를 넣으면 된다
# while b <= 10:
#     if b % 2 == 0:
#         # b += 1
#         continue
#     print(b)
#     b += 1

# while True:
#    print("hi") 
# 무한반복문
# 무한루프
# 조건식에 True를 입력해 항상 참이 되도록 하여 무한히 반복하게 한다


# while True:
#     user_input = input("종료하려면 1을 입력해주세요.")
#     if user_input == "1":
#         break

# 무한반복문으로 계산기 만들기
# + , -, *, / 계산
# 2개의 수를 계산 a + b
# while True:
#     print("""
#      계산기
#     -----------
#     1. 더하기 (+)
#     2. 빼기 (-)
#     3. 곱하기 (*)
#     4. 나누기 (/)
#     q. 계산기 종료
#     """)
#     operator = input("계산을 선택하세요 : ")
#     if operator == "q":
#         break
#     a = input("계산할 수1: ")
#     b = input("계산할 수2: ")
    
#     if operator == "1":
#         print(a+"+"+b+" = ", int(a)+int(b)) # a하고 b가 정수형일 때 print(a, "+", b, "=" , a+b) 로 바꿔주면 된다
#     elif operator == "2":
#          print(a+"-"+b+" = ", int(a)-int(b))
#     elif operator == "3":
#         print(a+"*"+b+" = ", int(a)*int(b))   
#     elif operator == "4":
#         print(a+"/"+b+" = ", int(a)/int(b))
    
# elif 는 else중에 if
# 위의 if가 참이면 elif는 else는 체크도안함
# 근데 if 여러번 써주면 맨위의 if가 참이어도 밑에 if들도 체크함

# 사용자가 가지고 있는 돈을 입력받는다.
# 구매할 수 있는 커피 개수와 잔돈을 출력
# 구매할 수 있는 음료수 개수와 잔돈을 출력
# 구매할 수 있는 콜라 개수와 잔돈을 출력
# 커피 500원 음료수 700원 콜라 930원
# 물품 개수는 무한이라 가정
# while 반복문 사용하여 작성
# idx = 0
# prices = [500, 700, 930]
# money = int(input("가지고 있는 돈: "))

# while idx < len(prices): #정해놓으면 나중에 데이터가 추가되거나 삭제될 때 수정하기 힘들다 그래서 어떤값이 오든 구할 수 있는 코드를 추천
#     price = prices[idx]
    
#     print("구매할  수 있는 커피 개수: ", money // price)
#     print("잔돈: ", money % price)
#     idx += 1

# while 반복문을 사용
# scores 리스트에 시험 점수 5개를 정수형으로 입력받으세요.

# scores = []
# i = 0

# while i < 5:
#     scores.insert(i,int(input("시험 점수를 입력하세요: ")))
#     i += 1
# print(scores)


# score = int(input("시험점수: "))
# scores.append(score)


# while 반복문을 사용하여 구구단 2단 출력

# num = 1
# while num < 10:
#     print(2*num) 
#     num += 1

# print("2 *", n, "=", 2 * n)














