def parse_cmd_line():

	import sys 

	output_file,input_file=sys.argv[-1],sys.argv[-2]

	print(input_file,output_file)

	return input_file,output_file