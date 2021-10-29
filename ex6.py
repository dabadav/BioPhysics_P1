from Bio.PDB import *
import argparse
import numpy as np

parser = argparse.ArgumentParser(
                                 prog='Script 4', 
                                 description='Generate a list of all CA atoms of given residue type with coordinates'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument('-rname', 
                    nargs= '?',
                    dest='name',
                    help='Residue type: name'
                    )
parser.add_argument('-rid0', 
                    nargs= '?',
                    default= ' ',
                    help='Residue type id: hetero-flag'
                    )
parser.add_argument('-rid1', 
                    nargs= '?',
                    help='Residue type id: sequence identifier'
                    )
parser.add_argument('-rid2', 
                    default= ' ',
                    nargs= '?',
                    help='Residue type id: insertion code'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()

pdbparser = PDBParser()

st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')
res_list = st.get_residues()

sel = []
for r in res_list:
    ## Residue type set to number**
    try:
        #if args.residue_type == r.id[1]:
        atom = st[0]["A"][r.id[1]]["CA"]
        print(f'Atom: {atom.get_name()}, with coordinates {atom.get_coord()},\nof residue type: name {atom.get_parent().get_resname()}; id {r.id}')
    except KeyError:
        continue