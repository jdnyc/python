#어떤 사람의 C언어 성적이 주어졌을 때, 평점은 몇 점인지 출력하는 프로그램을 작성하시오.
#A+: 4.3, A0: 4.0, A-: 3.7
#B+: 3.3, B0: 3.0, B-: 2.7
#C+: 2.3, C0: 2.0, C-: 1.7
#D+: 1.3, D0: 1.0, D-: 0.7
#F: 0.0

score = input()

if score=="A+":
    print("4.3")
elif score=="A0":
    print("4.0")
elif score=="A-":
    print("3.7")
elif score=="B+":
    print("3.3")
elif score=="B0":
    print("3.0")
elif score=="B-":
    print("2.7")
elif score=="C+":
    print("2.3")
elif score=="C0":
    print("2.0")
elif score=="C-":
    print("1.7")
elif score=="D+":
    print("1.3")
elif score=="D0":
    print("1.0")
elif score=="D-":
    print("0.7")
elif score=="F":
    print("0.0")