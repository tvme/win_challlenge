# -*- coding: utf-8 -*-
__author__ = 'Ersan'

import os
import pandas as pd


def data_to_submission(row):
    """
    read row by row from DataFame
    concat columns to data_for_submission (in start empty DataFrame)
    :return:
    """
    global id_stock, data_for_submission
    id_name = []
    for ndx in range(len(row)):
        name = str(id_stock) + '_' + str(ndx + 1)
        id_name.append(name)
    id_series = pd.DataFrame(row.values, index=id_name, columns=['Predicted'])
    id_stock += 1
    data_for_submission = pd.concat([data_for_submission, id_series])
    return

if __name__ == '__main__':
    dir_path = os.getcwdu() + '\data\\'
    f_train_in = 'train.csv'
    # f_test_in = 'test.csv'
    f_submission = 'sumission.csv'
    f_train_1000 = 'train_1000.csv'
    f_data_test = 'dummy_data.csv'
    id_stock = 1 # global index

    df = pd.read_csv(dir_path + f_data_test, sep=None, engine='python') # read data for submission
    data_for_submission = pd.DataFrame(columns=['Predicted']) # empty DataFrame for submission
    df = df.loc[:, 'Ret_121':'Ret_PlusTwo'].apply(data_to_submission, axis=1).copy
    data_for_submission.index.name = 'Id'
    print data_for_submission
    data_for_submission.to_csv(dir_path+f_submission)