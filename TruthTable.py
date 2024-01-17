import argparse

parser = argparse.ArgumentParser(description='Generate Truth Tables')
parser.add_argument('Expression', metavar='N', type=str, nargs='+',
                    help='Expression for the Truth Table')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))





#-M Markdown -L LaTeX -A Ascii -C Custom
parser.add_argument("-M", "--Markdown", help="Use Markdown Format")
parser.add_argument("-L", "--LaTeX", help="Use LaTeX Format")
parser.add_argument("-A", "--Ascii", help="Use Ascii Format")
parser.add_argument("-C", "--Custom", help="Use Custom Format")

args = parser.parse_args()

print()
