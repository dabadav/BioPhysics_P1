from re import A
from Bio.PDB import *
import argparse
from retrievepdb import *
import numpy as np
from Bio.PDB.PDBParser import PDBParser

def residue_id(res):
    """Nice representation of a residue"""
    return res.get_resname() + " " + res.get_parent().id + str(res.id[1])
    # return "{} {} {}".format()

def atom_id(at):
    """Nice representation of an atom"""
    return residue_id(at.get_parent()) + "." + at.id

parser = argparse.ArgumentParser(
                                 prog='Script 6', 
                                 description='Generate a list of all disulphide bonds of given residue type with coordinates'
                                 )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

parser.add_argument('-d', 
                    type = float,
                    dest = 'distance',
                    default = 2.2,
                    help='Residue type: name'
                    )


# Read command line into args
args = parser.parse_args()

retpdb(args)
st = PDBParser(QUIET=True).get_structure('tmp', f'{args.pdb_file}.pdb')

for at1 in st.get_atoms():
    if (at1.get_parent().get_resname() != 'CYS'):
        continue
    if at1.id[0] != "S":
        continue
    for at2 in st.get_atoms():
        if (at2.get_parent().get_resname() != 'CYS'):
            continue
        if at2.id[0] != "S":
            continue
        if at1 == at2:
            continue
        if at1.serial_number > at2.serial_number:
            continue
        if at1 - at2 < args.distance:
            print("Feasible disulphide bond:")
            print(atom_id(at1))
            print(atom_id(at2))
            print(f"Distance: {at1-at2}\n")
