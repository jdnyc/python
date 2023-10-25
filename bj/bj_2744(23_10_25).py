#영어 소문자와 대문자로 이루어진 단어를 입력받은 뒤, 대문자는 소문자로, 소문자는 대문자로 바꾸어 출력하는 프로그램을 작성

for i in input():
    if i.isupper() :
        print(i.lower(),end='')
    else:
        print(i.upper(),end='')


print("1-1칸","1-2칸","1-3칸",end = "")
print("2-1칸","2-2칸","2-3칸",sep = "")

print(input().swapcase())
