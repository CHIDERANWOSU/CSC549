from scipy import stats
import sys, string, math
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
geneFile = open("Influenza_control_expr.txt", 'r')
conGeneData = geneFile.readlines()
geneFile.close()
geneFile = open("Influenza_inf_expr.txt", 'r')
infGeneData = geneFile.readlines()
geneFile.close()
flag = 0
for i, j in zip(infGeneData, conGeneData):
 infGeneSplit = i.split()
 conGeneSplit = j.split()
 geneName = infGeneSplit[0]
 infVals = infGeneSplit[1:]
 conVals = conGeneSplit[1:]
 if flag != 0:
 infVals = list(map(float, infVals))
 conVals = list(map(float, conVals))
 t_test = stats.ttest_ind(infVals, conVals)
 if t_test[1] < 0.1:
 print("Gene: ")
 print(geneName)
 print("\n")
 print("P-Value: ")
 print(str(t_test[1]))
 print("\n")
 print("T-Statistic: ")
 print(str(t_test[0]))
 print("\n**********\n")
 flag += 1
