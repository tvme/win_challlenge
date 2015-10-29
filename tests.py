# -*- coding: utf-8 -*-
__author__ = 'Ersan'

# import numpy as np
import pandas as pd
import os

def blanc_with_zeros(dir_path, file_in, col_start=None, col_end=None, write_file=False, file_out=None):
    """
    fill in the blanks with zeros
    if write_file is True, write result in file and return
    if write_file is False, return Data Frame
    """

    df = pd.read_csv(dir_path + file_in, sep=None, engine='python')
    df = df.loc[:, col_start:col_end].fillna(0)
    if write_file:
        df.to_csv(dir_path+file_out, index=False)
        return
    else:
        return df

if __name__ == '__main__':
    dir_path = os.getcwdu() + '\data\\'
    f_train_in = 'train.csv'
    f_test_in = 'test.csv'
    f_train_out = 'train_out.csv'
    f_test_out = 'test_out.csv'

    blanc_with_zeros(dir_path, f_test_in, 'Ret_2', 'Ret_120', True, f_test_out)
