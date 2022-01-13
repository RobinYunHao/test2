from shujujiegou.findlist import findthing
list1 = [[0 for i in range(11)] for j in range(11)]
list1[1][2] = 1
list1[2][3] = 2
m = 0
list7 = [[0 for i in range(11)] for j in range(11)]

count = 1
number = 0
o = 0
p = 0
for list_ in list1:
    for list3_ in list_:
        print (list3_)
        print ("d================" + str(count))
        list4 = int(list3_)
        print (list4)
    o += 1
    for k in list_:
        i = int(k)
        if i != 0:

            m += 1
        else:
            pass
    print ("m = " + str(m))
for list6 in list1:
    lists = [[0 for w in range(3)] for l in range(m + 1)]
    print (lists)
    lists[0][0] = 11
    lists[0][1] = 11
    lists[0][2] = m
h = 0
for list8 in list1:
    for l9 in list8:
        if l9 != 0:
            lists[count][2] = l9
            lists[count][1] = number
            count += 1
        else:
            pass
        number += 1
for list5 in lists:
    print(list5)







