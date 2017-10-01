def map_box_api(csv_row):

	address,lat,long_ = csv_row

	lat,long_=float(lat),float(long_)

	

	# my map_box account apikey 

	map_box_key="pk.eyJ1IjoibW9oYW4wMCIsImEiOiJjajg0bDdudDYwOHM1MndwZmNjenp1dTduIn0.LxknjhXAQ_1n98amoXAANw"

	# below module for accesing geocoding services 

	import geocoder

	res=geocoder.mapbox(address,key=map_box_key)

	d_1 = {'address':None,'city':None,'state':None,'country':None,'county':None,'city':None,'lat':None,'lng':None}

	d_2 = {'address':None,'city':None,'state':None,'country':None,'county':None,'city':None,'lat':None,'lng':None}

	attr = d_2.keys()

	if res==None:
		print("services can't recognise this address sorry",address)
		return [1]
	if res.json==None:
		print("services error ",address)
		return [1]


	for s in attr:
		try:
			d_1[s]=res.json[s]
		except KeyError:
			pass


	response=geocoder.mapbox([lat,long_],method='reverse',key=map_box_key)
	# print(response)

	if response==None:
		print("service error for given lat,long"+" ".join(str(hh) for hh in [lat,long_]))
		return [1]
	if response.json == None:
		print("service error for given lat,long"+" ".join(str(hh) for hh in [lat,long_]))
		return [1]



	for i in attr:
		try:
			d_2[i]=response.json[i]
		except KeyError:
			pass
	# below print statements are for debugging manually u can ignore

	# print(d_2)
	# print(d_1)
	# print
	# print(d_2)

	return d_1,d_2


## below code is for manual testing only 

# address = "Suning, 2008 Yitian Rd, Futian Qu, Shenzhen Shi, Guangdong Sheng, China"

# map_box_api([address,79.73999,15.91290])