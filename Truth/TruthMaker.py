import argparse
from formats import format_as_ascii,format_as_csv, format_as_latex, format_as_markdown, format_as_custom
from table_maker import
def main():
    parser = argparse.ArgumentParser(description="Truth Table Maker")
    parser.add_argument('-f', '--format', choices=['markdown', 'latex', 'ascii', 'csv', 'custom'], default='ascii',
                        help="Specify the output format (markdown 'latex', 'ascii', 'csv)")

    parser.add_argument('values', metavar='value', type=str, nargs='+',
                        help="Input values for truth table generation")
    args = parser.parse_args()
    input_values = parse_input_values(args.values)

    truth_table = generate_truth_table(input_values)

    if args.format == 'ascii':
        formatted_table = format_as_ascii(truth_table)
    elif args.format == 'csv':
        formatted_table = format_as_csv(truth_table)
    elif args.format == 'custom':
        formatted_table = format_as_custom(truth_table)
    elif args.format == 'latex':
        formatted_table = format_as_latex()
    elif args.format == 'markdown':
        formatted_table = format_as_markdown(truth_table)

    print("Truth Table:")
    print(formatted_table)

if __name__ == "__main__":
    main()
