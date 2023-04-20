# for문
"""
for 변수 in iterable값:
    반복할 코드
iterable 순회가능하다
대표적으로 문자열, 리스트
"""

# li_1 = ["one", "two", "three"]
# for i in li_1:
#     print(i)
# 첫번재 요소부터 마지막 요소까지
# 변수에 대입하면서 반복

# s1 = "hello"
# for i in s1:
#     print(i)

# while과 for 서로 똑같은 내용 만들 수 있다
# 무한반복문은 for문에서 못만든다

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in numbers:
#     print(number)

# numbers.reverse()
# for number in numbers:
#     print(number)

# range() #범위 넣어주는건 정수여야 한다
# range(끝 정수) 0 ~ (끝 정수 -1)
# range(시작, 끝) 시작 ~ (끝 -1)
# range(시작, 끝, 스텝) 시작 ~ (끝 -1) 까지인데 스텝만큼 차이나게


# for i in range(10):
#     print(i)
# for i in range(1, 11):
#     print(i)
# for i in range(1, 21, 2):
#     print(i)

# for문을 사용하여 2부터 30까지

# for i in range(2,31):
#     print(i)


# for문을 사용하여 2부터 30까지 숫자 중 짝수만

# for i in range(2,31,2):
#     print(i)
"""
for i in range(2,31):
    if i % 2 == 1:
        #continue
        pass #아무것도 안하고 그냥 넘어간다
    else: 
        print(i)

for i in range(2,31):
    if i % 2 == 0:
        print(i)
"""

# for문을 사용하여 10부터 1까지

# for i in range(10, 0, -1):
#     print(i)
"""
for i in reversed(range(1,11)):
    print(i)

for i in range(1,11)[::-1]:
    print(i)    

 슬라이싱 [시작인덱스:끝인덱스:방향]

"""
# reversed라는 함수를 이용해 뒤집을 수 있다

# money = 2000
# price = 1000
# coffee = 5

# for i in range(coffee): 
#     print("커피를 구매했습니다.")
#     money -= price
#     print("남은 커피:", coffee - 1 - i)
#     if money < price:
#         break

# for문은 반복횟수가 정해져있을 때 좋다
# while문은 특정 조건이 있을 때 좋다 특정 동작까지 특정 시점까지

# for i in range(1, coffee + 1):
#     print("남은 커피 :", coffee - i)

# for i in range(coffee):
#     coffee -= 1
#     print("남은 커피 :", coffee)

# prices = [500, 700, 930]
# money = int(input("돈 "))

# for i in range(len(prices)):
#     price = prices[i]
#     print(money // price)
#     print(money % price)

# for price in prices:      # 이렇게 사용하는게 for문을 잘 사용하는 것
#     print(money // price)
#     print(money % price)
# scores = []
# for i in range(5):
#     score = int(input("시험점수: "))
#     scores.append(score)
# print(scores)

# for i in range(1,10):
#     print(2*i)

# 이중 for문
# for i in range(2,10):
#     print(i, "단")
#     for n in range(1,10):
#         print(i*n)
#     print("----------")

