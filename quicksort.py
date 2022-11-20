l = [1,3,2,10,5,3,2,7,8,9,5,0,12,34,5,5,6]
from slnc import Node, SLNC
def partition(data, low, high):
		pivot = data[high]
		l = low
		r = high - 1
		while True:
			if data[l] <= pivot:
				l += 1
			if data[r] > pivot:
				r -= 1
			if l>r:
				break
			if data[l] > pivot and data[r] <= pivot:
				data[l], data[r] = data[r], data[l]
				l += 1
				r-= 1
			if l> r:
				break
		data[l], data[high] = data[high], data[l]
		return l

def quicksort(data, low, high):
	if low < high:
		endd = partition(data, low, high)
		quicksort(data, low, endd-1)
		quicksort(data, endd, high)
quicksort(l, 0, len(l)-1)
print(l)

