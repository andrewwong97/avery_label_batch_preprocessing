# Andrew Wong
# 
# Wanted to prepare Avery labels for an event,
# but batch processing in Illustrator does not
# auto increment. So the next best thing was to
# format each line as 8 guest names.

import csv

f = csv.reader(open('Guestlist.csv','rb'))

data = [row for row in f]

out_list = []
counter = 0
for start in xrange(1, len(data), 8):
	row = []
	if start + 7 < len(data):
		end = 8
	else:
		end = len(data) - start
	for i in xrange(0,end):
		if data[start+i][0].islower():
			temp_first = data[start+i][0][0].upper() + data[start+i][0][1:]
			temp_last = data[start+i][1][0].upper() + data[start+i][1][1:]
			data[start+i][0] = temp_first
			data[start+i][1] = temp_last
		row.append(' '.join(data[start+i]))
	out_list.append(row)
	counter += 1
	print counter, 'row added'

headers = ['name' + str(i) for i in xrange(1,9)]

with open('Formatted_Guestlist.csv', 'wb') as out:
	writer = csv.writer(out)
	writer.writerow(headers)
	for i in out_list:
		writer.writerow(i)
	print 'Finished formatting'