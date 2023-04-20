import random

print("가위 바위 보 게임")
print("가위 바위 보를 하는 게임입니다")

com = random.choice(['가위','바위','보'])
player = input("가위 바위 보 중 하나를 입력하세요.")

print("컴퓨터는 " + format(com) +"를 냈습니다.")
print("플레이어는 " + format(player) +"를 냈습니다.")

if com == "가위":
    print("컴퓨터는 가위를 냈습니다.")
    if player == "가위":
        print("무승부")
    elif player == "바위":
        print("플레이어의 승리!")
    elif player == "보":
        print("컴퓨터의 승리!")
elif com == "바위":
    print("컴퓨터는 바위를 냈습니다.")
    if player == "가위":
        print("컴퓨터의 승리!")
    elif player == "바위":
        print("무승부")
    elif player == "보":
        print("플레이어의 승리!")
elif com == "보":
    print("컴퓨터는 보를 냈습니다.")
    if player == "가위":
        print("플레이어의 승리!")
    elif player == "바위":
        print("컴퓨터의 승리!")
    elif player == "보":
        print("무승부")
    
# 조건문에서 if,elif 쓰고 나머지 else라고 하는거랑 elif로 조건 써주는 거랑 차이가 없는지 궁금