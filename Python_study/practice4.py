# 다음 함수를 정의하세요
# 정수 n을 입력받고, n보다 작은 수 중 3의 배수와 5의 배수를 모두 더한 합을 반환하는 함수
# 함수 이름: sum_3_5

# def sum_3_5(n):
#     total = 0
#     for i in range(1,n):
#         if i % 3 == 0 or i % 5 == 0 : # if ~ elif 사용가능
#             total += i
#     return total
# print(sum_3_5(15))

# 정육면체 주사위 2개가 있다
# 2개의 주사위를 던졌을 때 나올 수 있는 주사위 눈의 조합을 모두 print하는 함수를 정의하세요
# 함수 이름 : double_dice
# 출력 예시
# 1, 2
# 6, 3

# def double_dice ():
#     for i in range(1,7):
#         for j in range(1,7):
#             print(i, j)
# double_dice()

# def double_dice ():
#     i = 1
#     while i < 7:
#         j = 1
#         while j < 7:
#             print(i, j)
#             j += 1
#         i += 1

# 두 수의 차이를 구하는 함수
# 함수에 입력된 두 정수의 차이를 계산하고 반환하는 함수를 정의하세요

# def get_diff (a, b):
#     result = abs(a - b) # if문 사용가능 if a < b: 처럼
#     return result
# print(get_diff(3,5))



# 가장 큰 수를 만드는 함수
# 함수에 입력된 5개의 정수를 사용하여 만들 수 가장 큰 수를 반환하는 함수
# 자릿수 이용하면 된다!
# def get_biggest(a, b, c, d, e):
#     li = [a, b, c, d, e]
#     li.sort() # 리스트 정렬
#     result = 0
#     for i in range(len(li)):
#         result += li[i] * (10 ** i)
#     return result
# print(get_biggest(1,2,3,5,5))

# 이런방법도 있다
# numbers = [a,b,c,d,e]
# numbers.sort(reverse=True)
# result = ""
# for i in numbers:
#     result += str(i)
# return int(result)
# 파이썬은 문자형 숫자형 왔다갔다 하기 편하다?


# 별찍기2 ㅎㄴㅎㅌ ㄷㅇㄹ ㄱㄹㅇ ㅈㅅㅊㄹㅈ
# 정수를 함수에 입력하여 호출하면 해당 정수 줄의 별을 화면에 출력한다.
# 함수 이름: print_stars2

# def print_stars2(n):
#     for i in range(1,n+1):
#         print(" " * (n-i) + "*" * (i))
# print_stars2(10)


# 실뭄에서 요청한게 애매해면 의뢰자한테 다시 확인해야한다


# 다음에 또 쓸려고 기록장치에 저장
# 프로그램이 데이터를 저장한다





















































