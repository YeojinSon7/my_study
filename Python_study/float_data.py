# 실수형 float형 (둥둥떠다닌다)
# 1.123 2.789 같은거
# 0.1 + 1.1 == 1.2 false가 나온다 오차때문에
print(0.1 + 1.1)
# 실수형을 정수형으로 바꾸는게 좋다  
# 실수형 변환 함수
# float()
# int(2.5) 같은걸 잘 안쓴다 결과는 2가 나오고 뒤에 소수점 아래 숫자는 날라간다

float_value = float(input("실수 입력:"))
print(float_value) 
#2 입력하면 2.0이 나온다 둘이 같은거고 표현만 다르다
# 0.1이 2진법으로 하면 무한 소수가 된다 그래서 오차값이 생긴다 -> 실제로 미군에서 이와 관련하여 미사일 방어 시스템에 오류가 생겨 사람이 사망하는 일이 있었다