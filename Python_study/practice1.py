
eng = int(input("영어 점수: "))
kor = int(input("국어 점수: "))
math = int(input("수학 점수: "))

avg = (eng+kor+math)/3

if avg>=91 and avg<=100:
    print("A")
elif avg>=81 and avg<=90:
    print("B")
elif avg>=71 and avg<=80:
    print("c")
elif avg>=61 and avg<=70:
    print("D")
else:
    print("F")

# input() 입력받은 데이터는 문자열 타입
# int(값) 정수형 변환 함수
# #함수 사용자로부터 정보를 입력받는 함수
# user_input = input()
# print(user_input)

