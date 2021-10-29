from Bio.PDB import *
import argparse
from retrievepdb import *

parser = argparse.ArgumentParser(
                                 prog='Script 2', 
                                 description='Generate a list of all atoms for a given residue number'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument('residue_num',
                    type=int,
                    help='Residue number (Including Chain if applicable)'
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


aa = []
res_list = st.get_residues()

for res in res_list:
    if args.residue_num in res.id:
        aa.append(res.get_resname())

selec = []
for at in st.get_atoms():
    if at.get_parent().get_resname() in aa:
        selec.append(at)

print("Atom, coordinates | Resname resid:")
for atom in selec:
    print(f'Atom: {atom.get_name()}, coordinates {atom.get_coord()} | {atom.get_parent().get_resname()} {atom.get_parent().id[1]}')
