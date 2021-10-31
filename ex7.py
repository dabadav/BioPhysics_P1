from Bio.PDB import *
import argparse
import numpy as np
import retrievepdb

def residue_id(res):
    """Nice representation of a residue"""
    return res.get_resname() + " " + res.get_parent().id + str(res.id[1])
    # return "{} {} {}".format()

def atom_id(at):
    """Nice representation of an atom"""
    return residue_id(at.get_parent()) + "." + at.id

parser = argparse.ArgumentParser(
                                 prog='Script 7', 
                                 description='Print distances between all atoms pairs of two given resides'
                                 )


# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    'r1', 
                    type=int,
                    help='Residue 1 number'
                    )

parser.add_argument(
                    'r2', 
                    type=int,
                    help='Residue 2 number'
                    )

# Read command line into args
args = parser.parse_args()

retrievepdb.retpdb(args)

pdbparser = PDBParser()

st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')
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
        print(f"{atom_id(at10)}, {atom_id(at20)}, Distance: {distance}")


