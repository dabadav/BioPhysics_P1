#!usr/bin/env python
import Bio
from Bio.PDB import *
from Bio.SeqUtils import *
import argparse
from retrievepdb import *
import numpy as np
from Bio.SeqUtils import seq3

def residue_id(res):
    """Nice representation of a residue"""
    return res.get_resname() + " " + res.get_parent().id + str(res.id[1])
    # return "{} {} {}".format()

def atom_id(at):
    """Nice representation of an atom"""
    return residue_id(at.get_parent()) + "." + at.id

parser = argparse.ArgumentParser(
                                 prog='Script 4', 
                                 description='Generate a list of all CA atoms of given residue type with coordinates'
                                 )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')
                    
# Format for a optional text argument, default values can be indicated.
parser.add_argument('rtype', 
                    help='Residue type: name'
                    )



# Read command line into args
args = parser.parse_args()
retpdb(args)

pdbparser = PDBParser()
st = pdbparser.get_structure(args.pdb_file, f'{args.pdb_file}.pdb')

if len(args.rtype) == 1:
    args.rtype = seq3(args.rtype).upper()

sel = []
res_list = st.get_residues()
for res in res_list:
    if args.rtype == res.get_resname():
        sel.append(res)

print('Atom: id coordinates\n-------------------------')
for s in sel:
    at = s.get_atoms()
    for a in at:
        if a.id == 'CA':
            print(atom_id(a), a.get_coord())

