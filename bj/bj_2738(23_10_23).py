#N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성

N,M=map(int, input().split())

a=[]
b=[]

#a 행렬을 띄어쓰기로 구분하여 2차원 행렬 생성
for i in range(N):
    a.append(list(map(int, input().split())))

#b 행렬을 띄어쓰기로 구분하여 2차원 행렬 생성
for i in range(N):
    b.append(list(map(int,input().split())))


for i in range(N):
    for j in range(M):
        result = a[i][j]+b[i][j]
        print(result, end=" ")
    print()