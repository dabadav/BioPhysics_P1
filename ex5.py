from Bio.PDB import *
import argparse
import numpy as np

parser = argparse.ArgumentParser(
                                 prog='Script 5', 
                                 description='Generate a list of backbone connectivity (i.e. which residues are linked by ordinary peptide bonds)'
                                 )

# Format for a optional text argument, default values can be indicated.

parser.add_argument(
                    '--cut-off', 
                    const=2.5,
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