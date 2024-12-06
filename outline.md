# Outline for future of project Dec 5 2024

- What can we do?
   - Run a fully parameterized and solvated simulation of the protein-ligand complex described in the barr-2 paper with LAMMPS
   - Verify that the total energy of Amber parameter and coordinate files converted into LAMMPS input are very close to the total energy before conversion. This is good, it means the "Translation" of Amber parameters into LAMMPS commands was fairly accurate
   - Run simulations of the protein-ligand complex several hundred picoseconds long on Macbook, write thermodynamic data to files for analysis, dump images of the simulation to be used for a visualization
- Which limitations?
   - Compute time. 4-6 hours of simulation time on laptop produces less than one nanosecond, replicating calculations from section "Umbrella sampling MD for finding the activation pathway of barr2." in the Mafi supplementary information will require more than 200ns of simulation.
   - Because of differences between LAMMPS and Amber/Gromacs, the long-range particle mesh interadtions will be slightly different. Constraint algorithm for H-bonds is also slightly different. 
- Further steps
   - Calculations can be accelerated using computers more powerful than a single laptop.
   - Perform very short simulations, 2ns rather than 200ns as preliminary data gathering