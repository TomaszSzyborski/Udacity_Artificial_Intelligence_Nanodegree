import sys 
file_name = sys.argv[1]

with open(file_name, 'r') as f:
	lines = f.read()

linez = []
lines = lines.replace("\\n", "\n")
lines = lines.splitlines("--------------------")
for line in lines:
	In = line.startswith("In",0,2)
	At = line.startswith("At",0,2)
	Load = line.startswith("Load",0,4)
	Unload = line.startswith("Unload",0,6)
	Fly = line.startswith("Fly",0,3)
	if not (In or At or Load or Unload or Fly):
		linez.append(line)

with open("cleaned.txt", 'w') as f:
	f.writelines(linez)

