from slnc import SLNC, Node, partition
import random

daftar = SLNC()
for i in range(50):
	daftar.insert_tail(random.randint(1,100))
print(daftar)
daftar.quicksort(0, len(daftar)-1)
print(daftar)