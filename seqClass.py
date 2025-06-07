#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

# Changed: Moved motif argument definition _before_ parsing args
parser = ArgumentParser(
    description='Classify a sequence as DNA, RNA, ambiguous (DNA or RNA), or neither; calculate nucleotide percentages; optionally search for a motif'
)
parser.add_argument('-s', '--seq',
                    type=str,
                    required=True,
                    help='Input sequence')
parser.add_argument('-m', '--motif',
                    type=str,
                    help='Motif to search for')  # Changed: Defined motif arg before parse_args()


if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)


args = parser.parse_args()
seq = args.seq.upper()  # Changed: Normalize sequence once into a local variable

# Classification logic 
if not re.fullmatch(r'[ACGTU]+', seq):
    print('The sequence is not DNA nor RNA')
else:
    has_t = 'T' in seq  # Changed: Count presence of T and U
    has_u = 'U' in seq

    if has_t and has_u:
        print('The sequence is not DNA nor RNA') 
    elif has_t:
        print('The sequence is DNA')               
    elif has_u:
        print('The sequence is RNA')               
    else:
        print('The sequence can be DNA or RNA')    

# Motif search 
if args.motif:
    motif = args.motif.upper()  # Changed: Normalize motif separately
    print(f'Motif search enabled: looking for motif "{motif}" in sequence "{seq}"... ', end='')
    if re.search(motif, seq):
        print('FOUND')
    else:
        print('NOT FOUND')

# Changed: Calculate nucleotide percentages
print('\nNucleotide composition:')
total_len = len(seq)
for nt in sorted(set(seq)):
    if nt in 'ACGTU':
        count = seq.count(nt)
        pct = count / total_len * 100
        print(f'  {nt}: {pct:.2f}% ({count}/{total_len})')
