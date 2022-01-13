import pickle
'''with open('data.pickle','wb') as mydatasave:
    pickle.dump([1, 2.1, 'three'], mydatasave)'''
try:
    fr = open('data.pickle','rb')
    lidta = pickle.load(fr)
    print lidta
except:
    print("wrong")
finally:
    fr.close()
try:
    fa = open('data.pickle', 'ab+')
    pickle.dump('567''data.pickle')
    fg = pickle.load(fa)
    print fg
except:
    pass
finally:
    fa.close()