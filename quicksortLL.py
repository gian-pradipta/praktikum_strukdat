l = [1,3,2,10,5,3,2,7,8,9,5,0,12,34,5,5,6]
from slnc import Node, SLNC
def partition(data, low, high):
		pivot = data.get_data(high)
		l = low
		r = high - 1
		while True:
			if data.get_data(l).data <= pivot.data:
				l += 1
			if data.get_data(r).data > pivot.data:
				r -= 1
			if l>r:
				break
			if data.get_data(l).data> pivot.data and data.get_data(r).data <= pivot.data:
				kiri = data.get_data(l)
				kanan = data.get_data(r)
				kiri.data, kanan.data = kanan.data, kiri.data
				l += 1
				r-= 1
			if l> r:
				break
		data.get_data(l).data, data.get_data(high).data= data.get_data(high).data, data.get_data(l).data
		return l

def quicksort_linked_list(data, low, high):
	if low < high:
		endd = partition(data, low, high)
		quicksort_linked_list(data, low, endd-1)
		quicksort_linked_list(data, endd, high)
		
ll = SLNC()
for i in l:
	ll.insert_tail(i)
print(ll)
quicksort_linked_list(ll, 0, len(ll) - 1)
print(ll)