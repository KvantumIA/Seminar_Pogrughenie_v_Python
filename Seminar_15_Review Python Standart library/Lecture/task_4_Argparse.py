import argparse

parses = argparse.ArgumentParser(prog='average',
                                 description='My first argument parses',
                                 epilog='Return the arithmetic mean')

parses.add_argument('numbers', metavar='N', type=float, nargs='*',
                    help='press some numbers')

args = parses.parse_args()
print(f'В скрипт передано: {args}')


"""
python .\task_4_Argparse.py 42 3.14 73
python .\task_4_Argparse.py --help
"""


