# MD_2024
Molecular Dynamics project+notes. "Docs" folder has most material in the bibliography.

Requires AmberTools and LAMMPS installed on your machine for conversion and simulation. Only tested on Mac.

[Instructions for AmberTools23 install](https://ambermd.org/GetAmber.php)
[Instructions for installing LAMMPS with Homebrew ](https://formulae.brew.sh/formula/lammps)

TODO: Description of complete procedure for converting .pdb file into LAMMPS input with H20 molecules added

TODO: Code used for conversion

TODO: Trajectories and other simulation output for analysis


Bibliography:
1. A. Mafi et al., "Mechanism of β-arrestin recruitment by the μ-opioid G protein-coupled receptor" (2020)

  TRV-130 paper, source for base PDB file. 

2. D.A Case et al., "Amber 2023" (2023)

  Amber 2023 manual. Generally informative for use of Amber force fields and AmberTools programs.

3. J.W. Ponder, D.A Case., "Force Fields for Protein Simulations" (2003)

  Fairly short description of the history of protein force fields up to 2003.

4. J.R Gissinger et al., "Type Label Framework for Bonded Force Fields in LAMMPS" (2024)

  Has a section giving a short primer on how force field parameters describe intramolecular interactions. Suggested by LAMMPS documentation as an introduction.

5. S. Plimpton., "Fast Parallel Algorithms for Short-Range Molecular Dynamics" (1995)

  Original LAMMPS publication. See also [LAMMPS documentation](https://docs.lammps.org/Intro.html)

6. W.D Cornell et al., "A Second Generation Force Field for the Simulation of Proteins, Nucleic Acids, and Organic Molecules" (1995)

  Clear description of the functional form which Amber force fields use for dihedral potential energy.
