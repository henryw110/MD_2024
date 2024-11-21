#!/bin/bash
fname='Barr2_MOR_noTRV'
if [ $1 ]; then
  fname=${{$1}%.pdb}
fi

STR="mol=loadPdb ../../data/Barr2_MOR_noTRV.pdb; solvateBox mol TIP3PBOX {10 20 10}; savePDB mol ../../data/$fname-solvated.pdb; saveAmberParm mol $fname-solvated.prmtop $fname-solvated.inpcrd; quit";
echo -e $STR | tleap -I . -f - 

python converter.py $fname-solvated.prmtop $fname-solvated.inpcrd ../../data/$fname-solvated-data.in
