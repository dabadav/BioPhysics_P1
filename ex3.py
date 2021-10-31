from Bio.PDB import *
import argparse
from retrievepdb import *


def residue_id(res):
    """Nice representation of a residue"""
    return res.get_resname() + " " + res.get_parent().id + str(res.id[1])
    # return "{} {} {}".format()

def atom_id(at):
    """Nice representation of an atom"""
    return residue_id(at.get_parent()) + "." + at.id
parser = argparse.ArgumentParser(
                                 prog='Script 3', 
                                 description='Determine all possible hydrogen bonds (Polar atoms at less than 3.5 Å)'
                                 )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')
                    
# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    '-c',
                    default=3.5,
                    type=float,
                    dest='d',
                    help='cut-off distance (defaults to 3.5)'
                    )



# Read command line into args
args = parser.parse_args()

# Download the pdb file
retpdb(args)

pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')
select = []

#Select only CA atoms

for at in st.get_atoms():
    if at.id == 'N' or at.id == 'O' or at.id == 'S':
        select.append(at)

# Preparing search
nbsearch = NeighborSearch(select)

print("Feasible Hydrogen bonds:")

#Searching for contacts under HBLNK

for at1, at2 in nbsearch.search_all(args.d):
    print("Feasible Hydrogen bond:")
    print(atom_id(at1))
    print(atom_id(at2))
    print(f"Distance: {at1-at2}\n")