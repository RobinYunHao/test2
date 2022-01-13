# -*- coding:utf-8 -*-
from TestGame.magicthing import Magic
# from magicthing import Magic
import random
import tkinter as tk
import easygui as g

# from lisy import forlist, findthing
window = tk.Tk()
window.title("炼金大冒险2.0")  # window标题
window.maxsize(300, 200)  # window的大小
window.minsize(500, 450)  # 通过设置最大最小一样，可以实现window不可缩放大小
var = tk.StringVar()
c = tk.StringVar()
Defense = 5
De = 1


def 开始():
    window.destroy()


def 二点零():
    var.set("开始界面图形化")


l = tk.Label(window, text='欢迎来到炼金世界', bg='blue', font=('Arial', 13), width=40, height=3)
e = tk.Label(window, textvariable=var, bg='yellow', fg='blue', font=('Arial', 13), width=55, height=3)
l.place(x='65', y='1')
e.place(x='1', y='61')
m = tk.Button(window, text='开始游戏', fg='blue', font=('Arial', 13), width=10, height=4, command=开始)
m.place(x='195', y='135')
i = tk.Button(window, text='2.0', font=('Arial', 13), width=8, height=3, command=二点零)
i.place(x='1', y='250')
window.mainloop()
z = 0
p = g.ccbox(msg="DO you want to see?", title='炼金大冒险2.0', choices=('看', '不看'))
op = int(p)
if op == 1:
    print("BE.1 finish the lake and a new monster:dragon")
    print("BE.2 finish the wood")
    print("1.0: a new secret ")
    print("1.1: repair a bug")
    print("1.2: finish a secret and a secret monster")
    print("1.3: repair a bug")
    print("1.31: finish 1.2 secret and repair secret's bug")
    print("1.4: a new boss: devil")
    print("1.41: a test")
    print("1.5: new era")
    print("1.6: a new map: city")
    print("1.7: repair coin bug")
    print("1.71: test new map")
    print("1.72: repair a bug")
    print("1.8: finish new map and two new monsters")
    print("1.9 test shop")

else:
    pass

yincang = random.randint(1, 5)
fate = random.randint(1, 2)
ma = Magic()
list1 = [[0 for i in range(4)] for j in range(4)]
print("Where are you going?")
print("There are many things in this wood.")
print("game is beginning")
hp = 100
coin = 0
list1[1][1] = 1
med = 1
secret = g.integerbox(msg="Do you know the secret?", title='密码', lowerbound=1, upperbound=1000000)
if secret == 1723:
    med += 1000
    print("You know the secret point")
else:
    pass
secret1 =  g.integerbox(msg="Do you know the other secret?", title='密码', lowerbound=1, upperbound=1000000)
if secret1 == 384:
    yincang = 10
    fate = 10
    print("Yes")
else:
    pass
