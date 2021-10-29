from Bio.PDB import *
import argparse
import numpy as np

parser = argparse.ArgumentParser(
                                 prog='Script 7', 
                                 description='Print distances between all atoms pairs of two given resides'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    '-r1', 
                    type=int,
                    dest='r1',
                    help='Residue 1 number'
                    )

parser.add_argument(
                    '-r2', 
                    type=int,
                    dest='r2',
                    help='Residue 2 number'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()
parser = PDBParser()

st = parser.get_structure('', args.pdb_file)
for model in st:
    for chain in model:
        print(chain)

#Selection of Residue 10 of Chain A
res10 = st[0]["A"][args.r1]
#Selection of Residue 20 of Chain A
res20 = st[0]["A"][args.r2]

print("Residue 10 is", res10.get_resname())
print("Residue 20 is", res20.get_resname())

print("\nAtom1 Atom2 dist1 dist2\n---------------------------")
for at10 in res10.get_atoms():      # Replace get_atoms with get_atom if you get an Error!
    for at20 in res20.get_atoms():
        dist = at20 - at10     # Direct procedure with (-) to compute distances
        vector = at20.coord - at10.coord  # Or using numpy coordinates
        distance = np.sqrt(np.sum(vector ** 2))
        print(at10, at20, dist, distance)

center = np.array([10, 10, 10])
print("\nDistance of res10 to {} \n".format(center))
for at10 in res10.get_atoms():
    vect = at10.coord - center
    distance = np.sqrt(np.sum(vect ** 2))
    print(at10, distance)

