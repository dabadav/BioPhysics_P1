from Bio.PDB import *
import os

def retpdb(args):
    if not os.path.isfile(f'{args.pdb_file}.pdb'):
        PDBList().retrieve_pdb_file(args.pdb_file, pdir='.', file_format="pdb", overwrite=True)
        os.rename(f'pdb{args.pdb_file}.ent', f'{args.pdb_file}.pdb')
