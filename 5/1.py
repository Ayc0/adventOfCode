file = open("./io.txt", "r")
io = [int(line.strip()) for line in file.readlines()]
file.close()

pointer = 0
loop = True
i = 1

while loop:
  nextPointer = pointer + io[pointer]
  if (nextPointer >= len(io)):
    loop = False
    print(i)
  else:
    io[pointer] += 1
    i += 1
    pointer = nextPointer
