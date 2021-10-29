import argparse
import sys

parser = argparse.ArgumentParser(
                                 prog='s1', 
                                 description='Determine the list of pairs of residues whose CA atoms are closer than a given distance'
                                 )

# Use add_argument for all needed arguments
# https://docs.python.org/3/library/argparse.html

# Format for a optional text argument, default values can be indicated.
parser.add_argument(
                    '-d',
                    dest='distance',
                    help='Maximum distance between CA atoms of residues pairs'
                    )

# Format for a required parameter, call will fail if empty. This only stores the file name, but specifiying type=file, the file is open and contents available. 
parser.add_argument('pdb_file',
                    help='Required file (.pdb)')

# Read command line into args

args = parser.parse_args()
       
# Print the parameters that has been read 
    
print ("\nSettings\n--------")

for k, v in vars(args).items():
    print ('{:10}:'.format(k), v)

print ("\nSettings, again\n---------------")    

#print the variables once assigned
Variable2 = args.distance
Variable_Required = args.pdb_file

print(Variable2, Variable_Required)  
