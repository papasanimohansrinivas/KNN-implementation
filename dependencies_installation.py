def dependencies_verification():	

	try:
		import geocoder 
	except ImportError:
		print("no geocoder module")
		print("use below cmds to install geocoder in ubuntu ")
		print("step 1")
		print("sudo apt-get install python3-setuptools")
		print("step 2")
		print("sudo easy_install3 pip")
		print("step 3")
		print("sudo pip3 install geocoder")
		print("then again run python3 geofencingValidator_.py location-for-dev.csv output_filename.csv")