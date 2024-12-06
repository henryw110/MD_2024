# Notes on Antechamber, ACPYPE, and ligand parameterization

- B-arr paper parameterized ligand with web server ACPYPE "Antechamber Pipe"
- [ACPYPE](https://www.bio2byte.be/acpype/)
- [SOUSA DA SILVA, A. W. & VRANKEN, W. F. ACPYPE - AnteChamber PYthon Parser interfacE. BMC Research Notes 2012, 5:367](https://doi.org/10.1186/1756-0500-5-367)
- [KAGAMI, L. P., SOUSA DA SILVA, A. W., DÍAZ, A., & VRANKEN, W. F., The ACPYPE web server for small-molecule MD topology generation, Bioinformatics, Volume 39, Issue 6, June 2023, btad350](https://doi.org/10.1093/bioinformatics/btad350)
- ACPYPE has a public archive of parameterized ligands w/ topology and structure files we can translate into LAMMPS input
- "acpype_oliceridine" folder contains files for TRV-130, the molecule of interest
- Supplied structure from B-arr paper github has atoms which need to be manually renamed according to the names in oliceridine_AC.lib
- ACPYPE can take input from .pdb, .mol2, or SMILES string and output appropriate parameters.