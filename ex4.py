from Bio.PDB import *
import argparse
from retrievepdb import *
import numpy as np

parser = argparse.ArgumentParser(
                                 prog='Script 4', 
                                 description='Generate a list of all CA atoms of given residue type with coordinates'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument('-rname',
                    dest='rname',
                    help='Residue type: name'
                    )
parser.add_argument('-rid0', 
                    dest='rid0',
                    help='Residue type id: hetero-flag'
                    )
parser.add_argument('-rid1', 
                    dest='rid1',
                    help='Residue type id: sequence identifier'
                    )
parser.add_argument('-rid2', 
                    dest ='rid2',
                    help='Residue type id: insertion code'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()
retpdb(args)

pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')

res_list = st.get_residues()

sel = []
for r in res_list:
    if args.rname:
        if args.rname in r.id:
            sel.append(r)
    if args.rid0:
        if args.rid0 in r.id:
            sel.append(r)
    if args.rid1:
        if args.rid1 in r.id:
            sel.append(r)
    if args.rid2:
        if args.rid2 in r.id:
            sel.append(r)

if not sel:
    sel = res_list

for s in sel:
    ## Residue type set to number**
    try:
        #if args.residue_type == r.id[1]:
        atom = st[0]["A"][s.id[1]]["CA"]
        print(f'Atom: {atom.get_name()}, with coordinates {atom.get_coord()},\nof residue type: name {atom.get_parent().get_resname()}; id {r.id}')
    except KeyError:
        continue