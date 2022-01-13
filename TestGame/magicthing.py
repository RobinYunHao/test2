# -*- coding:utf-8 -*-
import random
import easygui as ea


class Magic:
    def medi(self, hp_, med_):
        if med_ >= 1:
            hp_ += 50
            med_ -= 1
            print("Use the med")
            print("Your hp is" + str(hp_))
        else:
            print("You don't have med ")
        return hp_, med_

    def magict(self, list1, coin_, coin):
        if list1[1][1] == 1:
            print("You use the coin! ")
            coin_ += coin
            list1[1][1] = 0
        else:
            print("You don't have")
        return coin_, list1

    def over(self, hp, coin, c):
        if hp >= 1:
            ea.msgbox('win!')
            coin += c
        else:
            ea.msgbox('looser!')
        return coin

    def mag2(self, list1, hp1):
        if list1[1][3] == 1:
            hp1 -= 30
            list1[1][3] = 0
        else:
            ea.msgbox("You don't have")
        return list1, hp1

    def fight0(self, one, two, three, four):
        one = 2
        two = random.randint(1, four)
        if one == two:
            three = 1
        else:
            three = 2
        return three

    def findhp(self, hp, mhp):
        ea.msgbox("Your hp is" + str(hp) + '     \n' + "Monster's hp is" + str(mhp))

    def pcoin(self, coin):
        ea.msgbox("You have" + str(coin))

    def angel(self, list1, coin, hp, point, hp2, med):
        if list1[2][2] == 1:
            coin -= point
            hp += point
            hp2 -= point
            med = point * 0.05
            return coin, hp, hp2, med
            list1[2][2] = 0
        else:
            pass

    def devil(self, list1, hp, hp2, hpv):
        if list1[2][1] == 1:
            hp -= hpv
            hpe = hpv * 2
            hp2 -= hpe
            return hp, hp2
            list1[2][1] = 0
        else:
            pass

    def testfight(self, hp, hp1, med, hp_, list1, hp_1, hp1_, hp1_1, coin, power, coin_, Defense):
        hp__ = hp_ - Defense
        hp__1 = hp_1 - Defense
        while hp >= 1 and hp1 >= 1:
            end5 = ea.buttonbox(msg="fight or med", title="炼金大冒险2.0", choices=('fight', 'med', 'use thing'))
            if end5 == 'fight':
                fight1 = 2
                m1 = random.randint(1, 3)
                if fight1 == m1:
                    ea.msgbox("Yes!")
                    hp -= hp__
                    hp1 -= hp1_
                else:
                    ea.msgbox('No!')
                    hp -= hp__1
                    hp1 -= hp1_1
            elif end5 == 'med':
                hp, med = Magic().medi(hp, med)
            elif end5 == 'use thing':
                list_ = ['虎爪', '天使之翼']
                ch =ea.choicebox(msg='use one', title='炼金大冒险2.0', choices=list_)
                if ch == '狮牙':
                    list1, hp1 = Magic().mag2(list1, hp1)
                elif ch == '天使之翼':
                    pass
            if power == 1 and hp1 <= 100:
                hp1 += 10
            else:
                pass
            if power == 2 and hp1 >= 1:
                hp -= 5
            Magic().findhp(hp, hp1)
        coin = Magic().over(hp, coin, coin_)
        Magic().pcoin(coin)
        return hp, coin, list1, med

    #    def power(self,No):
    def shop(self, coin, med):
        if coin >= 30:
            pr = ea.buttonbox(msg="what do you want to buy?", title="商店", choices=('药水', '不买'))
            if pr == '药水':
                coin -= 30
                med += 1
                ea.msgbox("30yuan")
        else:
            pass
        return coin, med
