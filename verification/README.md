# Verification of converter script

- Added a collection of tripeptide .xyz files from PEPCONF dataset in /tripeptide. Each file is a tripeptide in several conformations with ACE and NHE groups on the ends. Will convert the .xyz files to .pdb, get parameters from AmberTools, calculate energy with AmberTools, then convert and load them into LAMMPS to test energy there. If energies are close conversion is fairly succesful.
- "energy.csv" contains the predicted energy from cpptraj(amber total energy) and total energy from lammps (lammps total energy) for 6 conformations of 288 tripeptides. PDB files for each conformation are available in the /pdb folder.


Bibliography  
1. ["PEPCONF, a diverse data set of peptide conformational energies"](https://www.nature.com/articles/sdata2018310)

Appears to be strong agreement between energy from LAMMPS thermo and Ambertools cpptraj for a converted tripeptide (Total -149.4593 in cpptraj, -149.350 in LAMMPS). 
TODO:Apply to rest of PEPCONF 
![Screenshot_2024-11-26_at_12 41 38_PM](https://github.com/user-attachments/assets/a1ab610b-dbf0-4f96-a5d8-d33db27df418)

