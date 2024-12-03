#!/bin/bash
# if [ $1 ]; then
#   fname=${{$1}%.pdb}
#fi
echo "conformation, sequence, amber total energy, lammps total energy" > energy.csv
F=$(ls -1 ./tripeptide/xyz)
echo "${F}"|while read p; do
  if [ $? -ne 0 ]; then
  exit 1
  fi
  fname=${p:0:13}
  echo "conv ${fname}"
  python verification.py $p
done
echo "${F}"|while read p ; do
  fname=$(echo "${p:0:13}.pdb")
  r=$(echo "${p:0:11}")
  if [ $fname ]; then
  STR="mol=loadPdb ./pdb/${fname}; setBox mol \"vdw\";savePdb mol out.pdb; saveAmberParm mol out.prmtop out.inpcrd; quit"
  echo -e $STR | tleap -I . -f - > /dev/null
  if [ $? -ne 0 ]; then
  exit 1
  fi
  python ../src/converter/converter.py out.prmtop out.inpcrd out.in > /dev/null
  STR="parm out.prmtop\n
trajin out.inpcrd\n
box auto \n
box x 30 y 30 z 30\n
energy out ene.dat en bond angle dihedral nb14 nonbond etype pme cut 12 ljswidth 2 nfft 25,25,25  \n
datafile ene.dat invert noxcol\n
run\n
printdata pep[*]\n
printdata en[*]" &&\
  echo -e $STR  | cpptraj > /dev/null &&\
  cat ene.dat | while read q; do
    cppt=${q#"en[total]"}
    if [ "$cppt" != "$q" ]; then
      cppt=$( echo "$cppt" | xargs )
      lmp_serial -in energy.lammps > /dev/null
      val=$(python parseYaml.py)
      echo "$fname,$r,$cppt,$val" >> energy.csv
      echo "$fname,$r,$cppt,$val"
    fi
    done
  fi
done
rm dump.yaml
rm ene.dat
rm leap.log
rm out.inpcrd
rm out.prmtop
rm out.pdb
rm out.in
rm log.lammps



#fname='out' && \
# python verification.py&&\
#STR="mol=loadPdb ${fname}.pdb; setBox mol \"vdw\";savePdb mol $fname.pdb; saveAmberParm mol $fname.prmtop $fname.inpcrd; quit"&&\
#echo -e $STR | tleap -I . -f - > /dev/null
#python ../src/converter/converter.py $fname.prmtop $fname.inpcrd $fname.in > /dev/null &&\
# STR="parm ${fname}.prmtop\n
# trajin ${fname}.inpcrd\n
# box auto \n
# box x 30 y 30 z 30\n
# energy out ene.dat en bond angle dihedral nb14 nonbond etype pme cut 12 ljswidth 2 nfft 25,25,25  \n
# datafile ene.dat invert noxcol\n
# run\n
# printdata pep[*]\n
# printdata en[*]" &&\
# echo -e $STR  | cpptraj > /dev/null &&\
# # cat ene.dat&&\
# lmp_serial -in in.lammps > /dev/null &&\
# cat ene.dat | while read q; do
#   st=${q#"en[total]"}
#   if [ "$st" != "$q" ]; then
#     echo "$fname $st" >> energy
#   fi
# done

