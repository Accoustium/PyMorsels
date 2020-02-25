import sys
import csv
import argparse


def find_delimiter(csv):
    return "|"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        default=sys.stdin
    )
    parser.add_argument(
        "outfile",
        type=argparse.FileType("w"),
        default=sys.stdout
    )
    parser.add_argument(
        "--in-delimiter",
        type=str
    )
    parser.add_argument(
        "--in-quote",
        type=str
    )
    args = parser.parse_args()

    old_csv = args.infile.read()
    old_csv = old_csv.split("\n")

    if not args.in_delimiter:
        args.in_delimiter = find_delimiter(old_csv)

    csv_file = csv.reader(args.infile, delimiter=args.in_delimiter, quotechar=args.in_quote)

    args.outfile.write('\n'.join(csv))


if __name__ == "__main__":
    main()
