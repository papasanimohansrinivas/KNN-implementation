def compare_distances(b,c,lat,lon):
	import geopy

	from geopy.distance import vincenty

	from geopy.distance import great_circle

	d= vincenty((b,c),(lat,lon)).miles

	# print d
	return d
