import sys
import argparse


def find_delimiter(csv):
    return "|"


def find_quote(csv, quote):
    for line in csv:
        for item in range(len(line)):
            if line[item].find(",") != -1:
                line[item] = '"' + line[item] + '"'

    return csv


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

    csv = [x.split(args.in_delimiter) for x in old_csv]

    csv = find_quote(csv, args.in_quote)

    csv = [",".join(line) for line in csv]
    args.outfile.write('\n'.join(csv))


if __name__ == "__main__":
    main()
