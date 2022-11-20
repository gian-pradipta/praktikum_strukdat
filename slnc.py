#node linked list
class Node:
    def __init__(self, value):
        self.next = None
        self.data = value
        
 #fungsi untuk partisi quicksort
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
		
#Single Linked List Non Circular
class SLNC:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0
    def __str__(self):
    	if self.size == 0:
    		return 'Kosong'
    	else:
    		result = 'Linked list ' + str(self.size) + ' data: \n['
    		helper = self.head 
    		while helper != None:
    			if helper == self.head:
    				result += f"{helper.data}"
    				helper = helper.next
    			else:	
	    			result += f", {helper.data}"
	    			helper = helper.next
    		return result + "]"
    def __len__(self):
    	return self.size
    def insert_head(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            node_baru.next = self.head
            self.head = node_baru
        self.size = self.size + 1

    def insert_tail(self, new_data):
        node_baru = Node(new_data)
        if self.size == 0:
            self.head = node_baru
            self.tail = node_baru
        else:
            self.tail.next = node_baru
            self.tail = node_baru
        self.size = self.size + 1

    def insert_mid(self, new_data, index):
        if self.size == 0 or index <= 0:
            self.insert_head(new_data)
        elif index >= self.size:
            self.insert_tail(new_data)
        else:
            node_baru = Node(new_data)
            helper = self.head
            for i in range(index-1):
                helper = helper.next
            node_baru.next = helper.next
            helper.next = node_baru
            self.size = self.size + 1
    def delete_head(self):
    	if self.size == 0:
    		return None
    	elif self.size == 1:
    		hapus = self.head.data
    		self.head = None
    		self.tail = None
    		self.size -= 1
    		return hapus
    	else:
    		hapus = self.head.data
    		hapus_2 = self.head
    		self.head = self.head.next
    		del hapus_2
    		self.size -= 1
    		return hapus
    def delete_tail(self):
    	if self.size <= 1:
    		return self.delete_head()
    	else:
    		hapus = self.tail
    		hapus_2 = self.tail.data
    		helper = self.head
    		while helper != self.tail:
    			helper = helper.next
    		self.tail = helper
    		self.tail.next = None
    		del hapus
    		self.size -= 1
    		return hapus_2
    def delete_mid(self, index):
    	if self.size <= 1:
    		return self.delete_head()
    	elif index <= 0:
    		return self.delete_head()
    	elif index >= self.size-1:
    		return self.delete_tail()
    	else:
    		helper = self.head
	    	for i in range(index-1):
	    		helper = helper.next
	    	hapus = helper.next
	    	hapus_2 = helper.next.data
	    	helper.next = hapus.next
	    	del hapus
	    	self.size -= 1
	    	return hapus
    def get_data(self, index):
        if self.size == 0:
            return None
        elif self.size == 1 or index <= 0:
            return self.head
        elif index >= self.size:
  
            return self.tail
        else:
            helper = self.head
            for i in range(index):
                helper = helper.next
            return helper
    def quicksort(self, low, high):
    	if low < high:
            end = partition(self, low, high)
            self.quicksort(low, end-1)
            self.quicksort(end, high)
       
if __name__ == "__main__":    	
	slnc = SLNC()
	for i in [1,3,2,10,5,3,2,7,8,9,5,0,12,34,5,5,0,0,0,0,0,0,6]:
		slnc.insert_tail(i)
	print("DATA SEBELUM DI-SORT")
	print(slnc)
	print()
	print("DATA SESUDAH DI-SORT")
	slnc.quicksort(0, len(slnc)-1)
	print(slnc)
	