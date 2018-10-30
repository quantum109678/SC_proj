import pandas as pd 
import numpy as np 
import datetime

data1=pd.read_csv('data1.csv')
des1=data1.describe()


min_lat=des1['latitude']['min']
max_lat=des1['latitude']['max']
min_lon=des1['longitude']['min']
max_lon=des1['longitude']['max']

diff_lat=max_lat - min_lat
diff_lon=max_lon - min_lon

dlat=diff_lat/100
dlon=diff_lon/100
print(dlat,dlon)
print(des1)
tar=data1['date'][3]
tar=tar.split()
print(tar)
currt=datetime.datetime.strptime(tar[1],"%H:%M:%S")
st_h=currt.hour
values=0
count=0
st_lat=min_lat+dlat*50
end_lat=min_lat+dlat*51
st_lon=min_lon+dlon*50
end_lon=min_lon+dlon*51
print(type(st_lon))
print(st_lat,end_lat,st_lon,end_lon)
for i in range(data1.shape[0]):
	#print(i)
	if(data1['latitude'][i] <= 50 and data1['latitude'][i]>=0):
	#if(data1['latitude'][i] >= st_lat and data1['latitude'][i] < end_lat):
		#if(data1['longitude'][i] >= st_lon and data1['longitude'][i] < end_lon):
		print(i,data1['latitude'][i])
		#curr=data1['date'][i]
		#curr=curr.split()
		#currt=datetime.datetime.strptime(curr[1],"%H:%M:%S")
		#if(currt.hour==st_h):
		#	values+=data1['co'][i]
		#	count+=1
if(count!=0):
	print(values/count,count)

