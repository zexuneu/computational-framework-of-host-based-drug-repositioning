#!/usr/bin/python
# -*- coding: UTF-8 -*-
def main():
	input_file = open("Prediction_results.matrix.txt","r") # matrix file name.
	output = open("Prediction_results.matrix.filtered.txt","w") # output file name.
	i = 0
	for x in input_file:
		if i >0:
			l = x.strip().split("\t")
			output.write(l[0])
			for y in range(1,len(l)):
				if float(l[y]) >= 0.892: # edit 0.892 if other cutoff used.
					output.write("\t"+l[y])
				else:
					output.write("\t"+"0")
			output.write("\n")
		if i ==0:
			output.write(x)
		i+=1
	input_file.close
	output.close
if __name__=='__main__':
    main()



	

