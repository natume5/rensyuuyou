import pickle

with open('pic.bin', 'rb') as p:
	l = pickle.load(p)
	print(l)
