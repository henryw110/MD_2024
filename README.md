# MD_2024



Molecular Dynamics project+notes. "Docs" folder has most material in the bibliography.  

<video src="https://github.com/user-attachments/assets/5ec062ac-e287-4eeb-9180-8adccf1bca81" width="480" height="480" > </ video >  

Requires Python3, Pip, AmberTools and LAMMPS installed on your machine for all conversions and simulation. Only tested on Mac. ffmpeg and pymol suggested.


- [Instructions for AmberTools23 install](https://ambermd.org/GetAmber.php)
- [Instructions for installing LAMMPS with Homebrew ](https://formulae.brew.sh/formula/lammps)


## Solvation and conversion of .pdb file to LAMMPS data format for use in simulations.
- Place pdb for conversion in /data folder. "Barr2_MOR_noTRV.pdb" is included in the repo.
- At the highest level of the repo, /MD_2024, run ```python3 -m .venv . --prompt MD_2024```
- ```source .venv/bin/activate```
- ```pip install -r requirements.txt```
- ```cd src/converter```
- ``` bash ./tleap.sh [TARGET PDB FILE NAME]``` -filename is technically optional, the script will default to "Barr2_MOR_noTRV.pdb"
- A script should run and output appropriately named .prmtop .inpcrd files along with a new pdb in /data which is named "-solvated". Open this pdb with pymol to visually confirm that the box has been solvated.
- The files with names ending in "solvated-data.in" in /data are the extracted atom positions, atom types, and associated angle, dihedral, etc. parameters extracted from the .prmtop file using Python library parmed and rewritten as LAMMPS commands
- ```cd lammps```
- ```lmp-serial -in in.lammps``` Runs a simulation. For visual confirmation look at the images dumped in lammps/img. At the end of the sim run ffmpeg will try to assemble a video out of the images. A .log file with some thermodynamic data will also be written automatically.



TODO: Description of complete procedure for converting parameters from .prmtop files into LAMMPS data using the canonical Amber potential energy formulas.

TODO: Trajectories and other simulation output for analysis

TODO: Ligand parameterization w/ Antechamber

TODO: Neutralization of charges in solvate box with NaCl ions. 


Bibliography:
1. A. Mafi et al., "Mechanism of β-arrestin recruitment by the μ-opioid G protein-coupled receptor" (2020)

   - TRV-130 paper, source for base PDB file. 

2. D.A Case et al., "Amber 2023" (2023)

   - Amber 2023 manual. Generally informative for use of Amber force fields and AmberTools programs.

3. J.W. Ponder, D.A Case., "Force Fields for Protein Simulations" (2003)

   - Fairly short description of the history of protein force fields up to 2003.

4. J.R Gissinger et al., "Type Label Framework for Bonded Force Fields in LAMMPS" (2024)

   - Has a section giving a short primer on how force field parameters describe intramolecular interactions. Suggested by LAMMPS documentation as an introduction.

5. S. Plimpton., "Fast Parallel Algorithms for Short-Range Molecular Dynamics" (1995)

   - Original LAMMPS publication. See also [LAMMPS documentation](https://docs.lammps.org/Intro.html)

6. W.D Cornell et al., "A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules" (1995)

   - Clear description of the functional form which Amber force fields use for dihedral potential energy.
