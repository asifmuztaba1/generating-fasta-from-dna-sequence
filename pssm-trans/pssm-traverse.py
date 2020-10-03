with open("10.fasta.pssm", "r") as f:
    lines = f.readlines()
with open("temp.fasta", "w+") as f:
    for line in lines[3:]:
        if(line[10]==' ' and line[11]==' ' and line[12]==' '):
            break
        f.write(line[10:90]+'\n')