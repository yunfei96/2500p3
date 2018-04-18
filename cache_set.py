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
		print (self.set_data[0][1].tag, end = " ")
		print (self.set_data[1][1].tag, end = "\n")
		self.increment()
		for item in self.set_data:
			if item[1].tag == tag and item[1].valid == 1:
				item[0] = 1
				return True
		return False

	def put(self,tag):
		self.set_data = sorted(self.set_data, key=itemgetter(0))
		#if the all way for the set is not full
		if self.set_data[0][0] != 0:
			index = len(self.set_data)-1
			#if it is dirty
			if self.set_data[index][1].dirty == 1 and self.write == "WB":
				self.set_data[index][1].tag = tag
				self.set_data[index][1].valid = 1
				self.set_data[index][1].dirty = 0
				self.set_data[index][0] = 1
				return self.block_size
			else:
				self.set_data[index][1].tag = tag
				self.set_data[index][1].valid = 1
				self.set_data[index][1].dirty = 0
				self.set_data[index][0] = 1
				return 0
		else:
			#print('empty')
			self.set_data[0][1].tag = tag
			self.set_data[0][1].valid = 1
			self.set_data[0][1].dirty = 0
			self.set_data[0][0] = 1
			return 0

	def increment(self):
		for item in self.set_data:
			if item[1].valid == 1:
				item[0] = item[0]+1
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
