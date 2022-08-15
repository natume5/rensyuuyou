import pickle

l = [1, 2, 3, 4, 5]
with open('pic.bin', 'wb') as p:
	pickle.dump(l, p)
