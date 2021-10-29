from Bio.PDB import *
import argparse

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
parser = PDBParser()

st = parser.get_structure('1UBQ', args.pdb_file)


aa = []
res_list = st.get_residues()

for res in res_list:
    if args.residue_num in res.id:
        aa.append(res.get_resname())

selec = []
for at in st.get_atoms():
    if at.get_parent().get_resname() in aa:
        selec.append(at)

print("Coordinates:")
for atom in selec:
    print(atom.get_parent().get_resname(), atom.get_parent().id,
          atom.get_name(), atom.get_coord())
