#!/usr/bin/python

# I'll leave this for now since you might need it later
def sort_avg_time(inner):
	return int(inner[2]/inner[0])

import string,sys
file = sys.argv[1]
access_times = {}
f = open(file, 'rU')

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
	if fixed_tier in access_times:
		old = access_times[fixed_tier]
		access_times[fixed_tier] = (old[0]+1,old[1]+int(line[10])
	else:
		access_times[fixed_tier] = (tmp_line[0],tmp_line[2])

# Close the file
f.close()