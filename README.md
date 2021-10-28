# BioPhysics_P1

1. Determine the list of pairs of residues whose CA atoms are closer than a given distance

Parameters: PDB file name, distance.

2. Generate a list of all atoms for a given residue number

Parameters: PDB file name, Residue number (Including Chain if applicable)

3. Determine all possible hydrogen bonds (Polar atoms at less than 3.5 Å).

Parameters: PDB file name. Optional: cut-off distance (defaults to 3.5)

4. Generate a list of all CA atoms of given residue type with coordinates

Parameters: PDB file name, residue type.

Optional: accept residue codes in one- or three-letter formats automatically

5. Generate a list of backbone connectivity (i.e. which residues are linked by ordinary peptide bonds).

Parameters: PDB file name. Optional: Cut-off distance for peptide bonds (defaults to 2.5)

6. Id 4, but for disulphide bonds.

7. Print distances between all atom pairs of two given residues

Parameters: PDB file name, Residue 1, Residue 2