while hp >= 1:
    fg = [1, 2, 3, 4]
    coin, med=ma.shop(coin, med)
    ch = g.choicebox(msg="1=NBE-Lake 2 = the wood beside your home,3 = the city,4 = the fire world(need 50 coin)", choices=fg)
    if ch == '1':
        print('Well,you come to the lake')
        print('You can fight with everything,1 or 2')
        fight2 = 0
        lake2 = 0
        end3 = 0
        end3 = ma.fight0(fight2, lake2, end3, 3)
        if end3 == 1:
            print("You meet a lion")
            hp1 = 85
            while hp1 >= 1 and hp >= 1:
                end1 = input("fight or med")
                if end1 == "1":
                    fight1 = 2
                    m1 = random.randint(1, 3)
                    print (m1)
                    if fight1 == m1:
                        print("Yes!")
                        hp -= 10
                        hp1 -= 50
                    else:
                        print('No!')
                        hp -= 20
                        hp1 -= 20
                elif end1 == 2:
                    hp, med = ma.medi(hp, med)
                ma.findhp(hp, hp1)
            c = input("Do you want to use the No.1?")
            if c == 1:
                coin, list1 = ma.magict(list1, coin, 30)
            else:
                print("Well")
            coin = ma.over(hp, coin, 30)
            coin = ma.pcoin(coin)
            list1[1][3] = 1
            print(list1)
        else:
            print("You meet the dog")
            hp2 = 40
            while hp2 >= 1 and hp >= 1:
                end2 = input("fight or med")
                if end2 == 1:
                    fight3 = 2
                    m2 = random.randint(1, 3)
                    if fight3 == m2:
                        print("Yes!")
                        hp2 -= 30
                        hp -= 5
                    else:
                        hp2 -= 19
                        hp -= 15
                        print("No!")
                elif end2 == 2:
                    hp, med = ma.medi(hp, med)
                ma.findhp(hp, hp2)
                n2 = input("Do you want to use the No.2?")
                if n2 == 1:
                    list1, hp2 = ma.mag2(list1, hp2)
                else:
                    pass
            c1 = input("Do you want to use the No.1?")
            if c1 == 1:
                coin, list1 = ma.magict(list1, coin, 15)
            else:
                print("Well")
            coin = ma.over(hp, coin, 15)
            ma.pcoin(coin)
    elif yincang == fate:
        print("You are so lucky!")
        yincang = 0
        fate = 3
        print("You meet the angel")
        hpa = 170
        while hp >= 1 and hpa >= 1:
            end1 = input("fight or med")
            if end1 == 1:
                fight1 = 2
                m1 = random.randint(1, 3)
                if fight1 == m1:
                    print("Yes!")
                    hp -= 0
                    hpa -= 55
                else:
                    print('No!')
                    hp -= 70
                    hpa -= 40
            elif end1 == 2:
                hp, med = ma.medi(hp, med)
            n2 = input("Do you want to use the No.2?")
            if n2 == 1:
                list1, hp4 = ma.mag2(list1, hpa)
            else:
                pass
            ma.findhp(hp, hpa)
        coin = ma.over(hp, coin, 150)
        ma.pcoin(coin)
        if hp >= 1:
            med += 5
            list1[2][2] = 1

    elif ch == '2' and fate != yincang:
        print("You go to the wood")
        choice = input('choose one')
        print('You can fight with everything,1 or 2')
        fight5 = 0
        wood = 0
        end4 = 0
        end4 = ma.fight0(fight5, wood, end4, 4)
        if end4 == 1:
            print("You meet a dragon!")
            hp4 = 135
            while hp >= 1 and hp4 >= 1:
                end1 = input("fight or med")
                if end1 == 1:
                    fight1 = 2
                    m1 = random.randint(1, 3)
                    if fight1 == m1:
                        print("Yes!")
                        hp -= 20
                        hp4 -= 57
                    else:
                        print('No!')
                        hp -= 40
                        hp4 -= 30
                elif end1 == 2:
                    hp, med = ma.medi(hp, med)
                n2 = input("Do you want to use the No.2?")
                if n2 == 1:
                    list1, hp4 = ma.mag2(list1, hp4)
                else:
                    pass
                ma.findhp(hp, hp4)
            coin = ma.over(hp, coin, 100)
            ma.pcoin(coin)
            med += 1
        else:
            print("You meet a wolf")
            hp3 = 70
            while hp3 >= 1 and hp >= 1:
                end5 = input("fight or med")
                if end5 == 1:
                    fight1 = 2
                    m1 = random.randint(1, 3)
                    if fight1 == m1:
                        print("Yes!")
                        hp -= 15
                        hp3 -= 45
                    else:
                        print('No!')
                        hp -= 30
                        hp3 -= 30
                elif end5 == 2:
                    hp, med = ma.medi(hp, med)
                n2 = input("Do you want to use the No.2?")
                if n2 == 1:
                    list1, hp3 = ma.mag2(list1, hp3)
                else:
                    pass
                ma.findhp(hp, hp3)
            coin = ma.over(hp, coin, 25)
            ma.pcoin(coin)
    elif ch == '3' and fate != yincang:
        print("You go to the city")
        print("You meet  a  zombie")
        hp5 = 60
        hp, coin, list1, med = ma.testfight(hp, hp5, med, 20, list1, 30, 45, 35, coin, 1, 30, Defense)
        z += 1
        if z == 5:
            print('You meet the zombie 5')
            hpz = 300
            hp, coin, list1, med = ma.testfight(hp, hpz, med, 25, list1, 20, 200, 30, coin, 1, 150, Defense)
    elif ch == '4' and fate != yincang and coin >= 50:
        print("You go to the fire world!")
        fight6 = 0
        fire = 0
        end6 = 0
        end6 = ma.fight0(fight6, fire, end6, 3)
        if end6 == 1:
            print("You meet the fire king")
            hpf = 120
            hp, coin, list1, med = ma.testfight(hp, hpf, med, 20, list1, 40, 59, 29, coin, 2, 85, Defense)
        else:
            print("You meet the fire !")
            hp6 = 60
            hp, coin, list1, med = ma.testfight(hp, hp6, med, 20, list1, 35, 59, 29, coin, 2, 40, Defense)
    else:
        pass
if coin >= 130:
    g.msgbox("You meet the devil!")
    ch = g.ccbox(msg="Give him 50 coin or kill him", choices=('1', '2'))
    if ch == 1:
        coin -= 50
    else:
        hp = 100
        hpd = 150
        while hp >= 1 and hpd >= 1:
            end5 = input("fight or med")
            if end5 == 1:
                fight1 = 2
                m1 = random.randint(1, 3)
                if fight1 == m1:
                    print("Yes!")
                    hp -= 20
                    hpd -= 100
                else:
                    print('No!')
                    hp -= 45
                    hpd -= 20
            elif end5 == 2:
                hp, med = ma.medi(hp, med)
            n2 = input("Do you want to use the No.2?")
            if n2 == 1:
                list1, hpd = ma.mag2(list1, hpd)
            else:
                pass
            ma.findhp(hp, hpd)
        coin = ma.over(hp, coin, 105)
        ma.pcoin(coin)

else:
    pass

print("Game over")
print(coin)
