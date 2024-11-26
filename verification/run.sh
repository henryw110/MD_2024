#!/bin/bash
fname='out'
python verification.py
if [ $1 ]; then
  fname=${{$1}%.pdb}
fi
STR="mol=loadPdb ${fname}.pdb; saveAmberParm mol $fname.prmtop $fname.inpcrd; quit";
echo -e $STR | tleap -I . -f - 

#python converter.py $fname-solvated.prmtop $fname-solvated.inpcrd ../../data/$fname-solvated-data.in
