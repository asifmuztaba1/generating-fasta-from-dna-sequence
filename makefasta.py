import os
os.mkdir('fastafiles-train')
with open("test.txt", "r") as f:
    lines = f.readlines()
    del lines[3-1::3]
i=1
for line, nextline in zip(lines[::2] ,lines[1::2]):
#if line.strip("\n") != "0":
#if line.isdigit():
    with open('train-fasta/'+str(i)+".fasta", "w+") as f:
        li=line+nextline
        f.write(li)
        i += 1
        print(line,nextline)

