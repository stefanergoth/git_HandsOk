#!/usr/bin/env python

# This code checks if an given seqence could be DNA or RNA 
import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")

if len(sys.argv) == 1:
    parser.print_help() #Prints help message
    sys.exit(1)

args = parser.parse_args()

# IF-Loop to assess if a sequence is DNA/RNA
args.seq = args.seq.upper()                 # Note we just added this line
if re.search('^[ACGTU]+$', args.seq):  #If it only contains ACTGU it is DNA/RNA
    if re.search('T', args.seq): # If it contains T and no Us it is DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq): # If it contains Us it is RNA
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA') 
else:
    print ('The sequence is not DNA nor RNA')

# IF look to look for motifs
if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("FOUND")
    else:
        print("NOT FOUND")

parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

#I added this in the master branch
# I added this in the motif branch
