import sys
import csv
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "infile",
        type=argparse.FileType("r"),
        default=sys.stdin
    )
    parser.add_argument(
        "outfile",
        type=str,
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

    dialect = csv.Sniffer().sniff(args.infile.read(1024))
    args.infile.seek(0)

    if not args.in_delimiter:
        args.in_delimiter = dialect.delimiter
    if not args.in_quote:
        args.in_quote = dialect.quotechar

    csv_file = csv.reader(args.infile, delimiter=args.in_delimiter, quotechar=args.in_quote)
    with open(args.outfile, 'w', newline='') as out_file:
        writing = csv.writer(out_file, quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writing.writerows(csv_file)


if __name__ == "__main__":
    main()
