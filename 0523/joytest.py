try:
    score=int(input("請輸入學生分數(最高300分)"))
    print(score)
except ValueError:
    print("輸入錯誤請再輸入一次!")