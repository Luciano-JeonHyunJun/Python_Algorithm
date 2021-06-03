a = 0.3 + 0.6
print(a)

if a == 0.9:
    print(True)
else:
    print(False)

a = 0.3 + 0.6
print(round(a, 4))

if round(a,4) == 0.9:
    print(True)
else:
    print(False)

# round는 첫번째 인자가 실수형 데이터 이고 , 두번째 인자는 (반올림하고자 하는 위치 -1)이다.
# 예를 들어 123.456을 소수점 셋째 자리에서 반올림하려면 