# -*- coding: utf-8 -*-
__author__ = 'Ersan'

import os
import pandas as pd

id_stock = 1

def id_submission(row):
    """
    read row by row from DataFame
    concat columns to data_for_submission (in start empty DataFrame)
    :return: text columns Id,Predicted
    """
    global id_stock
    test_out = ''
    for ndx in range(len(row)):
        id_name = str(id_stock) + '_' + str(ndx + 1)
        test_out += id_name + ',' + str(row.values[ndx]) + '\n'
    id_stock += 1
    return test_out


if __name__ == '__main__':
    dir_path = os.getcwdu() + '\data\\'
    f_submission = 'test_submission.csv'
    f_train_in = 'train.csv'
    f_train_1000 = 'train_1000.csv'
    f_data_test = 'dummy_data.csv'

    df = pd.read_csv(dir_path + f_train_in, sep=None, engine='python') # read data for submission

    with open(dir_path+f_submission, 'w') as f_target:
        line_zero = 'Id,Predicted\n'
        f_target.write(line_zero)
        df.loc[:, 'Ret_121':'Ret_PlusTwo'].apply(lambda row: f_target.write(id_submission(row)), axis=1)
