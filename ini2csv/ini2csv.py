import sys
import argparse
import configparser


class IniConfig:
    def __init__(self):
        self.config = configparser.ConfigParser()
        self.csv_config = {}
        self.condensed = {}

    def read_ini(self, file_name: argparse.FileType):
        self.config.read_string(file_name.read())
        for header in self.config:
            for key, value in self.config[header].items():
                self.config[header][key] = value

    def write_csv(self, file_name: argparse.FileType, collapsed: bool=False):
        for header in self.config:
            for key, value in self.config[header].items():
                file_name.write(f"{header},{key},{value}\n")


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
