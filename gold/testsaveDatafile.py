from testLoadDataFile import getValueInFile
#gold = 'gold.game'
money2 = getValueInFile("gold", "gold.game")
print (">>>>>>>>>>>>>>the value is :" + str(money2))
print str(money2)
#with open('gold.game','a+') as test_file:
money2 += 1
print str(money2)
