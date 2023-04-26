def add(a,b):
    return a+b
def sub(a,b):
    return a-b


if __name__ == "__main__": #python에서 실행하는 특별한 함수들을 __   __로 표현
    print(add(1,2))
    print(sub(3,4))
else:
    print(__name__)
# 포함된 파일은 name이 my_module되기 때문에 실행시킨 파일에서는  print(add(1,2), print(sub(3,4)) 안나온다


