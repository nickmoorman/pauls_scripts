#!/opt/cbsi-python2.7/bin/python
import string,sys,operator,pprint,string

# I'll leave this for now since you might need it later

def add_tier_access_times(fixed_tier,access_times,tmp_line,line):
	if fixed_tier in access_times:
			old = access_times[fixed_tier]
			access_times[fixed_tier] = (old[0]+1,old[1]+int(line[10]))
	else:
		access_times[fixed_tier] = (tmp_line[0],tmp_line[2])
	return access_times

def find_service_name(tier):
	skip_fields = set(['server-enabled','admin','probe',''])
	fixed_tier = -1

	if len(tier) < 2:
		return fixed_tier
	if tier[1] in skip_fields:
		return fixed_tier
		
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
	return fixed_tier

def sort_avg_time(inner):
	return int(inner[1][1]/inner[1][0])

def build_dictionary(file,dict):
	access_times = {}
	for line in f:
		line = string.split(line,' ')
		tier = string.split(line[6],'/')
		tmp_line = []
		tmp_line.append(1)
		
		fixed_tier=find_service_name(tier)
		if fixed_tier == -1:
			continue

	  # Initialize tmp_line
		tmp_line.append(fixed_tier)

	  # Do whatever this does
		try:	
			tmp_line.append(int(line[10]))
		except:
			print line
			print line[10]
			continue
		

		# Check if this service has been used already
		# If so, increment the usage count and sum to total access time
		# If not, initialize
		access_times =  add_tier_access_times(fixed_tier,access_times,tmp_line,line)

	return access_times

file = sys.argv[1]
access_times = {}
f = open(file, 'rU')

access_times = build_dictionary(f,access_times)

access_times=sorted(access_times.iteritems(), key=sort_avg_time)

print_me = []

print_me.append(['AVG (ms)','Service','Requests'])

for i in xrange(min(25,len(access_times))):
	print_me.append([str(access_times[len(access_times)-i-1][1][1]/access_times[len(access_times)-i-1][1][0]),access_times[len(access_times)-i-1][0],str(access_times[len(access_times)-i-1][1][0])])

pprint.pprint(print_me)

f.close()
