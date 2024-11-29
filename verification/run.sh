#!/bin/bash
if [ $1 ]; then
  fname=${{$1}%.pdb}
fi
fname='out' && \
python verification.py&&\
STR="mol=loadPdb ${fname}.pdb; setBox mol \"vdw\";savePdb mol $fname.pdb; saveAmberParm mol $fname.prmtop $fname.inpcrd; quit"&&\
echo -e $STR | tleap -I . -f - > /dev/null &&\
python ../src/converter/converter.py $fname.prmtop $fname.inpcrd $fname.in > /dev/null &&\
STR="parm ${fname}.prmtop\n
trajin ${fname}.inpcrd\n
box auto \n
box x 30 y 30 z 30\n
energy out ene.dat en bond angle dihedral nb14 nonbond etype pme cut 12 ljswidth 2 nfft 25,25,25  \n
run\n
printdata pep[*]\n
printdata en[*]" &&\
echo -e $STR  | cpptraj > /dev/null &&\
echo "cpptraj energy" &&\
cat ene.dat&&\
lmp_serial -in in.lammps > /dev/null &&\
echo "lammps energy" &&\
cat "dump.yaml"

