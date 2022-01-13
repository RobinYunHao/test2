def forlist (a_list):
#def a thing
    for lista in a_list:
        if isinstance(lista,list):
            forlist(lista)
        else:
            print lista


def findthing(listb ='', stra=''):
    print ("1.2")
    if isinstance(listb,list):
        print('This is a list')
    if isinstance(stra,str):
        print('yes,its a str')
    else:
        print('oh no')
