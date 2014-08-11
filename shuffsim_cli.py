#!/usr/bin/python
__author__ = 'Horea Christian'
import argparse
import shuffles
import formulae
import inspect

all_functions = inspect.getmembers(shuffles, inspect.isfunction)
all_formulae = inspect.getmembers(formulae, inspect.isfunction)

parser = argparse.ArgumentParser()
parser.add_argument("shuffle", help="Shuffle type to use, we currently support the following types of shuffles: "+', '.join([a[0] for a in all_functions])+".", type=str)
parser.add_argument("-d", "--deck-size", help="Specify the number of files in the deck.", default=52, type=int)
parser.add_argument("-t", "--tasmanian-down-number", help="Specify the number of files in the deck.", type=int)
parser.add_argument("-f", "--force-simulation", help="Do NOT use formulaic solutions (even when they are present), force actual simulation", action="store_true")
args = parser.parse_args()

if args.shuffle == "tasmanian" and args.tasmanian_down_number is None:
    parser.error("\"tasmanian\" requires --tasmanian-down-number specification")

if not args.force_simulation and args.shuffle in [a[0] for a in all_formulae]:
    if args.shuffle == "tasmanian":
        result = getattr(formulae, args.shuffle)(deck_size=args.deck_size, down_nr=args.tasmanian_down_number)
    else:
        result = getattr(formulae, args.shuffle)(deck_size=args.deck_size)    
else:
    if args.shuffle == "tasmanian":
        result = getattr(shuffles, args.shuffle)(deck_size=args.deck_size, down_nr=args.tasmanian_down_number)
    else:
        result = getattr(shuffles, args.shuffle)(deck_size=args.deck_size)

print(result)
