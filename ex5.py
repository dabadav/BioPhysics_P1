from Bio.PDB import *
import argparse
from retrievepdb import *
import numpy as np

parser = argparse.ArgumentParser(
                                 prog='Script 5', 
                                 description='Generate a list of backbone connectivity (i.e. which residues are linked by ordinary peptide bonds)'
                                 )

# Format for a optional text argument, default values can be indicated.

parser.add_argument(
                    '--cut-off', 
                    default=2.5,
                    type=float,
                    dest='d',
                    help='Optional: Cut-off distance for peptide bonds (defaults to 2.5)'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()
parser = PDBParser()

# Download the pdb file
retpdb(args)

pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')
select = []

#Select only CA atoms

for at in st.get_atoms():
    if at.id == 'C' or at.id == 'N':
        select.append(at)

# Preparing search
nbsearch = NeighborSearch(select)

print("Feasible Peptide bonds:")

#Searching for contacts under HBLNK

ncontact = 1

for at1, at2 in nbsearch.search_all(20):
    if at1-at2 < args.d:
        print("Contact: ", ncontact)
        print("ATOM 1:", at1, at1.get_serial_number(), at1.get_parent().get_resname(), at.get_parent().id[1])
        print("ATOM 2:", at2, at2.get_serial_number(), at2.get_parent().get_resname(), at.get_parent().id[1])
        print(f"Distance: {at1-at2}\n")
    ncontact += 1