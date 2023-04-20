weather = "맑음" #weather 변수에 값 할당
print("비가 오니요?", weather == "비") #문자열, 조건식 출력
if weather == "비":# weather의 값이 "비"와 같으면 조건식이 True 이므로 코드 블록 실행
    print("우산을 가져간다.")
elif weather == "맑음":
    print("날씨가 좋다")
else:
    print("우산을 가져가지 않는다.")

#if elif else 에서는 if 가 elif 가 해당되면 그다음으로 안가고 프로그램 끝난다
