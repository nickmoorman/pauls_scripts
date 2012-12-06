#!/usr/bin/python

def sort_avg_time(inner):
	return int(inner[2]/inner[0])
def find_it(key,lists):
   for index, sublist in enumerate(lists):
       if sublist[1] == key:
            return index
import string,sys
file = sys.argv[1]
access_times = []
f = open(file, 'r')
# f = open('/tmp/test.log', 'r')
#foreach line
for line in f:
	line = string.split(line,' ')
	tier = string.split(line[6], '/')
	tmp_line = []
	tmp_line.append(1)
	skip-fields = set(['server-enabled','admin','probe',''])
	if len(tier) < 2:
		continue
	if tier[1] in skip-fields:
		continue
	# if tier[1] == 'server-enabled':
	# 	continue
	# if tier[1] == 'admin':
	# 	continue
	# if tier[1] == 'probe':
	# 	continue
	# if (tier[1] == ''):
	# 	continue 
	# print tier
	if len(tier) > 4:
		if tier[3] == 'blog_bookmarks':
			fixed_tier = tier[3]
		else:
			tier_question=string.split(tier[4],'?')
			fixed_tier=(tier[3] + '/' + tier_question[0])
	else:
		if len(tier) < 3:
			fixed_tier=tier[1]
		if len(tier) == 4:
			tier_question = string.split(tier[3],'?')
			fixed_tier=tier_question[0]
	tmp_line.append(fixed_tier)
	try:	
		tmp_line.append(int(line[10]))
	except:
		print line
		print line[10]
		continue
	# if int(line[10]) > 5000:
	# 	worst+=1
	#if service already exits: increment count && add time to total time
	index=find_it(fixed_tier,access_times)
	if (index is not None):
		access_times[index][0]+=1
		access_times[index][2]+=int(line[10])
	else:
		access_times.append(tmp_line)
access_times.sort(key=sort_avg_time,reverse=True)
print "%8s%27s%26s%8s" % ("AVG (ms)", "Service"," ", "Requests")
for i in xrange(25):
	print "%-10s %26s %28s" % (str(access_times[i][2]/access_times[i][0]), access_times[i][1], str(access_times[i][0]))
exit
