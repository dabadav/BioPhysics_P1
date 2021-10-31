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
                                 prog='Script 1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Format for a optional text argument, default values can be indicated.
parser.add_argument('distance',
                    type = int,
                    help='Maximum distance between CA atoms of residues pairs'
                    )


# Read command line into args
args = parser.parse_args()


# Retrieve pdb file
# Download the pdb file
retpdb(args)

# read structure from file
pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')

# Get all residues from a structure
select = []

#Select only CA atoms

for at in st.get_atoms():
    if at.id == 'CA':
        select.append(at)

# Preparing search
nbsearch = NeighborSearch(select)

#Searching for contacts under HBLNK

for at1, at2 in nbsearch.search_all(args.distance):
        print(atom_id(at1))
        print(atom_id(at2))
        print(f"Distance: {at1-at2}\n")

