from Bio.PDB import *
import argparse
from retrievepdb import *
import numpy as np

def residue_id(res):
    """Nice representation of a residue"""
    return res.get_resname() + " " + res.get_parent().id + str(res.id[1])
    # return "{} {} {}".format()

def atom_id(at):
    """Nice representation of an atom"""
    return residue_id(at.get_parent()) + "." + at.id

parser = argparse.ArgumentParser(
                                 prog='Script 5', 
                                 description='Generate a list of backbone connectivity (i.e. which residues are linked by ordinary peptide bonds)'
                                 )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')
                    
# Format for a optional text argument, default values can be indicated.

parser.add_argument(
                    '--cut-off', 
                    default=2.5,
                    type=float,
                    dest='d',
                    help='Optional: Cut-off distance for peptide bonds (defaults to 2.5)'
                    )



# Read command line into args
args = parser.parse_args()
parser = PDBParser()

# Download the pdb file
retpdb(args)

pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')
select = []

#Select only C N atoms

for at in st.get_atoms():
    if at.id == 'C' or at.id == 'N':
        select.append(at)

# Preparing search
nbsearch = NeighborSearch(select)

#Searching for contacts under HBLNK
for at1, at2 in nbsearch.search_all(args.d):
    if at1.get_parent() == at2.get_parent():
        continue
    print("Feasible Peptide bond between:")
    print(atom_id(at1))
    print(atom_id(at2))
    print(f"Distance: {at1-at2}\n")
