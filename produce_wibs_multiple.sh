infile=$1
n=$2
host_start=$3
stops=$host_start+$n
python emulatorCopier.py --infile=$infile --n=$n --host_start=$host_start

factor=48
fac_min_one=$(( $factor - 1 ))
newstart=$host_start
c=1
for ((i=$(($host_start+1)); i<=$stops; i++)); do

  res=$(($i-$host_start))
  wib_start=$(( $res - $fac_min_one ))
#  if [[ "$res" -eq 0 ]]; then
#         continue
#  fi
  modulo=$(($res % $factor))
  if [[ "$modulo" -eq 0 ]];then
#    echo "python configfilemaker_multiple.py --n=$factor --host_start=$newstart --wib_num_start=$wib_start"
#    echo "mv config.xml config${c}.xml"
    python configfilemaker_multiple.py --n=$factor --host_start=$newstart --wib_num_start=$wib_start
    mv config.xml /home/nfs/dunedcs/wib_opcua_feb18_2026/multirun/wibopcua${c}/build/bin
    newstart=$(($i))
    c=$(($c+1))
  fi
  if [[ "$i" -eq "$stops" ]] && [[ "$modulo" -ne 0 ]];then
#          echo "python configfilemaker_multiple.py --n=$modulo --host_start=$newstart --wib_num_start=$(($res - $modulo + 1))"
#          echo "mv config.xml config${c}.xml"
          python configfilemaker_multiple.py --n=$modulo --host_start=$newstart --wib_num_start=$(($res - $modulo + 1))
          mv config.xml /home/nfs/dunedcs/wib_opcua_feb18_2026/multirun/wibopcua${c}/build/bin
  fi
done
#python configfilemaker.py --n=$n --host_start=$host_start

#mv config.xml /home/dunedcs/wib_opcua_cc_threadlimit/multirun/wibopcua2/build/bin
