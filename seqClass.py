#!/usr/bin/env python

import sys
import re
from argparse import ArgumentParser

parser = ArgumentParser(
    description='Classify a sequence as DNA, RNA, ambiguous (DNA or RNA), or neither, and optionally search for a motif'
)
parser.add_argument('-s', '--seq',
                    type=str,
                    required=True,
                    help='Input sequence')
parser.add_argument('-m', '--motif',
                    type=str,
                    help='Motif to search for')

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()
seq = args.seq.upper()

# First check that the sequence contains only the valid letters A, C, G, T, U
if not re.fullmatch(r'[ACGTU]+', seq):
    print('The sequence is not DNA nor RNA')
else:
    # Now decide between DNA, RNA, or ambiguous
    has_t = 'T' in seq
    has_u = 'U' in seq

    if has_t and has_u:
        # contains both T and U → impossible
        print('The sequence is not DNA nor RNA')
    elif has_t:
        print('The sequence is DNA')
    elif has_u:
        print('The sequence is RNA')
    else:
        # only A, C, G → could be either
        print('The sequence can be DNA or RNA')

# Optional motif search
if args.motif:
    motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{motif}" in sequence "{seq}"... ', end='')
    if re.search(motif, seq):
        print('FOUND')
    else:
        print('NOT FOUND')
