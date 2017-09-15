import subprocess
from interruptingcow import timeout
from subprocess import Popen, PIPE

#cleaning the file
with open("run_search_analysis_2.txt", "w") as f:
	f.write("")

search = "pypy3 run_search.py --problems {0} --searches {1}"

to_write = []
filters = ["In(", "At(", "Load(", "Unload(", "Fly("]

for p in range(1,4):
	for s in range(1,11):
		print("Running:")
		cmd = search.format(p, s)
		print(cmd)
		to_write.append("Solving problem {} \n".format(p))
		to_write.append("Using Search number {} \n".format(s))
		try:
			with timeout(10*60, exception=RuntimeError):
				
				proc = Popen(cmd.split(" "),
					stdout=PIPE,
					universal_newlines=True)
				while True:
					line = proc.stdout.readline()
					if line != '':
						print("INFO:", line.strip())
						# _In = line.startswith(filters[0], 0, 2)
						# _At = line.startswith(filters[1], 0, 2)
						# _Load = line.startswith(filters[2], 0, 4)
						# _Unload = line.startswith(filters[3], 0, 6)
						# _Fly = line.startswith(filters[4], 0, 3)
						_In = filters[0] in line
						_At = filters[1] in line
						_Load = filters[2] in line
						_Unload = filters[3] in line
						_Fly = filters[4] in line
						
						if not (True in [_In,_At,_Load,_Unload,_Fly]):
							to_write.append(line)
					else:
						break
		except RuntimeError:
			to_write.append("\nWARNING!!!\nSearch took more than 10 minutes\n")
		finally:
			to_write.append("--------------------\n")

with open("run_search_analysis_2.txt", "a") as f:
	f.writelines(to_write)
		
