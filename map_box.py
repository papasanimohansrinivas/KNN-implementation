def map_box_api(row):

	address,lat,long_ = row

	lat,long_=float(lat),float(long_)

	

	# my map_box account apikey 

	map_box_key="pk.eyJ1IjoibW9oYW4wMCIsImEiOiJjajg0bDdudDYwOHM1MndwZmNjenp1dTduIn0.LxknjhXAQ_1n98amoXAANw"


	import geocoder

	res=geocoder.mapbox(address,key=map_box_key)

	d_1 = {'address':None,'city':None,'state':None,'country':None,'county':None,'city':None,'lat':None,'lng':None}

	d_2 = {'address':None,'city':None,'state':None,'country':None,'county':None,'city':None,'lat':None,'lng':None}

	attr = d_2.keys()

	if res==None:
		print(address,"res is none")
		return [1]
	if res.json==None:
		print(address,"res.json is none")
		return [1]


	for s in attr:
		try:
			d_1[s]=res.json[s]
		except KeyError:
			pass


	response=geocoder.mapbox([lat,long_],method='reverse',key=map_box_key)
	# print response



	for i in attr:
		try:
			d_2[i]=response.json[i]
		except KeyError:
			pass
	# print d_2
	# print d_1
	# print 
	# print d_2

	return d_1,d_2



# add = "Suning, 2008 Yitian Rd, Futian Qu, Shenzhen Shi, Guangdong Sheng, China"

# map_box_api([add,79.73999,15.91290])

# k,m=[1]