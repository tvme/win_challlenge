# -*- coding: utf-8 -*-
__author__ = 'Ersan'

# import numpy as np
import pandas as pd
import os

def blanc_with_zeros(dir_path, file_in, col_start=None, col_end=None, file_out=None):
    """
    fill in the blanks with zeros
    :return:
    """

    df = pd.read_csv(dir_path + file_in, sep=None, engine='python')
    df = df.loc[:, col_start:col_end].fillna(0)
    df.to_csv(dir_path+f_test_out, index=False)

if __name__ == '__main__':
    dir_path = os.getcwdu() + '\data\\'
    f_train_in = 'train.csv'
    f_test_in = 'tast.csv'
    f_train_out = 'train_out.csv'
    f_test_out = 'tast_out.csv'

    blanc_with_zeros(dir_path, f_test_in, 'Ret_2', 'Ret_120', f_test_out)
