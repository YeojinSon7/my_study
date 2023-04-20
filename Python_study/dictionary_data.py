# # 딕셔너리 자료형
# # 이름표처럼 이름달아서 찾기
# # key-value 형태
# # key: value
# person ={"이름": "이름", "나이": 27, "점수": {"영어": 80, "국어": 90,"수학": 100}} # key와 value 자리에 다양한 자료형이 올 수 있다
# # 자바스크립트 웹/앱 에서 사용하는 json도 같은 형태로 있다
# # key값으로 찾는다 어떤 정보인지 알아보기 쉽다
# # 딕셔너리 안에 딕셔너리가 들어갈 수 있다
# print(person["나이"])
# print(person["점수"]["영어"]) # 인덱스와 달리 키로 찾는다

# dict_1 = {1: 'a'}
# dict_1['b'] = 2 # 'b': 2 key-value 쌍 추가
# dict_1[1] = 'c'
# del dict_1[1]
# print(dict_1)
# # 추가 수정 삭제 가능

dict_2 = {1: 'a', 2: 'b', 3: 'c'}
# keys() 딕셔너리에서 key만 리스트형태로 돌려준다.
# dict_keys=dict_2.keys()
# print(dict_keys)

# # values()
# #딕셔너리에서 value 값만 리스트 형태로 돌려준다.
# dict_values = dict_2.values()
# print(dict_values)

# # items()
# # 딕셔너리에서 key-value 쌍을 튜플로 묶은 값을 리스트 형태로 돌려준다.
# dict_items= dict_2.items()
# print(dict_items)

# get()
# key에 대응되는 value를 돌려준다.
# key값이 존재하지 않으면 None을 돌려준다
# dict_2["나이"] 쓰면 에러난다 dict_2에 "나이"라는 key값이 없어서

# print(dict_2.get("나이")) #아예 비어있는게아니라 데이터가 없다라는 내용의 데이터가 있는것이다 다른언어에서는 null값
# print(dict_2.get("나이","나이 불명")) #뒤어 넣어준 값으로 나온다 위에꺼보다 안정적이다

# clear()
# 딕셔너리 안의 모든 요소를 삭제한다.
dict_2.clear()
print(dict_2)


