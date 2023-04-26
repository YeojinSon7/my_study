# 예외 처리
# 오류 발생을 잡아내서 처리하는 것

# li = [1, 2, 3, 4, 5]
# li[100]

# 100 / 0

# f =  open("없는파일", 'r')

# 에러 발생 시 프로그램을 중단하고 에러 메세지를 보여준다

# 에러 처리 구문
# try ~ except
# try 블록에는 오류가 발생할 수 있는 코두
# except 블록에는 오류가 발생했을 때 수행할 코드
# try:
#     100 / 0
# except Exception as e: # Exception 오류 클래스 예외객체 잡아내서 에러메세지 출력
#     print(e) # try 안에 에러가 발생할 경우 실행한다 오류 없으면 실행 안된다

# print("에러 발생 후")

# try:
#     [1, 2, 3, 4, 5][100]                         # except에서 나온 에러가 아닌 다른에러가 나오는 코드가 try에 써있으면 에러를 못잡는다
# except ZeroDivisionError as e: 
#     print(e, "0으로 나눌 수 없습니다.") 

# finally
# 예외 발생 여부와 상관 없이 항상 수행되는 코드 (마지막으로 수행할 코드)
# try:
#     f = open("없는 파일", "r")
# except: 
#     print("에러 발생")
# finally:
#     f.close()

# else
# 오류가 발생하지 않으면 실행되는 코드
# try:
#     age = int(input("나이: "))
# except:
#     print("입력이 잘못 되었습니다.")
#     print("숫자를 입력해주세요.")
# else:
#     if age >= 20:
#         print("성인입니다.")
#     else:
#         print("미성년자입니다.")

# class Bird:
#     def fly(self):
#         raise NotImplementedError # 일부로 에러 발생

# my_bird = Bird()
# my_bird.fly()
# 다른 사람들이나 미래의 나한테 구현안한걸 알려줘야한다