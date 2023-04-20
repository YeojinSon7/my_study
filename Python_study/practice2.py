# li_1 = ["Hello", "World", "Python"]
# # Hello World Python 이라고 출력하세유

# print(li_1[0]+" "+li_1[1]+" "+li_1[2]) 
# print(li_1[0], li_1[1], li_1[2])

# # join(리스트) 개수가 많은 리스트를 하나로 합쳐주는것
# # " ".join(li_1) # 합칠때 사이사이에 " "을 넣어준다

# print(" ".join(li_1))

# # Help라고 출력하슈

# print(li_1[0][0]+li_1[0][1]+li_1[0][2]+li_1[2][0])
# print(li_1[0][:3]+li_1[2][0])

# li_2=[1, 2, 3]
# # li_1과 li_2를 사용하여 ["Hello", "World", "Python", 1, 2, 3] 출력

# print(li_1+li_2)

# #li_1.extend(li_2)
# #print(li_1)

# # li_1과 li_2를 사용하여 ["Hello", "1", "World", 2, "Python", 3] 출력

# # li_3 = li_1+li_2
# # li_3[1] =li_2[0]
# # li_3[3] =li_2[1]
# # li_3[4]=li_1[2]
# # li_3[5] =li_2[2]
# # print(li_3)

# li_1.insert(1, li_2[0])
# li_1.insert(3,li_2[1])
# li_1.insert(5, li_2[2])

# print(li_1)

# # li_1.insert(1, li_2[0])
# # li_1.insert(3,li_2[1])
# # li_1.append(li_2[2])


# scores = [] # scores = list()라고 해도된다 / 비어있는 리스트 생성

# scores.append(int(input("영어 점수:" ))) # input()에 입력한 것은 문자형을 나온다
# scores.append(int(input("국어 점수:" )))
# scores.append(int(input("수학 점수:" )))
              
# avg = (scores[0]+scores[1]+scores[2])/3
# print(avg)

# #sum()은 리스트의 요소를 모두 더한다.
# # avg = sum(scores)/3 # sum()은 들어간 값이 숫자형이어야 한다

# if avg>=91 and avg<=100:
#     print("A")
# elif avg>=81 and avg<=90:
#     print("B")
# elif avg>=71 and avg<=80:
#     print("c")
# elif avg>=61 and avg<=70:
#     print("D")
# else:
#     print("F")

# 나이와 가지고 있는 돈을 입력받는다.
# 가지고 있는 돈으로 물건별로 각각 몇개 살 수 있는지와 잔돈을 출력한다.
# 물건1의 가격은 1000원이다.
# 물건 2의 가격은 50원이다.
# 물건 3의 가격은 120원이다.
age = input("나이: ")
money = int(input("가지고 있는 돈: "))

a = [1000, 50, 120]

print(money // a[0])
print(money // a[1])
print(money // a[2])

print(money % a[0])
print(money % a[1])
print(money % a[2])


# print(money-((int(money/a[0]))*a[0]))
# print(money-((int(money/a[1]))*a[1]))
# print(money-((int(money/a[2]))*a[2]))

# print(str(money/int(a[0]))+str(money-((money/int(a[0]))*int(a[0]))))
# print(str(money/int(a[1]))+str(money-((money/int(a[1]))*int(a[1]))))
# print(str(money/int(a[2]))+str(money-((money/int(a[2]))*int(a[2]))))
