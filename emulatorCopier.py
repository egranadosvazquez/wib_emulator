import argparse
import sys

parser = argparse.ArgumentParser( description = 'Script used to create multiple emulators with different host' )
parser.add_argument('--infile', type = str, required = True, help = 'input emulator file')
parser.add_argument('--n', type = int, required = True, help = 'Number of copies')
parser.add_argument('--host_start', type = int, required = True, help = 'first host number')

args = parser.parse_args()

infile = args.infile
n      = args.n
start  = args.host_start

for i in range(start, start+n):
    with open(infile, 'r') as or_emul, open(f"wib_emulator_v2_host_{i}.py", 'w') as emul_copy:
      for line in or_emul:
        newline = line.replace("5555", f"{i}")
        emul_copy.write(newline)




