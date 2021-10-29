from Bio.PDB import *
import argparse

parser = argparse.ArgumentParser(
                                 prog='Script 3', 
                                 description='Determine all possible hydrogen bonds (Polar atoms at less than 3.5 Å)'
                                 )

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    '--cut-off', 
                    const=3.5,
                    type=float,
                    dest='d',
                    help='cut-off distance (defaults to 3.5)'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required .pdb file for the program')

# Read command line into args
args = parser.parse_args()
parser = PDBParser()