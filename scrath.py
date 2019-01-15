fout = open("namenumdict.txt","a")

for i in range(2,5):
    fout.write(str(i)+'\n')

fout.close()