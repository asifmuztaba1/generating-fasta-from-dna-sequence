with open("Test.pdb", "r") as f:
    lines = f.readlines()
    del lines[3-1::3]
    print(lines)
with open("t.pdb", "w") as f:
    for line in lines:
        #if line.strip("\n") != "0":
        #if line.isdigit():
        f.write(line)
        print(line)