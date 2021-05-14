#!/usr/bin/python
# -*- coding: UTF-8 -*-
def main():
	d = open("File S3 Drugbank_Approved.txt","r")   #or other drug info file (e.g, "File S4 TCM_selected.txt").
	p = open("File S1 Coronaviridae_HDGs.txt","r")  #or other protein info file.
	output = open("Drug_Target_Pair.txt","w")
	i = 0
	inchi = {}
	for x in d:
		if i > -1:
			l = x.strip().split("\t")
			inchi[i] = l[1]
		i += 1
	i = 0
	for x in p:
		l = x.strip().split("\t")
		for k in inchi.keys():
			output.write(inchi[k]+"\t"+l[1]+"\n")
	d.close
	p.close
	output.close
if __name__=='__main__':
    main()



	

