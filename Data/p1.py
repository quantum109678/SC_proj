import pandas as pd 
import numpy as np 
import datetime
import csv

data1=pd.read_csv('new_sensor.csv')
des1=data1.describe()


min_lat=des1['latitude']['min']
max_lat=des1['latitude']['max']
min_lon=des1['longitude']['min']
max_lon=des1['longitude']['max']

diff_lat=max_lat - min_lat
diff_lon=max_lon - min_lon

dlat=diff_lat/100
dlon=diff_lon/100

st_h=8

print(st_h)
reord8=[[0 for x in range(100)] for y in range(100)]
counts=[[0 for x in range(100)] for y in range(100)]
		
for i in range(data1.shape[0]):
	print(i)
	curr_lat=data1['latitude'][i]
	curr_lon=data1['longitude'][i]
	row_num=int((curr_lat - min_lat)/dlat)
	col_num=int((curr_lon - min_lon)/dlat)
	print(row_num,col_num)

	
	curr=data1['date'][i]
	curr=curr.split()
	currt=datetime.datetime.strptime(curr[1],"%H:%M:%S")
					#print(currt)
	if(currt.hour==st_h):
		reord8[row_num][col_num]+=data1['co'][i]
		counts[row_num][col_num]+=1

for x in  range(100):
	for y in range(100):
		if counts[x][y]!=0:
			reord8[x][y]=reord8[x][y]/counts[x][y]


with open("8am.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(reord8)						#print(data1['co'][i])


