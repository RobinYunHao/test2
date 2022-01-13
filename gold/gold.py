import pickle

savegold = open('gold.game', 'wb')
gold = 0
pickle.dump(gold, savegold)
savegold.close()
