from Bio.PDB import *
import argparse
from retrievepdb import *

parser = argparse.ArgumentParser(
                                 prog='Script 3', 
                                 description='Determine all possible hydrogen bonds (Polar atoms at less than 3.5 Å)'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    '-c',
                    default=3.5,
                    type=float,
                    dest='d',
                    help='cut-off distance (defaults to 3.5)'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()

# Download the pdb file
retpdb(args)

pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')
select = []

#Select only CA atoms

for at in st.get_atoms():
    if at.id == 'N':
        select.append(at)

# Preparing search
nbsearch = NeighborSearch(select)

print("NBSEARCH:")

#Searching for contacts under HBLNK

ncontact = 1

for at1, at2 in nbsearch.search_all(20):
    if at1-at2 < args.d:
        print("Contact: ", ncontact)
        print("ATOM 1:", at1, at1.get_serial_number(), at1.get_parent().get_resname(), at.get_parent().id[1])
        print("ATOM 2:", at2, at2.get_serial_number(), at2.get_parent().get_resname(), at.get_parent().id[1])
        print(f"Distance: {at1-at2}\n")
    ncontact += 1