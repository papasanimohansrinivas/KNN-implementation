def dependencies_verification():	

	import pip

	try:
		import geocoder 
	except ImportError:
		print("no geocoder")
		print("please wait.... intalling dependencies")
		pip.main(['intstall','geocoder'])
		dependencies_verification()