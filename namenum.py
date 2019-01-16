"""
ID: pradyun1
LANG: PYTHON3
TASK: namenum
"""

fin = open("namenum.in", "r")#Initialize input and output of files
fout = open("namenum.out", "a")

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
finnames = []

for i in number:
    convnum.append(convertdic[i])

for i in list(itertools.product(*convnum)):#Using itertools to derive all possible combinations in my list of lists
    temp = "".join(i)+'\n'#Concatenating the list of strings into one string w newline character
    din = open('dict.txt','r')#Opening dict, checking for all possible matches
    if temp in din:
        finnames.append(temp)
    din.close()



if finnames == []:
    fout.write("NONE\n")

else:
    for i in finnames:
        fout.write(i)

fin.close()#Closing file connections
fout.close()