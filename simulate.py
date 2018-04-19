import cache
import controller

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
cache_size = 1024
block_size = 8
way = 4
set_count = int (int(cache_size/block_size)/way)
write = "WB"
#-----
cache = cache.cache(set_count,block_size,cache_size,write, way)
controller.proccess(action_list,cache)