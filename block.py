class block:
	def __init__(self,block_size):
		self.data = [None]*block_size
		self.valid = 0
		self.tag = 0
		self.frequency = 0
		self.dirty = 0