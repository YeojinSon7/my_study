# 계산기 만들기
# 기능 : 두 정수의 사칙연산(+, =, *, /)
# add(), sub(), mul(), div() 함수 정의
# input() 함수를 활용하여
# 정수 2개, 사칙연산 선택을 입력받은 후
# 계산결과 print한다
# 계산식과 결과를
# calculator_result.txt 파일에 기록한다
# 사용자가 'q'를 입력하면 종료한다

# def add(a,b):
#     result = str(a)+ "+" + str(b) + "=" + str(a+b) # 포멧팅 문자열로 바꿔보기
#     print(result)
#     with open("C:/Users/405/my_study/Python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)
# def sub(a,b):
#     result = str(a)+ "-" + str(b) + "=" + str(a-b)
#     print(result)
#     with open("C:/Users/405/my_study/Python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)
# def mul(a,b):
#     result = str(a)+ "*" + str(b) + "=" + str(a*b)
#     print(result)
#     with open("C:/Users/405/my_study/Python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)
# def div(a,b):
#     result = str(a)+ "/" + str(b) + "=" + str(a/b)
#     print(result)
#     with open("C:/Users/405/my_study/Python_study/calculator_result.txt", "a", encoding="utf-8") as f:
#         f.write(result)




# while True:
#     print("""
#     계산기
#     1. +
#     2. -
#     3. *
#     4. /
#     q: 종료
#     """)
#     operator = input("원하는 계산을 입력하세요: ")
#     if  operator == 'q':
#         break
#     a = int(input("정수 1: "))
#     b = int(input("정수 2: "))
#     if operator == "1":
#         op = "+"
#         add(a,b)
#     elif operator == "2":
#         op = "-"
#         sub(a,b)
#     elif operator == "3":
#         op = "*"
#         mul(a,b)
#     elif operator == "4":
#         op = "/"
#         div(a,b)

if __name__== "__main__": # 실행코드부분만 안쪽으로 넣어준다
    
    class MyCalculator:
        def __init__(self): # 굳이 안해줘도 된다 
            pass
        def add(self,a,b):
            return a + b  # print(f"{n1} + {n2} = {n1+n2}")
        def sub(self,a,b):
            return a - b
        def mul(self,a,b):
            return a * b
        def div(self,a,b):
            return a / b
    my_calculator = MyCalculator()
    while True:
        print("""
        계산기
        1. +
        2. -
        3. *
        4. /
        q: 종료
        """)
        operator = input("원하는 계산을 입력하세요: ")
        if operator == 'q':
            print("종료하겠습니다.")
            break
        n1 = int(input("정수1: "))
        n2 = int(input("정수2: "))
        if operator == "1":
            print(n1,"+",n2,"=",my_calculator.add(n1,n2))
            
        elif operator == "2":
            print(n1,"+",n2,"=",my_calculator.sub(n1,n2))
        
        elif operator == "3":
            print(n1,"+",n2,"=",my_calculator.mul(n1,n2)) 
            
        elif operator == "4":
            print(n1,"+",n2,"=", my_calculator.div(n1,n2))
        else:
            print("잘못 입력했습니다.")
        
