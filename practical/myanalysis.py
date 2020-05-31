#!/usr/bin/env python

from argparse import ArgumentParser
import pandas as pd
import numpy as np


def main():
    parser = ArgumentParser(prog=__file__, description = "Assessment script for QLS612, May 2020, David MacDonald")
    parser.add_argument("brainsize_data_file", action="store", help = "Path to brainsize data file")
    bs_data = pd.read_csv(parser.parse_args().brainsize_data_file, sep=';', index_col=0)

    print(bs_data)

    # Add column of random noise
    bs_data['partY'] = np.random.normal(0,1,bs_data.shape[0])
    print(bs_data)

if __name__ == "__main__":
    main()

