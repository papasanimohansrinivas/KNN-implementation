from dependencies_installation import dependencies_verification

from parse_cmd import parse_cmd_line

from distance_vector import compare_distances

from map_box import map_box_api

from algo_ import cmp_address


def validatior(output_file,input_file):

	outfile=open(output_file,"w")
	print("qrqwerqewr")

	import csv
	print(input_file,output_file)

	with open(input_file,"r") as doc:

		file=csv.reader(doc)
		wrt=csv.writer(outfile)
		for m in file:
			try:
				test_1,test_2,test_3 = m
				# print(m)
				
				d_1,d_2=map_box_api(m)
				
				result=cmp_address(d_1,d_2)

				# # print result

				wrt.writerow(m+[result])

			except ValueError:
				pass
			except IndexError:
				pass

		outfile.close()

input_file,output_file=parse_cmd_line()
validatior(output_file,input_file)

