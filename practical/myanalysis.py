#!/usr/bin/env python

from argparse import ArgumentParser
import pandas as pd

def main():
    parser = ArgumentParser(prog=__file__, description = "Assessment script for QLS612, May 2020, David MacDonald")
    parser.add_argument("brainsize_data_file", action="store", help = "Path to brainsize data file")
    bs_data = pd.read_csv(parser.parse_args().brainsize_data_file)

    print(bs_data)

if __name__ == "__main__":
    main()

