from Bio.PDB import PDBParser
import argparse

parser = argparse.ArgumentParser(
                                 prog='Script 1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    '-d', 
                    type=int,
                    dest='distance',
                    help='Maximum distance between CA atoms of residues pairs'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()
       
# read structure from file
pdbparser = PDBParser()
structure = pdbparser.get_structure(args.pdb_file.strip(".pdb"), args.pdb_file)

model = structure[0]
chain = model['A']

# this example uses only the first residue of a single chain.
# it is easy to extend this to multiple chains and residues.
for residue1 in chain:
    for residue2 in chain:
        if residue1 != residue2:
            # compute distance between CA atoms
            try:
                distance = residue1['CA'] - residue2['CA']
            except KeyError:
                ## no CA atom, e.g. for H_NAG
                continue
            if distance < args.distance:
                print(residue1, residue2, distance)
        # stop after first residue
        break