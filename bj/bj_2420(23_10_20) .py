#첫째 줄에 두 도메인의 유명도 N과 M이 주어진다. (-2,000,000,000 ≤ N, M ≤ 2,000,000,000
#첫째 줄에 두 유명도의 차이 (|N-M|)을 출력한다.

A,B = map(int, input().split())

if A>B:
    print(A-B)
elif A<B:
    print(B-A)