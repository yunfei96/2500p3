import block
import cache_set
class cache:
	total_hit = 0
	mem_read = 0
	mem_write = 0
	def __init__(self,set_count,block_size,cache_size,write, n_way):
		self.set_count = set_count
		self.block_size = block_size
		self.cache_size = cache_size
		self.cache = []
		self.write = write
		self.n_way = n_way
		i = 0
		while i< self.set_count:
			self.cache.append(cache_set.cache_set(n_way,block_size,write))
			i = i+1