"""
ID: pradyun1
LANG: PYTHON3
TASK: namenum
"""

fin = open("namenum.in", "r")#Initialize input and output of files
fout = open("namenum.out", "a")
din = open("dict.txt", "r")

import itertools#importing module to derive all possible combinations of set of strings


convertdic={"2":["A","B","C"],
            "3":["D","E","F"],
            "4":["G","H","I"],
            "5":["J","K","L"],
            "6":["M","N","O"],
            "7":["P","R","S"],
            "8":["T","U","V"],
            "9":["W","X","Y"]}#Conversion key

rawnum = fin.readline().strip()#Take number and setup for conversion into list type, char by char
number = []

for i in rawnum:#Conversion from string into list of single digit strings
    number.append(i)


convnum = []#Converted number list

for i in number:#Adding full converted number to string possibilities into new set
    convnum.append(convertdic[i])

rawposscomb = list(itertools.product(*convnum))#Using itertools to derive all possible combinations in my list of lists

posscomb=[]

for i in rawposscomb:#Condense lists of string combinations into single strings
    posscomb.append("".join(i))

finnames = []#List of final names

for i in din:#Actually checking for final names in names dictionary
    if i.strip() in posscomb:
        finnames.append(i.strip())

if finnames == []:#Writing actual output to file
    fout.write("NONE")

else:
    for i in finnames:
        fout.write(i+'\n')

fin.close()#Closing file connections
fout.close()