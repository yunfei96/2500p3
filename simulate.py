import DM_cache
import DM_controller

f = open("test1.trace","r")
#-----read input file
action_list = []
for line in f:
	line = line.split()
	rw = line[0]
	address = int(line[1],0)
	action = (rw,address)
	action_list.append(action)
#----test 
cache_size = 1*1024
block_size = 128
block_count = int(cache_size/block_size)
write = "WB"
#-----
cache = DM_cache.DM_cache(block_count,block_size,cache_size,write)
DM_controller.proccess(action_list,cache)