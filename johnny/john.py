from argparse import ArgumentParser
from gooey import Gooey
import os
import sys

nonbuffered_stdout = os.fdopen(sys.stdout.fileno(), 'w')
sys.stdout = nonbuffered_stdout


@Gooey(program_name="Mytestprogram")
def parse_args():
    parser = ArgumentParser(description='Add description here')
    parser.add_argument('infile',
                        action='store',
                        default='infile1.txt',
                        help="Input file")
    parser.add_argument('outdir',
                        action='store',
                        default='outdir',
                        help="Output directory")
    parser.add_argument('outfile_name',
                        action='store',
                        default='outfile.txt',
                        help='Output file name')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    conf = parse_args()
    print("Done")