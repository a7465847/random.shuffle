import random
win = 0
lose = 0
for times in range(0, 100000) :
    #準備門
    doors = ["羊","車","羊"]
    random.shuffle(doors)
    print(doors)

    #準備選
    c = random.randint(0, 2)
    print("參賽選:", doors[c])
    del doors[c]
    print("剩下門:",doors)

    #主持人開一門出來
    doors.remove("羊")
    print("最後剩下的門",doors)

    #輸贏
    if doors[0] == "車" :
        win = win + 1
        print("我贏了")
    else:
        lose = lose + 1
        print("我輸了")

print("贏次數:",win,"次")
print("輸次數:",lose,"次")
total = win + lose
print("贏機率:",win / total * 100,"%")
print("輸機率:",lose / total * 100,"%")