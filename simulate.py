import cache
import controller

name = "test1.trace"
f = open(name,"r")
file = open("test.result","w")
#-----read input file
action_list = []
for line in f:
	line = line.split()
	rw = line[0]
	address = int(line[1],0)
	action = (rw,address)
	action_list.append(action)
#----test 
cache_size_list = [1024, 4096, 65536, 131072]
block_size_list = [8,16,32,128]
n_way_list = ["DM","2W","4W","FA"]
write_list = ["WB","WT"]
for cache_size in cache_size_list:
	for block_size in block_size_list:
		for n in n_way_list:
			for write in write_list:
				if n == "FA":
					n_way = int(cache_size/block_size)
				elif n == "DM":
					n_way = 1
				elif n == "2W":
					n_way = 2
				else:
					n_way = 4
				set_count = int (int(cache_size/block_size)/n_way)
				simulate_cache = cache.cache(set_count,block_size,cache_size, write, n_way, n)
				controller.proccess(action_list,simulate_cache, file)
file.close()
f.close()