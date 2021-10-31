echo '________________________________________________________________________________-'
echo
echo 'Script 1: Determine the list of pairs of residues whose CA atoms are closer than a given distance'
echo 'for parameters: pdb_file=1ubq, distance = 4'
echo '________________________________________________________________________________-'
echo
python ex1.py 1ubq 4;
wait
read -n 1 -s -r -p "Press any key to continue"

echo '________________________________________________________________________________-'
echo
echo 'Script 2: Generate a list of all atoms for a given residue number'
echo 'for parameters: pdb_file = 1ubq, residue num = 10'
echo '________________________________________________________________________________-'
echo
python ex2.py 4kk9 10;
wait
read -n 1 -s -r -p "Press any key to continue"

echo '________________________________________________________________________________-'
echo
echo 'Script 3: Determine all possible hydrogen bonds (Polar atoms at less than 3.5 Å)'
echo 'for parameters: pdb_file = 1ubq, -c (cut-off distance) = 3.5'
echo '________________________________________________________________________________-'
echo
python ex3.py 1ubq;
wait
read -n 1 -s -r -p "Press any key to continue"

echo '________________________________________________________________________________-'
echo
echo 'Script 4: Generate a list of all CA atoms of given residue type with coordinates'
echo 'for parameters: pdb_file = 1ubq, rtype (residue name)= ARG'
echo '________________________________________________________________________________-'
echo
python ex4.py 1ubq ARG;
wait
read -n 1 -s -r -p "Press any key to continue"


echo '________________________________________________________________________________-'
echo
echo 'Script 5: Generate a list of backbone connectivity (i.e. which residues are linked by ordinary peptide bonds)'
echo 'for parameters: pdb_file = 1ubq, cut-off distance for peptide bonds = 2.5'
echo '________________________________________________________________________________-'
echo
python ex5.py 1ubq;
wait
read -n 1 -s -r -p "Press any key to continue"

echo '________________________________________________________________________________-'
echo
echo 'Script 6: Generate a list of all disulphide bonds of given residue type with coordinates'
echo 'for parameters: pdb_file = 1ubq, cut-off distance for peptide bonds = 2.5'
echo '________________________________________________________________________________-'
echo
python ex6.py 2hls;
wait
read -n 1 -s -r -p "Press any key to continue"

echo '________________________________________________________________________________-'
echo
echo 'Script 7: Generate a list with the distances between all atoms pairs of two given resides'
echo 'for parameters: pdb_file = 1ubq, num_residue1 = 10, num_residue2 = 20'
echo '________________________________________________________________________________-'
echo
python ex7.py 1ubq 10 20;
wait
read -n 1 -s -r -p "Press any key to continue"
