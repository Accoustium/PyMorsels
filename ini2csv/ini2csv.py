import sys
import csv
import argparse
import configparser


class IniConfig:
    def __init__(self):
        self.config = {}

    def read_ini(self, file_name: argparse.FileType):
        reader = configparser.ConfigParser()
        reader.read_string(file_name.read())

        for header in reader.sections():
            if str(header) not in self.config.keys():
                self.config.update({header: {}})

            for key, value in reader.items(header):
                self.config[header].update({key: value})

    def write_csv(self, file_name: argparse.FileType, collapsed: bool = False):
        writer = csv.writer(file_name)
        if not collapsed:
            for header in self.config:
                for key, value in self.config[header].items():
                    writer.writerow([header, key, value])
        else:
            writer.writerow(['header', *list(self.config[list(self.config)[0]].keys())])
            for header in self.config:
                line = [header]
                for key, value in self.config[header].items():
                    line.append(value)
                writer.writerow(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "ini_file",
        type=argparse.FileType("r"),
        default=sys.stdin,
    )
    parser.add_argument(
        "csv_file",
        type=argparse.FileType("w"),
        default=sys.stdout,
    )
    parser.add_argument(
        "-c",
        "--collapsed",
        action="store_true",
        default=False,
    )
    args = parser.parse_args()

    ini = IniConfig()
    ini.read_ini(args.ini_file)
    ini.write_csv(args.csv_file, args.collapsed)
