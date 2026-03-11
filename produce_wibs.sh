
infile=$1
n=$2
host_start=$3
python emulatorCopier.py --infile=$infile --n=$n --host_start=$host_start
python configfilemaker.py --n=$n --host_start=$host_start

mv config.xml /home/nfs/dunedcs/wib_opcua_feb18_2026/wib_opcua/build/bin

