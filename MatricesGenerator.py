#!/usr/bin/python
# -*- coding: UTF-8 -*-
def main():
	protein_file = open("File S1 Coronaviridae_HDGs.txt","r") #or other protein info file.
	protein_AA = []
	protein_info = {}
	for x in protein_file:
		l = x.strip().split("\t")
		protein_AA.append(l[1])
		protein_info[l[1]] = l[0]
	protein_file.close
	drug_file = open("File S3 Drugbank_Approved.txt","r")  #or other drug info file (e.g, "Table S4 TCM_selected.txt").
	drug_inchi = []
	drug_info = {}
	for x in drug_file:
		l = x.strip().split("\t")
		drug_inchi.append(l[1])
		drug_info[l[1]] = l[0]
	drug_file.close

	PredictedScore = open("Prediction_results.tsv","r")  #or other DTI score result file (Format：DrugInChI	ProteinAA	PredictedScore).
	output = open("Prediction_results.matrix.txt","w")
	i = 1
	createVar = locals()
	for i in range(0,len(protein_AA)):
		createVar[str(protein_AA[i])]={}
	for x in PredictedScore:
		l = x.strip().split("\t")
		createVar[str(l[1])][str(l[0])] = l[2]
		i += 1
	PredictedScore.close
	n = 0
	for i in protein_AA:
		output.write("\t"+protein_info[i])
	output.write("\n")
	for i in drug_inchi:
		if n == 0:
			output.write(drug_info[i]+"\t")
			for ii in range(0,len(protein_AA)):
				y = "0"
				if i in createVar[protein_AA[ii]]:
					y = createVar[protein_AA[ii]][i]
				output.write(y+"\t")
		if n > 0:
			if i == x:
				for ii in range(0,len(protein_AA)):
					y = "0"
					if i in createVar[protein_AA[ii]]:
						y = createVar[protein_AA[ii]][i]
					output.write(y+"\t")
			if i != x:
				output.write(str(i)+"\t")
				for ii in range(0,len(protein_AA)):
					y = "0"
					if i in createVar[protein_AA[ii]]:
						y = createVar[protein_AA[ii]][i]
					output.write(y+"\t")
		x = i
		output.write("\n")
	output.close
if __name__=='__main__':
	main()


	

