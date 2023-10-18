# 두 정수 A와 B를 입력받은 다음 A+B를 출력하는 프로그램 작성

A, B = input().split()

x = int(A)
y = int(B)

print(x+y)

#split 함수
# 구분 기호를 기반으로 문자열 분리
text = "apple,banana,orange"
result = text.split(',')
print(result)  # 출력: ['apple', 'banana', 'orange']

# 공백을 기반으로 문자열 분리
text = "one two three"
result = text.split()
print(result)  # 출력: ['one', 'two', 'three']

# maxsplit 인수 사용
text = "apple,banana,orange"
result = text.split(',', 1)
print(result)  # 출력: ['apple', 'banana,orang]