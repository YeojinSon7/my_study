# tuple (튜플)형
# 값이 정해지면 값을 수정할 수 없다 즉 튜플은 element의 갑슬 수정할 수 없다.
# mutable / immutable
# mutable 수정 가능한 - list, dictrionary
# immutable 수정 불가능 - int, float, str, tuple

# my_list = [1, 2, 3]
# my_list[0] = 5
# print(my_list)

# my_tuple = (1, 2, 3) # 튜플은 소괄호 사용
# my_tuple[0] = 5
# print(my_tuple) # 에러난다  튜플형은 수정 불가능
# 원본 보호때문에 사용

# tuple_1 = ("Hello", "world", "python")
# t2 = (1, 2, 3, 4, 5)
# t3 = (1, 2, "Hello")
# t4 = 1, 2, 3
# t5 = (1, 2, (3, 4, 5))

# 삭제도 안된다

# t6 = tuple_1 + t2
# t7 = t3 * 3
# t7 = t3 * 4
# print(t7) # 가능하다 왜냐면 가리키는 화살표가 달라지는거라

# print(t3[2]) # 들어있는 값 형태
# print(t3[0:2]) # 튜플형으로 가져온다 튜플형이라 또 수정이 안된다
# print(len(t3))

# print(t5[2][1])

# t8 = (5, 3, 1, 4, 2)
# 값이 바뀌는 정렬은 못한다
# 값을 추가하는것도 안된다

# mutable / immutable 인지 잘 체크하고 써야한다

# for i in t8:
#     print(i)
# 인덱스 순서대로 들어가서 5, 3, 1, 4, 2가 나온다
# 튜플에서 +,* 연산 된다 왜냐면 수정이 아니고 새로 만드는 거라서

# 2 ~ 9 사이의 숫자를 입력받아
# 해당하는 단의 구구단을 출력하세요

# num = int(input("2~9사이의 값을 입력하세요: "))
# while num < 2 or num > 9: # 조건이 참일 때 반복 not 2 <= n <= 9로 써줘도 된다
#     print("잘못 입력했습니다")
#     num = int(input("다시 입력하세요: "))

# if n >= 2 and n <= 9 이렇게 써주면 안에는 구구단 출력 코드 쓰기
# if 2 <= n <= 9로 써줄수도 있다 오직 python에서만 가능 다른언어는 불가능

# t1 = (1, 2, 3, 4, 5, 6, 7, 8 ,9)
# for i in t1: #iterable 값 즉 하나씩 줄 수 있다 또는 range(1, 10) 
#     print(num, "*", i, "=", num*i)

# 정수를 입력받고 그 정수보다 작은 수 중 가장 큰 제곱수를 출력하세요.

# num = int(input("정수를 입력하세요: "))
# i = 0
# while i ** 2 < num:
#     i += 1
# print((i-1) ** 2) 
# 4 ** 0.5 이것도 제곱근 구하는 방법이다


# while True:
#   if i * i > n:
#       break # while 문을 빠져나간다
#   answer = 1 ** 2
#   i += 1
# print(answer)