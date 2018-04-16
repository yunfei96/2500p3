import block
import DM_cache
import math
#------below is DM controller
def proccess(action_list,cache):
	for i in action_list:
		h = hit(i[0],i[1],cache)
	print(cache.total_hit/len(action_list))
	print(cache.mem_read)
	print(cache.mem_write)

def hit(action,memory_address,cache):
	block_index = math.floor(memory_address/cache.block_size)%cache.block_count 
	block_offset = memory_address%cache.block_size 
	tag = math.floor(memory_address/cache.cache_size)

	#if it is a cache hit
	if (cache.cache[block_index].tag == tag) and (cache.cache[block_index].valid == 1):
		cache.total_hit = cache.total_hit+1
		if action == "write":
			#write back to memory
			if cache.write == "WT":
				cache.mem_write = cache.mem_write+4
			#mark it as dirty block
			else:
				cache.cache[block_index].dirty = 1
	#if it is a cache miss
	else:
		#write the data back to memory
		if action == "write":
			if cache.write == "WT":
				cache.mem_write = cache.mem_write+4
			else:
				cache.cache[block_index].dirty = 1
		#if it is dirty block
		if cache.write == "WB" and cache.cache[block_index].dirty == 1:
				cache.mem_write = cache.mem_write+cache.block_size
		#read in new block of memory
		cache.mem_read = cache.mem_read+cache.block_size
		cache.cache[block_index].tag = tag
		cache.cache[block_index].valid = 1
		cache.cache[block_index].dirty = 0
		
