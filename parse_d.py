import re
import sys
import json
import os


file_counter = 0
all_traj = dict() 
for file in os.listdir("traj"):
  with open("traj/"+file, 'r') as myfile:   #outfile--file scope
   	data = myfile.read()
	traj_list_tmp = list()
	point_counter = 0	
	#print file
	for line in data.split('\n'):		#infile--line scope
		if "Point" in line:				#do things when it detects the point
			point_counter+=1
			line_counter = 0
			print "Point",point_counter 
			point_tmp_dict = dict()
			continue
		if "Gaussian" in line:
			break
		elif point_counter >= 1:		#points
			line_counter+=1
			
			point_tmp_dict['point'] =point_counter
			#print "first point"
			if line_counter==1 :
				print 'x',line
				point_tmp_dict['x'] =line.split('\r')[0]
			if line_counter==2 :
				print 'y',line
				point_tmp_dict['y'] =line.split('\r')[0]
			if line_counter==16 :
				print 'timeframe',line	
				timeframe =int(line.split('\r')[0])
				sec=int(timeframe/30)
				point_tmp_dict['time'] =sec
				traj_list_tmp.append(point_tmp_dict)
	all_traj[file_counter]=traj_list_tmp
	file_counter +=1
	if file_counter>3500:
		break;

with open("result_first_10min.json", "w") as outfile:
	json.dump(all_traj, outfile, indent=4)



