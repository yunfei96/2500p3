import block
from operator import itemgetter
class cache_set:
	def __init__(self,n_way,block_size,write):
		self.set_data = []
		self.block_size = block_size
		self.write = write
		i = 0
		while i< n_way:
			self.set_data.append([0, block.block()])
			i = i+1

	def search_hit(self,tag):
		for item in self.set_data:
			if item[1].tag == tag and item[1].valid == 1:
				item[0] = item[0] +1
				return True
		return False

	def put(self,tag):
		index = self.full()
		#if the all way for the set is full
		if index == -1:
			#find the smallest one
			sorted(self.set_data, key=itemgetter(0))
			#if it is dirty
			if self.set_data[0][1].dirty == 1 and self.write == "WB":
				self.set_data[0][1].tag = tag
				self.set_data[0][1].valid = 1
				self.set_data[0][1].dirty = 0
				self.set_data[0][0] = 0
				return self.block_size
			else:
				self.set_data[0][1].tag = tag
				self.set_data[0][1].valid = 1
				self.set_data[0][1].dirty = 0
				self.set_data[0][0] = 0
				return 0
		else:
			print('empty')
			self.set_data[index][1].tag = tag
			self.set_data[index][1].valid = 1
			self.set_data[index][1].dirty = 0
			self.set_data[index][0] = 0
			return 0

	def full(self):
		#print (self.set_data[0][1].tag, end = " ")
		#print (self.set_data[1][1].tag, end = "\n")

		i = 0;
		for item in self.set_data:
			if item[1].valid == 1:
				i = i+1
			else:
				#first index that is not full
				return i
		#return full
		return -1
	def set_dirty(self,tag):
		for item in self.set_data:
			if item[1].tag == tag:
				item[1].dirty = 1
				return True
		return False

	def check_dirty(self,tag):
		for item in self.set_data:
			if item[1].tag == tag:
				if item[1].dirty == 1:
					return True
		return False
