import math
import cache_set
#------below is controller
def proccess(action_list,cache,file):
	for i in action_list:
		h = hit(i[0],i[1],cache)
	for i in cache.cache:
		cache.mem_write = cache.mem_write + i.release_dirty()
	file.write(str(cache.cache_size)+ '	'
		+ str(cache.block_size)+'	'
		+ str(cache.n)+'	'
		+ str(cache.write)+ '	'
		+ str(round(cache.total_hit/len(action_list),2))+'	' 
		+ str(cache.mem_read)+'	'
		+ str(cache.mem_write)
		+ '\n')

def hit(action,memory_address,cache):
	set_index = math.floor(memory_address/cache.block_size)%cache.set_count 
	tag = math.floor(memory_address/(cache.cache_size/cache.n_way))
	#print(tag)
	#if it is a cache hit
	if cache.cache[set_index].search_hit(tag):
		cache.total_hit = cache.total_hit+1
		if action == "write":
			#write back to memory
			if cache.write == "WT":
				cache.mem_write = cache.mem_write+4
			#mark it as dirty block
			else:
				cache.cache[set_index].set_dirty(tag)
	#if it is a cache miss
	else:
		#read in new block of memory
		cache.mem_read = cache.mem_read+cache.block_size
		#put the new data
		cache.mem_write = cache.mem_write + cache.cache[set_index].put(tag)
		#write the data back to memory
		if action == "write":
			if cache.write == "WT":
				cache.mem_write = cache.mem_write+4
			else:
				cache.cache[set_index].set_dirty(tag)
		
		
