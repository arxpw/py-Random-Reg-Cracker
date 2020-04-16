reg2 = ["X","K","Y"]

pos1 = ["R","B","P","C"]
pos2 = ["T","B","P"]
pos3 = ["V","Y","X","N","K"]
reg = "AK14"

filestring = ""

for one in pos1:
  for two in pos2:
    for three in pos3:
      for reg2thing in reg2:
        format = "A" + reg2thing + "14" + one + two + three + "\n"
        filestring = filestring + format

f = open("regs.txt", "a")
f.write(filestring)
f.close()
