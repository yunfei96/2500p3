import block
class DM_cache:
	total_hit = 0
	mem_read = 0
	mem_write = 0
	def __init__(self,block_count,block_size,cache_size,write):
		self.block_count = block_count
		self.block_size = block_size
		self.cache_size = cache_size
		self.cache = [block.block(block_size)]*self.block_count
		self.write = write
	
